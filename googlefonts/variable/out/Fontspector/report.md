## FontSpector report

fontspector version: 1.5.4






## Check results




<details><summary>[4] </summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Ensure VFs have 'ital' STAT axis. (opentype/STAT/ital_axis)</summary>
    <div>








- ⚠️ **WARN** MonaSans-Italic[opsz,wdth,wght].ttf has STAT table 'ital' axis with wrong flags. Expected: (empty), got 'ELIDABLE_AXIS_VALUE_NAME' [code: wrong-ital-axis-flag]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>








- ⚠️ **WARN** MonaSans-Italic[opsz,wdth,wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, math, cherokee, coptic
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, math, canadian-aboriginal, tifinagh, syriac, todhri, tai-le, duployan, coptic, malayalam, old-permic
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
... and 71 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** MonaSans[opsz,wdth,wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, math, cherokee, coptic
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, math, canadian-aboriginal, tifinagh, syriac, todhri, tai-le, duployan, coptic, malayalam, old-permic
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
... and 71 others

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Check for presence of an ARTICLE.en_us.html file (googlefonts/description/has_article)</summary>
    <div>








- ℹ️ **INFO** This font doesn't have an ARTICLE.en_us.html file. [code: missing-article]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Check axis ordering on the STAT table. (googlefonts/STAT/axis_order)</summary>
    <div>








- ℹ️ **INFO** None of the fonts lack a STAT table.

	And these are the most common STAT axis orderings:
	wdth-wght-opsz-ital: 2 [code: summary]
  
  

</div>
</details>


</div>
</details>


<details><summary>[16] MonaSans-Italic[opsz,wdth,wght].ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Axes and named instances fall within correct ranges? (opentype/fvar/regular_coords_correct)</summary>
    <div>








- ⚠️ **WARN** Regular instance has opsz coordinate of 8, expected between 10 and 16 [code: opsz]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>








- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. (interpolation_issues)</summary>
    <div>








- ⚠️ **WARN** Glyph zero.tf has interpolation issues:
* Wrong start point: contour 1 should start at 1 in wdth=75 [code: glyph]
  
  


- ⚠️ **WARN** Glyph zero.tf has interpolation issues:
* Wrong start point: contour 1 should start at 1 in wdth=75,opsz=100 [code: glyph]
  
  


- ⚠️ **WARN** Glyph zero.tf.ss08 has interpolation issues:
* Wrong start point: contour 1 should start at 1 in wdth=75 [code: glyph]
  
  


- ⚠️ **WARN** Glyph zero.tf.ss08 has interpolation issues:
* Wrong start point: contour 1 should start at 1 in wdth=75,opsz=100 [code: glyph]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? (ligature_carets)</summary>
    <div>








- ⚠️ **WARN** This font lacks caret positioning values for these ligature glyphs:

* f_f.liga
* f_y.liga
* f_f_i.liga
* fl
* fi
* fi.ss01
* f_f_i.liga.ss01 [code: incomplete-caret-pos-data]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* f.longarm
* f_f.liga
* f_f_i.liga
* f_y.liga [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? (valid_glyphnames)</summary>
    <div>








- ⚠️ **WARN** The following glyph names are too long: "periodcentered.loclCAT.case.ss01" [code: legacy-long-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts have relatively consistent sidebearings. (suspicious_sidebearings)</summary>
    <div>








- ⚠️ **WARN** Glyph "uni0336" has suspiciously high variation (z-score 10.51) in right sidebearings at locations:
    wdth=75.00, wght=200.00, opsz=8.00
    wdth=75.00, wght=277.56, opsz=8.00 [code: large-rsb-variation]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages              |
|-------------------------------------------------------------------|------------------------|
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)     |
|   The following auxiliary characters are missing from the font: ſ |                        |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)     |
|   The following auxiliary characters are missing from the font: Ǿ |                        |
|   The following auxiliary characters are missing from the font: ǿ |                        |
| Auxiliary orthography codepoints:                                 | * de_Latn (German)     |
|   The following auxiliary characters are missing from the font: Ŏ |                        |
|   The following auxiliary characters are missing from the font: ŏ |                        |
|   The following auxiliary characters are missing from the font: ſ |                        |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)    |
|   The following auxiliary characters are missing from the font: Ŏ | * cs_Latn (Czech)      |
|   The following auxiliary characters are missing from the font: ŏ | * cy_Latn (Welsh)      |
|                                                                   | * es_Latn (Spanish)    |
|                                                                   | * hu_Latn (Hungarian)  |
|                                                                   | * pt_Latn (Portuguese) |
|                                                                   | * sk_Latn (Slovak)     |
|                                                                   | * tr_Latn (Turkish)    |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)    |
|   The following auxiliary characters are missing from the font: Ŏ |                        |
|   The following auxiliary characters are missing from the font: ŏ |                        |
|   The following auxiliary characters are missing from the font: ʻ |                        |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)    |
|   The following auxiliary characters are missing from the font: Ǥ |                        |
|   The following auxiliary characters are missing from the font: Ȟ |                        |
|   The following auxiliary characters are missing from the font: Ǩ |                        |
|   The following auxiliary characters are missing from the font: Ʒ |                        |
|   The following auxiliary characters are missing from the font: Ǯ |                        |
|   The following auxiliary characters are missing from the font: ǥ |                        |
|   The following auxiliary characters are missing from the font: ȟ |                        |
|   The following auxiliary characters are missing from the font: ǩ |                        |
|   The following auxiliary characters are missing from the font: ʒ |                        |
|   The following auxiliary characters are missing from the font: ǯ |                        | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:

* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>








- ⚠️ **WARN** The following glyphs have overlapping path segments:

* f_f.liga: Line(Line { p0: (328.0, 485.0), p1: (335.0, 517.0) }) has the same coordinates as a previous segment.
* f_f_i.liga: Line(Line { p0: (328.0, 485.0), p1: (335.0, 517.0) }) has the same coordinates as a previous segment.
* f_f_i.liga: Line(Line { p0: (594.0, 517.0), p1: (587.0, 485.0) }) has the same coordinates as a previous segment.
* fi (U+FB01): Line(Line { p0: (335.0, 517.0), p1: (328.0, 485.0) }) has the same coordinates as a previous segment.
* fl (U+FB02): Line(Line { p0: (335.0, 517.0), p1: (328.0, 485.0) }) has the same coordinates as a previous segment.
* fi.ss01: Line(Line { p0: (335.0, 517.0), p1: (328.0, 485.0) }) has the same coordinates as a previous segment.
* f_f_i.liga.ss01: Line(Line { p0: (328.0, 485.0), p1: (335.0, 517.0) }) has the same coordinates as a previous segment.
* f_f_i.liga.ss01: Line(Line { p0: (594.0, 517.0), p1: (587.0, 485.0) }) has the same coordinates as a previous segment. [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'GTHB' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Show hinting filesize impact. (hinting_impact)</summary>
    <div>








- ℹ️ **INFO** Hinting filesize impact:

 |               | MonaSans-Italic[opsz,wdth,wght].ttf     |
 |:------------- | ---------------:|
 | Dehinted Size | 603448 |
 | Hinted Size   | 603472   |
 | Increase      | 24      |
 | Change        | 0.0 %  | [code: size-impact]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Font contains all required tables? (required_tables)</summary>
    <div>








- ℹ️ **INFO** This font contains the following optional tables:

    loca
    prep
    GPOS
    GSUB
    gasp [code: optional-tables]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>








- ℹ️ **INFO** These are the ppm ranges declared on the gasp table:

| PPM <= 65535 | - Use grid-fitting                                    |
|              | 	- Use grayscale rendering                            |
|              | 	- Use gridfitting with ClearType symmetric smoothing |
|              | 	- Use smoothing along multiple axes with ClearType®  |
|--------------|-------------------------------------------------------|
 [code: ranges]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Font has old ttfautohint applied? (googlefonts/old_ttfautohint)</summary>
    <div>








- ℹ️ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: Version 2.022 [code: version-not-detected]
  
  

</div>
</details>


</div>
</details>


<details><summary>[18] MonaSans[opsz,wdth,wght].ttf</summary>
<div>


<details>
    <summary>🔥 <b>FAIL</b> Validates subfamilyNameID and postScriptNameID for the default instance record (opentype/varfont/valid_default_instance_nameids)</summary>
    <div>








- 🔥 **FAIL** ExtraLight instance has the same coordinates as the default instance; its subfamily name should be 8pt ExtraLight.

Note: It is alternatively possible that Name ID 17 is incorrect, and should be set to the default instance subfamily name, 8pt ExtraLight, rather than '8pt ExtraLight'. If the default instance is ExtraLight, NameID 17 is probably the problem. [code: invalid-default-instance-subfamily-name]
  
  


- 🔥 **FAIL** ExtraLight instance has the same coordinates as the default instance; its postscript name should be MonaSans-8ptExtraLight instead of MonaSans-ExtraLight. [code: invalid-default-instance-postscript-name]
  
  

</div>
</details>





<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct (googlefonts/font_names)</summary>
    <div>








- 🔥 **FAIL** Font names are incorrect:

| Name                       | Current                      | Expected                 |
|----------------------------|------------------------------|--------------------------|
| Family Name                | **Mona Sans 8pt ExtraLight** | **Mona Sans ExtraLight** |
| Subfamily Name             | Regular                      | Regular                  |
| Full Name                  | **Mona Sans 8pt ExtraLight** | **Mona Sans ExtraLight** |
| Postscript Name            | **MonaSans-8ptExtraLight**   | **MonaSans-ExtraLight**  |
| Typographic Family Name    | Mona Sans                    | Mona Sans                |
| Typographic Subfamily Name | **8pt ExtraLight**           | **ExtraLight**           | [code: bad-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Axes and named instances fall within correct ranges? (opentype/fvar/regular_coords_correct)</summary>
    <div>








- ⚠️ **WARN** Regular instance has opsz coordinate of 8, expected between 10 and 16 [code: opsz]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron (alt_caron)</summary>
    <div>








- ⚠️ **WARN** Lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** lcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  


- ⚠️ **WARN** tcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. (interpolation_issues)</summary>
    <div>








- ⚠️ **WARN** Glyph Y has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph Yacute has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph Ycircumflex has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph Ydieresis has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph uni1EF4 has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph Ygrave has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph uni1EF6 has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph uni1EF8 has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph Ydieresis.ss01 has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  


- ⚠️ **WARN** Glyph uni1EF4.ss01 has interpolation issues:
* Contour 0 becomes underweight in wdth=75 compared to default [code: glyph]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? (ligature_carets)</summary>
    <div>








- ⚠️ **WARN** This font lacks caret positioning values for these ligature glyphs:

* f_f_i.liga.ss01
* f_y.liga
* fi
* fl
* fi.ss01
* f_f.liga
* f_f_i.liga [code: incomplete-caret-pos-data]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs (unreachable_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

* f.longarm
* f_f.liga
* f_f_i.liga
* f_y.liga [code: unreachable-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? (valid_glyphnames)</summary>
    <div>








- ⚠️ **WARN** The following glyph names are too long: "periodcentered.loclCAT.case.ss01" [code: legacy-long-names]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts have relatively consistent sidebearings. (suspicious_sidebearings)</summary>
    <div>








- ⚠️ **WARN** Glyph "uni0336" has suspiciously high variation (z-score 13.02) in right sidebearings at locations:
    wdth=75.00, wght=200.00, opsz=8.00
    wdth=75.00, wght=200.00, opsz=100.00
    wdth=75.00, wght=277.56, opsz=8.00
    wdth=75.00, wght=277.56, opsz=100.00
    wdth=75.00, wght=365.13, opsz=8.00
    wdth=75.00, wght=365.13, opsz=100.00
    wdth=75.00, wght=464.58, opsz=8.00
    wdth=75.00, wght=464.58, opsz=100.00
    wdth=75.00, wght=599.99, opsz=8.00 [code: large-rsb-variation]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>








- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages              |
|-------------------------------------------------------------------|------------------------|
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)    |
|   The following auxiliary characters are missing from the font: Ǥ |                        |
|   The following auxiliary characters are missing from the font: Ȟ |                        |
|   The following auxiliary characters are missing from the font: Ǩ |                        |
|   The following auxiliary characters are missing from the font: Ʒ |                        |
|   The following auxiliary characters are missing from the font: Ǯ |                        |
|   The following auxiliary characters are missing from the font: ǥ |                        |
|   The following auxiliary characters are missing from the font: ȟ |                        |
|   The following auxiliary characters are missing from the font: ǩ |                        |
|   The following auxiliary characters are missing from the font: ʒ |                        |
|   The following auxiliary characters are missing from the font: ǯ |                        |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)    |
|   The following auxiliary characters are missing from the font: Ŏ |                        |
|   The following auxiliary characters are missing from the font: ŏ |                        |
|   The following auxiliary characters are missing from the font: ʻ |                        |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)    |
|   The following auxiliary characters are missing from the font: Ŏ | * cs_Latn (Czech)      |
|   The following auxiliary characters are missing from the font: ŏ | * cy_Latn (Welsh)      |
|                                                                   | * es_Latn (Spanish)    |
|                                                                   | * hu_Latn (Hungarian)  |
|                                                                   | * pt_Latn (Portuguese) |
|                                                                   | * sk_Latn (Slovak)     |
|                                                                   | * tr_Latn (Turkish)    |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)     |
|   The following auxiliary characters are missing from the font: Ǿ |                        |
|   The following auxiliary characters are missing from the font: ǿ |                        |
| Auxiliary orthography codepoints:                                 | * de_Latn (German)     |
|   The following auxiliary characters are missing from the font: Ŏ |                        |
|   The following auxiliary characters are missing from the font: ŏ |                        |
|   The following auxiliary characters are missing from the font: ſ |                        |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)     |
|   The following auxiliary characters are missing from the font: ſ |                        | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Font has correct separator glyphs? (googlefonts/separator_glyphs)</summary>
    <div>








