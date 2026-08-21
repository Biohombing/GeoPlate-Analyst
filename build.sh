#!/bin/bash
# =============================================================================
# build.sh
# Build script for Linux / macOS -> executable binary
# Run with: bash build.sh
# =============================================================================

set -e   # Stop on error

echo ""
echo "============================================================"
echo " GEOPLATE ANALYST v1.0.0 - BUILD SCRIPT (Linux/Mac)"
echo "============================================================"
echo ""

# ── Check Python ────────────────────────────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo "[ERROR] python3 not found!"
    exit 1
fi
echo "[OK] $(python3 --version)"

# ── Install PyInstaller ───────────────────────────────────────────────────────
echo ""
echo "[1/4] Checking for PyInstaller ..."
python3 -c "import PyInstaller" 2>/dev/null || pip3 install pyinstaller
echo "[OK] PyInstaller ready"

# ── Install dependencies ────────────────────────────────────────────────────────
echo ""
echo "[2/4] Installing dependencies ..."
pip3 install -r requirements.txt
echo "[OK] Dependencies done"

# ── Clean previous build ──────────────────────────────────────────────────────
echo ""
echo "[3/4] Cleaning previous build ..."
rm -rf build dist
echo "[OK] Build folder cleaned"

# ── Build ─────────────────────────────────────────────────────────────────────
echo ""
echo "[4/4] Building the executable ..."
echo "(This process takes 3-10 minutes ...)"
echo ""

pyinstaller sundaland.spec --clean --noconfirm

echo ""
echo "============================================================"
echo "[SUCCESS] Build complete!"
echo ""
echo "Executable file available at: dist/GeoPlate Analyst"
echo ""
ls -lh "dist/GeoPlate Analyst" 2>/dev/null || echo "(file was not found in the dist/ folder)"
echo "============================================================"
