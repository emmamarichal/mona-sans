#!/bin/bash
# build.sh - Font building script for Mona Sans
# run from the root!

set -e  # Exit on any error
# Check if running from the correct directory
if [ ! -f "sources/config.yaml" ]; then
  echo "Error: Please run this script from the root of the repository."
  exit 1
fi

# echo "Starting Mona Sans Google Fonts build process..."


# # Check for required tools
# command -v gftools >/dev/null 2>&1 || { echo "Error: gftools is required but not installed. Aborting."; exit 1; }
# command -v ttfautohint >/dev/null 2>&1 || { echo "Warning: ttfautohint not found. Install for best hinting results."; }

# # build googlefonts
# gftools builder sources/config.yaml

# # clean up build artifacts
# rm -rf sources/instance_ufos
# rm sources/.ninja_log
# rm sources/build.ninja

# # remove buggy .woff2 that gftools builder creates
# rm -f googlefonts/MonaSans[ital,wdth,wght].woff2

# echo "Google's Font files available in the 'googlefonts/' directory"


echo "Organizing font files..."

# Create necessary directories if they don't exist
mkdir -p fonts/static/ttf fonts/static/otf fonts/webfonts/static fonts/webfonts/variable fonts/variable

# Sort Glyphs generated VF (only move if files exist)
if ls fonts/*].woff2 1> /dev/null 2>&1; then
    mv fonts/*].woff2 fonts/webfonts/variable/
fi
if ls fonts/*].woff 1> /dev/null 2>&1; then
    mv fonts/*].woff fonts/webfonts/variable/
fi
if ls fonts/*].ttf 1> /dev/null 2>&1; then
    mv fonts/*].ttf fonts/variable/
fi

#Sort Glyphs generated static fonts (only move if files exist)
if ls fonts/*.ttf 1> /dev/null 2>&1; then
    mv fonts/*.ttf fonts/static/ttf/
fi
if ls fonts/*.otf 1> /dev/null 2>&1; then
    mv fonts/*.otf fonts/static/otf/
fi
if ls fonts/*.woff2 1> /dev/null 2>&1; then
    mv fonts/*.woff2 fonts/webfonts/static/
fi
if ls fonts/*.woff 1> /dev/null 2>&1; then
    mv fonts/*.woff fonts/webfonts/static/
fi

#check if there are any fonts in the wrong places
if [ "$(ls -A fonts/*.ttf 2>/dev/null)" ] || [ "$(ls -A fonts/*.otf 2>/dev/null)" ] || [ "$(ls -A fonts/*.woff2 2>/dev/null)" ] || [ "$(ls -A fonts/*.woff 2>/dev/null)" ]; then
  echo "!!! Warning: Some font files are still in the 'fonts/' directory. Please check and move them to the appropriate subdirectories."
fi

#Count files in each directory
echo "File counts by directory:"
echo "Variable TTF: $(ls -1 fonts/variable/*.ttf 2>/dev/null | wc -l)"
echo "Static TTF: $(ls -1 fonts/static/ttf/*.ttf 2>/dev/null | wc -l)"
echo "Static OTF: $(ls -1 fonts/static/otf/*.otf 2>/dev/null | wc -l)"
echo "Variable WOFF2: $(ls -1 fonts/webfonts/variable/*.woff2 2>/dev/null | wc -l)"
echo "Variable WOFF: $(ls -1 fonts/webfonts/variable/*.woff 2>/dev/null | wc -l)"
echo "Static WOFF2: $(ls -1 fonts/webfonts/static/*.woff2 2>/dev/null | wc -l)"
echo "Static WOFF: $(ls -1 fonts/webfonts/static/*.woff 2>/dev/null | wc -l)" 

