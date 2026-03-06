#!/usr/bin/env python3
# add_vf_rules.py
# Injects conditional substitution rules into a compiled variable font TTF.
# Equivalent to Glyphs' #ifdef VARIABLE / condition opsz < 38 syntax.
# Run after gftools builder: python3 sources/add_vf_rules.py path/to/font.ttf

import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables

# Substitutions to apply when opsz < 38
# Format: { "source_glyph": "alternate_glyph" }
SUBSTITUTIONS = {
    "a": "a.ss05",
    "Q": "Q.ss09",
    "J": "J.ss10",
}

# opsz axis condition: apply rules when opsz is below this value
OPSZ_MAX = 37.9999  # exclusive upper bound (i.e. opsz < 38)


def build_single_subst_lookup(font, substitutions):
    """Build a SingleSubst lookup table for the given glyph substitutions."""
    lookup = otTables.Lookup()
    lookup.LookupType = 1  # SingleSubst
    lookup.LookupFlag = 0

    subst = otTables.SingleSubst()
    subst.mapping = substitutions
    lookup.SubTable = [subst]
    lookup.SubTableCount = 1
    return lookup


def get_or_create_gsub(font):
    """Return the GSUB table, creating it if it doesn't exist."""
    if "GSUB" not in font:
        gsub = otTables.GSUB()
        gsub.Version = 1.0
        gsub.ScriptList = otTables.ScriptList()
        gsub.ScriptList.ScriptRecord = []
        gsub.FeatureList = otTables.FeatureList()
        gsub.FeatureList.FeatureRecord = []
        gsub.LookupList = otTables.LookupList()
        gsub.LookupList.Lookup = []

        table = font.newTable("GSUB")
        table.table = gsub
        font["GSUB"] = table

    return font["GSUB"].table


def find_opsz_axis_index(font):
    """Return the index of the opsz axis in fvar, or None if not found."""
    if "fvar" not in font:
        print("Error: font has no fvar table (not a variable font).")
        return None
    for i, axis in enumerate(font["fvar"].axes):
        if axis.axisTag == "opsz":
            return i
    print("Error: opsz axis not found in fvar.")
    return None


def add_rvrn_rules(font_path):
    """Inject rvrn substitution rules conditioned on opsz < 38."""
    font = TTFont(font_path)
    glyph_order = font.getGlyphOrder()

    # Check that all alternate glyphs exist in the font
    valid_subs = {}
    for src, dst in SUBSTITUTIONS.items():
        if src not in glyph_order:
            print(f"Warning: source glyph '{src}' not found, skipping.")
            continue
        if dst not in glyph_order:
            print(f"Warning: alternate glyph '{dst}' not found, skipping.")
            continue
        valid_subs[src] = dst

    if not valid_subs:
        print("No valid substitutions found. Aborting.")
        return

    opsz_index = find_opsz_axis_index(font)
    if opsz_index is None:
        return

    gsub = get_or_create_gsub(font)

    # Build the SingleSubst lookup
    lookup = build_single_subst_lookup(font, valid_subs)

    # Add lookup to LookupList
    lookup_index = len(gsub.LookupList.Lookup)
    gsub.LookupList.Lookup.append(lookup)
    gsub.LookupList.LookupCount = len(gsub.LookupList.Lookup)

    # Build FeatureVariations (rvrn) with opsz condition
    # opsz axis value must be normalized: map 38 to its normalized value
    opsz_axis = font["fvar"].axes[opsz_index]
    
    def normalize(value, minimum, default, maximum):
        """Normalize an axis value to [-1, 1] range."""
        if value < default:
            return (value - default) / (default - minimum) if default != minimum else 0
        elif value > default:
            return (value - default) / (maximum - default) if maximum != default else 0
        return 0.0

    normalized_max = normalize(
        OPSZ_MAX,
        opsz_axis.minValue,
        opsz_axis.defaultValue,
        opsz_axis.maxValue,
    )

    # Build ConditionSet: opsz <= normalized_max (i.e. opsz < 38)
    condition = otTables.ConditionTable()
    condition.Format = 1
    condition.AxisIndex = opsz_index
    condition.FilterRangeMinValue = -1.0  # from minimum
    condition.FilterRangeMaxValue = normalized_max

    condition_set = otTables.ConditionSet()
    condition_set.Condition = [condition]
    condition_set.ConditionCount = 1

    # Build FeatureTableSubstitution entry pointing to our lookup
    feature = otTables.Feature()
    feature.FeatureParams = None
    feature.LookupListIndex = [lookup_index]
    feature.LookupCount = 1

    subst_record = otTables.FeatureTableSubstitutionRecord()
    # rvrn feature index: find or create it
    rvrn_feature_index = None
    for i, fr in enumerate(gsub.FeatureList.FeatureRecord):
        if fr.FeatureTag == "rvrn":
            rvrn_feature_index = i
            break

    if rvrn_feature_index is None:
        # Create rvrn feature record
        fr = otTables.FeatureRecord()
        fr.FeatureTag = "rvrn"
        fr.Feature = otTables.Feature()
        fr.Feature.FeatureParams = None
        fr.Feature.LookupListIndex = []
        fr.Feature.LookupCount = 0
        gsub.FeatureList.FeatureRecord.insert(0, fr)
        gsub.FeatureList.FeatureCount = len(gsub.FeatureList.FeatureRecord)
        rvrn_feature_index = 0

    subst_record.FeatureIndex = rvrn_feature_index
    subst_record.Feature = feature

    feature_subst = otTables.FeatureTableSubstitution()
    feature_subst.Version = 1.0
    feature_subst.SubstitutionRecord = [subst_record]
    feature_subst.SubstitutionCount = 1

    # Build FeatureVariationRecord
    fv_record = otTables.FeatureVariationRecord()
    fv_record.ConditionSet = condition_set
    fv_record.FeatureTableSubstitution = feature_subst

    # Add FeatureVariations to GSUB
    if not hasattr(gsub, "FeatureVariations") or gsub.FeatureVariations is None:
        gsub.FeatureVariations = otTables.FeatureVariations()
        gsub.FeatureVariations.Version = 1.0
        gsub.FeatureVariations.FeatureVariationRecord = []
        gsub.FeatureVariations.FeatureVariationCount = 0
        gsub.Version = 0x00010001  # GSUB version 1.1 required for FeatureVariations

    gsub.FeatureVariations.FeatureVariationRecord.append(fv_record)
    gsub.FeatureVariations.FeatureVariationCount = len(
        gsub.FeatureVariations.FeatureVariationRecord
    )

    font.save(font_path)
    print(f"✓ Rules injected into {font_path}")
    for src, dst in valid_subs.items():
        print(f"  {src} → {dst}  (when opsz < 38)")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 add_vf_rules.py path/to/font.ttf [path/to/font2.ttf ...]")
        sys.exit(1)
    for path in sys.argv[1:]:
        add_rvrn_rules(path)