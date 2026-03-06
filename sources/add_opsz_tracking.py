#!/usr/bin/env python3
# add_opsz_tracking.py
# Injects optical-size-conditional kerning/tracking into a compiled variable font TTF.
# Replicates the Glyphs feature:
#   pos @All <14 0 14 0 (opsz:20) 9 0 9 0 (opsz:34) 4 0 4 0 (opsz:42) 17 0 17 0 (opsz:64) -2 0 -2 0 (opsz:100) 0 0 0 0>;
#
# This injects a GPOS FeatureVariations table with SingleAdjustment lookups
# conditioned on opsz ranges, applied to all glyphs via the 'dist' or 'kern' feature.
#
# Run after gftools builder:
#   python3 sources/add_opsz_tracking.py path/to/font.ttf

import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables

# opsz breakpoints and their ValueRecord (XPlacement, YPlacement, XAdvance, YAdvance)
# Syntax from Glyphs: <XPlacement 0 XAdvance 0 (opsz:VALUE)>
# Each entry means: "at opsz=VALUE, use these values" (linear interpolation between breakpoints)
# We model this as discrete opsz ranges with the closest breakpoint value.
#
# Original: <14 0 14 0 (opsz:20)  9 0 9 0 (opsz:34)  4 0 4 0 (opsz:42)  17 0 17 0 (opsz:64)  -2 0 -2 0 (opsz:100)  0 0 0 0>
# Format: (opsz_max_exclusive, x_placement, x_advance)
# The last entry (0 0 0 0) applies above opsz:100 — we ignore it (zero values = no adjustment needed).

OPSZ_TRACKING_RANGES = [
    # (opsz_upper_bound_exclusive, XPlacement, XAdvance)
    # Range: opsz < 20  → use <14 0 14 0>
    (20,  14, 14),
    # Range: 20 ≤ opsz < 34 → use <9 0 9 0>
    (34,   9,  9),
    # Range: 34 ≤ opsz < 42 → use <4 0 4 0>
    (42,   4,  4),
    # Range: 42 ≤ opsz < 64 → use <17 0 17 0>
    (64,  17, 17),
    # Range: 64 ≤ opsz < 100 → use <-2 0 -2 0>
    (100, -2, -2),
    # opsz >= 100 → <0 0 0 0> = no adjustment (skip)
]


def normalize_opsz(value, axis):
    """Normalize an opsz user-space value to [-1, 1] using the fvar axis mapping."""
    minimum = axis.minValue
    default = axis.defaultValue
    maximum = axis.maxValue
    if value <= minimum:
        return -1.0
    if value >= maximum:
        return 1.0
    if value < default:
        return -(default - value) / (default - minimum)
    if value > default:
        return (value - default) / (maximum - default)
    return 0.0


def get_or_create_gpos(font):
    """Return the GPOS table object, creating it if absent."""
    if "GPOS" not in font:
        gpos_obj = otTables.GPOS()
        gpos_obj.Version = 1.0
        gpos_obj.ScriptList = otTables.ScriptList()
        gpos_obj.ScriptList.ScriptRecord = []
        gpos_obj.ScriptList.ScriptCount = 0
        gpos_obj.FeatureList = otTables.FeatureList()
        gpos_obj.FeatureList.FeatureRecord = []
        gpos_obj.FeatureList.FeatureCount = 0
        gpos_obj.LookupList = otTables.LookupList()
        gpos_obj.LookupList.Lookup = []
        gpos_obj.LookupList.LookupCount = 0

        table = font.newTable("GPOS")
        table.table = gpos_obj
        font["GPOS"] = table

    return font["GPOS"].table


def find_opsz_axis(font):
    """Return (index, axis) for opsz in fvar, or (None, None)."""
    if "fvar" not in font:
        print("Error: font has no fvar table (not a variable font).")
        return None, None
    for i, axis in enumerate(font["fvar"].axes):
        if axis.axisTag == "opsz":
            return i, axis
    print("Error: opsz axis not found in fvar.")
    return None, None


def build_single_adjustment_lookup(glyph_order, x_placement, x_advance):
    """
    Build a GPOS LookupType 1 (SingleAdjustment) lookup
    applying the given XPlacement and XAdvance to all glyphs.
    """
    lookup = otTables.Lookup()
    lookup.LookupType = 1  # SingleAdjustment
    lookup.LookupFlag = 0

    subst = otTables.SinglePos()
    subst.Format = 1  # Apply same ValueRecord to all covered glyphs

    value_record = otTables.ValueRecord()
    value_record.XPlacement = x_placement
    value_record.XAdvance = x_advance

    subst.Value = value_record
    subst.ValueFormat = 0x0005  # XPlacement (0x0001) | XAdvance (0x0004)

    # Coverage: all glyphs
    coverage = otTables.Coverage()
    coverage.Format = 1
    coverage.glyphs = list(glyph_order)
    subst.Coverage = coverage

    lookup.SubTable = [subst]
    lookup.SubTableCount = 1
    return lookup


