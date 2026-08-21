@echo off
:: =============================================================================
:: BUILD.bat
:: Automated build script for GeoPlate Analyst -> .exe
:: Run by double-clicking, or from Command Prompt
:: =============================================================================

title GeoPlate Analyst v1.0.0 - Build EXE
color 0A

echo.
echo  ============================================================
echo   GEOPLATE ANALYST v1.0.0 - BUILD SCRIPT
echo   Building the application into an .exe file ...
echo  ============================================================
echo.

:: ── Check that Python is available ──────────────────────────────────────────────
python --version >nul 2>&1
if errorlevel 1 (
    echo  [ERROR] Python not found!
    echo  Please install Python 3.10+ from https://python.org
    pause
    exit /b 1
)

echo  [OK] Python found
python --version

:: ── Install PyInstaller if not already present ───────────────────────────────
echo.
echo  [1/4] Checking for PyInstaller ...
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo  [INFO] Installing PyInstaller ...
    pip install pyinstaller
    if errorlevel 1 (
        echo  [ERROR] Failed to install PyInstaller!
        pause
        exit /b 1
    )
)
echo  [OK] PyInstaller ready

:: ── Install all dependencies ─────────────────────────────────────────────────
echo.
echo  [2/4] Installing all dependencies ...
pip install -r requirements.txt
if errorlevel 1 (
    echo  [WARNING] Some packages may have failed to install.
    echo  Continuing build ...
)
echo  [OK] Dependencies done

:: ── Clean previous build ─────────────────────────────────────────────────────
echo.
echo  [3/4] Cleaning previous build ...
if exist "build" rmdir /s /q "build"
if exist "dist"  rmdir /s /q "dist"
echo  [OK] Build folders cleaned

:: ── Run PyInstaller ───────────────────────────────────────────────────────────
echo.
echo  [4/4] Building the .exe file ...
echo  (This process takes 3-10 minutes, please wait ...)
echo.

pyinstaller sundaland.spec --clean --noconfirm

if errorlevel 1 (
    echo.
    echo  ============================================================
    echo  [ERROR] Build FAILED!
    echo  Try running: python -m PyInstaller sundaland.spec
    echo  or check the error message above.
    echo  ============================================================
    pause
    exit /b 1
)

:: ── Done ─────────────────────────────────────────────────────────────────────
echo.
echo  ============================================================
echo  [SUCCESS] Build complete!
echo.
echo  The .exe file is available at:
echo  dist\GeoPlate Analyst.exe
echo.
echo  File size:
dir "dist\GeoPlate Analyst.exe" | findstr "GeoPlate"
echo  ============================================================
echo.

:: Automatically open the dist folder
explorer dist

pause
