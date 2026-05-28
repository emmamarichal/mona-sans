#!/bin/bash
# build.sh - Font building script for Mona Sans
# run from the root!

set -e  # Exit on any error

# Check if running from the correct directory
if [ ! -f "sources/config.yaml" ]; then
  echo "Error: Please run this script from the root of the repository."
  exit 1
fi

# Build with gftools
echo "Building Mona Sans..."
gftools builder sources/config.yaml

echo "Building Mona Sans Mono..."
gftools builder sources/config-mono.yaml

# Run fontspector checks (run separately per family to avoid family name conflicts)
echo ""
echo "Running fontspector checks..."
mkdir -p Fontspector/"Mona Sans"
mkdir -p Fontspector/"Mona Sans Mono"

echo "Checking Mona Sans..."
gftools qa -f fonts/variable/MonaSans*.ttf fonts/static/ttf/MonaSans*.ttf -a -gfb --rust \
  --out Fontspector/"Mona Sans" \
  || echo "fontspector: Mona Sans checks completed with findings (see report)"

echo "Checking Mona Sans Mono..."
gftools qa -f fonts/variable/MonaSansMono*.ttf fonts/static/ttf/MonaSansMono*.ttf -a -gfb --rust \
  --out Fontspector/"Mona Sans Mono" \
  || echo "fontspector: Mona Sans Mono checks completed with findings (see report)"

echo ""
echo "Fontspector reports saved to Fontspector/"