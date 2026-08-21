# 📦 How to Build GeoPlate Analyst v1.0.0 → .EXE File

Complete guide to turning the Python application into an `.exe` file
that can be run directly without installing Python.

---

## ✅ Prerequisites

- Python 3.10 or newer installed
- Internet connection (to download PyInstaller and dependencies)
- Operating system: **Windows 10/11** (to produce the .exe)

Check Python:
```
python --version
```

---

## 🚀 How to Build (Windows) — EASIEST METHOD

### Step 1 — Open the project folder

Make sure you are inside the `GeoPlate_Analyst/` folder
that contains `main.py`, `BUILD.bat`, `sundaland.spec`, etc.

### Step 2 — Double-click BUILD.bat

Find the **`BUILD.bat`** file inside the folder, then **double-click** it.

This script will automatically:
1. Check for Python
2. Install PyInstaller
3. Install all dependencies from `requirements.txt`
4. Build the `.exe` file
5. Open the `dist/` folder containing the build output

⏳ This process takes **3–10 minutes** depending on your internet speed and computer.

### Step 3 — Get the .exe file

Once finished, the `.exe` file is at:
```
GeoPlate_Analyst/
└── dist/
    └── GeoPlate Analyst.exe   ← this is the one you share with others
```

---

## 🖥️ Manual Build (via Command Prompt)

If BUILD.bat doesn't run, do it manually:

```bash
# Open CMD in the GeoPlate_Analyst folder, then:

# Step 1: Install PyInstaller
pip install pyinstaller

# Step 2: Install all dependencies
pip install -r requirements.txt

# Step 3: Build
pyinstaller sundaland.spec --clean --noconfirm
```

---

## 🍎 Building on Linux / macOS

```bash
# In the terminal, go to the project folder:
cd GeoPlate_Analyst

# Grant execute permission
chmod +x build.sh

# Run it
bash build.sh
```

The build output is at `dist/GeoPlate Analyst` (no extension on Linux/Mac).

---

## 📁 Structure After Build

```
GeoPlate_Analyst/
├── dist/
│   └── GeoPlate Analyst.exe   ← BUILD OUTPUT FILE
├── build/                        ← temporary files (safe to delete)
├── main.py
├── sundaland.spec
├── BUILD.bat
└── ...
```

---

## 📤 Distributing to Others

Just copy **a single file**:
```
GeoPlate Analyst.exe
```

Send it via USB, Google Drive, email, or any other platform.

Users just need to **double-click** the file — no need to install Python,
no need to install any libraries.

---

## ❗ Build Troubleshooting

### Error: `ModuleNotFoundError` during build

Make sure all libraries are installed:
```bash
pip install -r requirements.txt
```

### Cartopy-related error

Cartopy sometimes needs to be installed via Conda:
```bash
conda install -c conda-forge cartopy pyinstaller
pyinstaller sundaland.spec --clean
```

### The .exe runs but an error appears when opening it

Try building with `--console` mode first to see the error:

Edit `sundaland.spec`, change the line:
```python
console=False   →   console=True
```
Then rebuild. A black window will appear showing the error message.

### Antivirus blocks the .exe

This is normal for PyInstaller-built .exe files. Add it to your antivirus
whitelist, or use a code signing certificate for commercial distribution.

### File size is too large

Normal size for this application: **150–400 MB**.
This is expected because the Python runtime and all libraries are bundled in.

To reduce the size:
1. Make sure UPX is installed: https://upx.github.io/
2. UPX is already enabled in `sundaland.spec` (`upx=True`)

---

## 🔄 Rebuilding After Code Changes

Every time you change the Python code, you need to rebuild:

```bash
# First remove the old build output
rmdir /s /q build dist

# Rebuild
pyinstaller sundaland.spec --clean --noconfirm
```

Or simply run `BUILD.bat` again.