- ⚠️ **WARN** The following separator glyphs are missing:

* U+2028
* U+2029 [code: missing-separator-glyphs]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (googlefonts/meta/script_lang_tags)</summary>
    <div>








- ⚠️ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>








- ⚠️ **WARN** OS/2 VendorID value 'GTHB' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Checking OS/2 fsSelection value. (opentype/xavgcharwidth)</summary>
    <div>








- ℹ️ **INFO** OS/2 xAvgCharWidth is 552 but it should be 551 which corresponds to the average of the widths of all glyphs in the font. These are similar values, which may be a symptom of the slightly different calculation of the xAvgCharWidth value in font editors. There's further discussion on this at https://github.com/fonttools/fontbakery/issues/1622 [code: xAvgCharWidth-close]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Show hinting filesize impact. (hinting_impact)</summary>
    <div>








- ℹ️ **INFO** Hinting filesize impact:

 |               | MonaSans[opsz,wdth,wght].ttf     |
 |:------------- | ---------------:|
 | Dehinted Size | 631468 |
 | Hinted Size   | 631492   |
 | Increase      | 24      |
 | Change        | 0.0 %  | [code: size-impact]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Font contains all required tables? (required_tables)</summary>
    <div>








- ℹ️ **INFO** This font contains the following optional tables:

    loca
    prep
    GPOS
    GSUB
    gasp [code: optional-tables]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Is the Grid-fitting and Scan-conversion Procedure ('gasp') table
set to optimize rendering? (googlefonts/gasp)</summary>
    <div>








- ℹ️ **INFO** These are the ppm ranges declared on the gasp table:

| PPM <= 65535 | - Use grid-fitting                                    |
|              | 	- Use grayscale rendering                            |
|              | 	- Use gridfitting with ClearType symmetric smoothing |
|              | 	- Use smoothing along multiple axes with ClearType®  |
|--------------|-------------------------------------------------------|
 [code: ranges]
  
  

</div>
</details>





<details>
    <summary>ℹ️ <b>INFO</b> Font has old ttfautohint applied? (googlefonts/old_ttfautohint)</summary>
    <div>








- ℹ️ **INFO** Could not detect which version of ttfautohint was used in this font. It is typically specified as a comment in the font version entries of the 'name' table. Such font version strings are currently: Version 2.022 [code: version-not-detected]
  
  

</div>
</details>


</div>
</details>






### Summary

| 🔥 FAIL | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 3 | 44 | 11 | 223 | 78 | 
| 1% | 13% | 3% | 66% | 23% | 



