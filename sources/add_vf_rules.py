#!/usr/bin/env python3
# add_vf_rules.py
# Injects conditional substitution rules into a compiled variable font TTF.
# Activates ss05 (a), ss09 (Q), ss10 (J) alternates when opsz < 38
# by adding a FeatureVariations record referencing the existing lookups.
# Run after gftools builder: python3 sources/add_vf_rules.py path/to/font.ttf

import sys
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables import otTables

# Map: source glyph -> alternate glyph (to identify existing lookups)
SUBSTITUTIONS = {
    "a": "a.ss05",
    "Q": "Q.ss09",
    "J": "J.ss10",
}

# opsz axis condition: apply rules when opsz is below this value (user-space)
OPSZ_MAX = 38.0


def find_opsz_axis_index(font):
    if "fvar" not in font:
        print("Error: font has no fvar table.")
        return None, None
    for i, axis in enumerate(font["fvar"].axes):
        if axis.axisTag == "opsz":
            return i, axis
    print("Error: opsz axis not found.")
    return None, None


def normalize_with_avar(font, axis_tag, user_value):
    """Normalize a user-space value to [-1,1], applying avar if present."""
    axis = next(a for a in font["fvar"].axes if a.axisTag == axis_tag)
    minimum, default, maximum = axis.minValue, axis.defaultValue, axis.maxValue
    if user_value < default:
        n = (user_value - default) / (default - minimum) if default != minimum else 0.0
    elif user_value > default:
        n = (user_value - default) / (maximum - default) if maximum != default else 0.0
    else:
        n = 0.0
    n = max(-1.0, min(1.0, n))
    if "avar" in font:
        segment = font["avar"].segments.get(axis_tag)
        if segment:
            keys = sorted(segment.keys())
            for i in range(len(keys) - 1):
                k0, k1 = keys[i], keys[i + 1]
                if k0 <= n <= k1:
                    t = (n - k0) / (k1 - k0) if k1 != k0 else 0.0
                    return segment[k0] + t * (segment[k1] - segment[k0])
            n = segment[keys[0]] if n <= keys[0] else segment[keys[-1]]
    return n


def find_lookup_indices(font, substitutions):
    """Find existing GSUB lookup indices that perform the given substitutions."""
    gsub = font["GSUB"].table
    found = {}
    for i, lookup in enumerate(gsub.LookupList.Lookup):
        if lookup.LookupType != 1:
            continue
        for st in lookup.SubTable:
            if not hasattr(st, "mapping"):
                continue
            for src, dst in substitutions.items():
                if src in st.mapping and st.mapping[src] == dst:
                    found[src] = i
    return found


def get_or_create_feature(gsub, tag):
    """Find or create a feature with the given tag. Returns (index, feature_record)."""
    for i, fr in enumerate(gsub.FeatureList.FeatureRecord):
        if fr.FeatureTag == tag:
            return i, fr
    fr = otTables.FeatureRecord()
    fr.FeatureTag = tag
    fr.Feature = otTables.Feature()
    fr.Feature.FeatureParams = None
    fr.Feature.LookupListIndex = []
    fr.Feature.LookupCount = 0
    gsub.FeatureList.FeatureRecord.append(fr)
    gsub.FeatureList.FeatureCount = len(gsub.FeatureList.FeatureRecord)
    # Register in all scripts
    idx = len(gsub.FeatureList.FeatureRecord) - 1
    for sr in gsub.ScriptList.ScriptRecord:
        script = sr.Script
        if script.DefaultLangSys is not None:
            if idx not in script.DefaultLangSys.FeatureIndex:
                script.DefaultLangSys.FeatureIndex.append(idx)
                script.DefaultLangSys.FeatureCount = len(script.DefaultLangSys.FeatureIndex)
        for lsr in script.LangSysRecord:
            if idx not in lsr.LangSys.FeatureIndex:
                lsr.LangSys.FeatureIndex.append(idx)
                lsr.LangSys.FeatureCount = len(lsr.LangSys.FeatureIndex)
    return idx, fr


def add_rvrn_rules(font_path):
    font = TTFont(font_path)

    # Find existing lookup indices for our substitutions
    lookup_map = find_lookup_indices(font, SUBSTITUTIONS)
    if not lookup_map:
        print("No matching lookups found in font. Aborting.")
        return

    lookup_indices = sorted(set(lookup_map.values()))
    print(f"Found lookups: { {src: lookup_map[src] for src in lookup_map} }")

    opsz_index, opsz_axis = find_opsz_axis_index(font)
    if opsz_index is None:
        return

    normalized_max = normalize_with_avar(font, "opsz", OPSZ_MAX)
    print(f"opsz={OPSZ_MAX} normalizes to {normalized_max:.6f} (AxisIndex={opsz_index})")

    gsub = font["GSUB"].table

    # Use a dedicated 'calt' feature for opsz-conditional substitutions
    # (rvrn is problematic as gftools already uses FeatureVariations for other things)
    base_feature_idx, base_feature_rec = get_or_create_feature(gsub, "calt")

    # Build ConditionSet: opsz in [-1, normalized_max] i.e. opsz < 38
    condition = otTables.ConditionTable()
    condition.Format = 1
    condition.AxisIndex = opsz_index
    condition.FilterRangeMinValue = -1.0
    condition.FilterRangeMaxValue = normalized_max

    condition_set = otTables.ConditionSet()
    condition_set.ConditionTable = [condition]
    condition_set.ConditionCount = 1

    # Feature override: activate our lookups for this condition
    feature_override = otTables.Feature()
    feature_override.FeatureParams = None
    feature_override.LookupListIndex = lookup_indices
    feature_override.LookupCount = len(lookup_indices)

    subst_record = otTables.FeatureTableSubstitutionRecord()
    subst_record.FeatureIndex = base_feature_idx
    subst_record.Feature = feature_override

    feature_subst = otTables.FeatureTableSubstitution()
    feature_subst.Version = 1.0
    feature_subst.SubstitutionRecord = [subst_record]
    feature_subst.SubstitutionCount = 1

    fv_record = otTables.FeatureVariationRecord()
    fv_record.ConditionSet = condition_set
    fv_record.FeatureTableSubstitution = feature_subst

    # Ensure GSUB version 1.1 and FeatureVariations exist
    if not hasattr(gsub, "FeatureVariations") or gsub.FeatureVariations is None:
        gsub.FeatureVariations = otTables.FeatureVariations()
        gsub.FeatureVariations.Version = 1.0
        gsub.FeatureVariations.FeatureVariationRecord = []
        gsub.FeatureVariations.FeatureVariationCount = 0
    gsub.Version = 0x00010001

    # Insert at position 0 — first match wins
    gsub.FeatureVariations.FeatureVariationRecord.insert(0, fv_record)
    gsub.FeatureVariations.FeatureVariationCount = len(
        gsub.FeatureVariations.FeatureVariationRecord
    )

    font.save(font_path)
    print(f"✓ Rules injected into {font_path}")
    for src, dst in SUBSTITUTIONS.items():
        print(f"  {src} → {dst}  (when opsz < {OPSZ_MAX})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 add_vf_rules.py path/to/font.ttf [...]")
        sys.exit(1)
    for path in sys.argv[1:]:
        add_rvrn_rules(path)