def get_or_create_dist_feature(gpos):
    """Find or create a 'dist' feature record in GPOS FeatureList. Returns index."""
    for i, fr in enumerate(gpos.FeatureList.FeatureRecord):
        if fr.FeatureTag == "dist":
            return i

    # Create dist feature
    fr = otTables.FeatureRecord()
    fr.FeatureTag = "dist"
    fr.Feature = otTables.Feature()
    fr.Feature.FeatureParams = None
    fr.Feature.LookupListIndex = []
    fr.Feature.LookupCount = 0
    gpos.FeatureList.FeatureRecord.append(fr)
    gpos.FeatureList.FeatureCount = len(gpos.FeatureList.FeatureRecord)

    # Register dist feature in all scripts
    feature_index = len(gpos.FeatureList.FeatureRecord) - 1
    for sr in gpos.ScriptList.ScriptRecord:
        script = sr.Script
        if script.DefaultLangSys is not None:
            if feature_index not in script.DefaultLangSys.FeatureIndex:
                script.DefaultLangSys.FeatureIndex.append(feature_index)
                script.DefaultLangSys.FeatureCount = len(script.DefaultLangSys.FeatureIndex)
        for lsr in script.LangSysRecord:
            if feature_index not in lsr.LangSys.FeatureIndex:
                lsr.LangSys.FeatureIndex.append(feature_index)
                lsr.LangSys.FeatureCount = len(lsr.LangSys.FeatureIndex)

    return feature_index


def add_opsz_tracking(font_path):
    """Inject GPOS FeatureVariations for opsz-conditional tracking."""
    font = TTFont(font_path)
    glyph_order = font.getGlyphOrder()

    opsz_index, opsz_axis = find_opsz_axis(font)
    if opsz_index is None:
        return

    gpos = get_or_create_gpos(font)

    # Ensure scripts exist — copy from GSUB if GPOS has none
    if gpos.ScriptList.ScriptCount == 0 and "GSUB" in font:
        import copy
        gpos.ScriptList = copy.deepcopy(font["GSUB"].table.ScriptList)

    dist_feature_index = get_or_create_dist_feature(gpos)

    # Build one lookup + one FeatureVariationRecord per opsz range
    fv_records = []

    # Track the lower bound for each range
    prev_upper = None  # below the first range = opsz < first breakpoint

    for i, (upper, xplacement, xadvance) in enumerate(OPSZ_TRACKING_RANGES):
        # Determine normalized opsz condition bounds
        norm_min = normalize_opsz(prev_upper if prev_upper is not None else opsz_axis.minValue, opsz_axis)
        norm_max = normalize_opsz(upper - 0.0001, opsz_axis)  # exclusive upper bound

        prev_upper = upper

        # Skip zero-adjustment range (opsz >= 100, no-op)
        if xplacement == 0 and xadvance == 0:
            continue

        # Build lookup
        lookup = build_single_adjustment_lookup(glyph_order, xplacement, xadvance)
        lookup_index = len(gpos.LookupList.Lookup)
        gpos.LookupList.Lookup.append(lookup)
        gpos.LookupList.LookupCount = len(gpos.LookupList.Lookup)

        # Build ConditionSet
        condition = otTables.ConditionTable()
        condition.Format = 1
        condition.AxisIndex = opsz_index
        condition.FilterRangeMinValue = norm_min
        condition.FilterRangeMaxValue = norm_max

        condition_set = otTables.ConditionSet()
        condition_set.Condition = [condition]
        condition_set.ConditionCount = 1

        # Build feature override pointing to this lookup
        feature = otTables.Feature()
        feature.FeatureParams = None
        feature.LookupListIndex = [lookup_index]
        feature.LookupCount = 1

        subst_record = otTables.FeatureTableSubstitutionRecord()
        subst_record.FeatureIndex = dist_feature_index
        subst_record.Feature = feature

        feature_subst = otTables.FeatureTableSubstitution()
        feature_subst.Version = 1.0
        feature_subst.SubstitutionRecord = [subst_record]
        feature_subst.SubstitutionCount = 1

        fv_record = otTables.FeatureVariationRecord()
        fv_record.ConditionSet = condition_set
        fv_record.FeatureTableSubstitution = feature_subst

        fv_records.append((upper, xplacement, fv_record))

    if not fv_records:
        print("No tracking rules to inject.")
        return

    # Add FeatureVariations to GPOS
    if not hasattr(gpos, "FeatureVariations") or gpos.FeatureVariations is None:
        gpos.FeatureVariations = otTables.FeatureVariations()
        gpos.FeatureVariations.Version = 1.0
        gpos.FeatureVariations.FeatureVariationRecord = []
        gpos.FeatureVariations.FeatureVariationCount = 0
        gpos.Version = 0x00010001  # GPOS version 1.1 required for FeatureVariations

    for _, _, fv_record in fv_records:
        gpos.FeatureVariations.FeatureVariationRecord.append(fv_record)
    gpos.FeatureVariations.FeatureVariationCount = len(
        gpos.FeatureVariations.FeatureVariationRecord
    )

    font.save(font_path)
    print(f"✓ Tracking rules injected into {font_path}")
    prev = opsz_axis.minValue
    for upper, xplacement, _ in fv_records:
        print(f"  opsz {prev}–{upper}: XPlacement={xplacement}, XAdvance={xplacement}")
        prev = upper


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 add_opsz_tracking.py path/to/font.ttf [path/to/font2.ttf ...]")
        sys.exit(1)
    for path in sys.argv[1:]:
        add_opsz_tracking(path)