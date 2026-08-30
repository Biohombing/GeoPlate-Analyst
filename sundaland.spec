# -*- mode: python ; coding: utf-8 -*-
# =============================================================================
# sundaland.spec
# PyInstaller specification file for GeoPlate Analyst
#
# Usage:
#   pyinstaller sundaland.spec
#
# Output: dist/GeoPlate Analyst.exe
# =============================================================================

import sys
import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# ── Collect all required data files ────────────────────────────────────────────

datas = []

# Cartopy: Requires internal shapefile data (coastlines, borders, etc.)
try:
    import cartopy
    cartopy_dir = os.path.dirname(cartopy.__file__)
    datas += [(os.path.join(cartopy_dir, 'data'), 'cartopy/data')]
    datas += [(os.path.join(cartopy_dir, 'io'),   'cartopy/io')]
    # Cartopy shapefiles (Natural Earth)
    import cartopy.io.shapereader as shp
    ne_dir = shp.natural_earth.__module__
    datas += collect_data_files('cartopy')
except ImportError:
    pass

# Matplotlib: data fonts dan style
datas += collect_data_files('matplotlib')

# UI stylesheet
datas += [('ui/style_light.qss', 'ui'), ('ui/style_dark.qss', 'ui')]
datas += [('assets/compass_rose.png', 'assets')]
# Natural Earth map data (50m) previously downloaded and cached by Cartopy
# on the build computer (see the guide) -> bundled into ‘cartopy_data’ inside the .exe.
datas += [(r'C:\Users\HP\.local\share\cartopy', 'cartopy_data')]

# ── Hidden imports (libraries not detected automatically) ─────────────────────

hiddenimports = ['PIL', 'PIL._imaging']

# Cartopy submodules
hiddenimports += collect_submodules('cartopy')

# Matplotlib backends
hiddenimports += [
    'matplotlib.backends.backend_qtagg',
    'matplotlib.backends.backend_agg',
]

# PyQt6 modules
hiddenimports += [
    'PyQt6.QtCore',
    'PyQt6.QtGui',
    'PyQt6.QtWidgets',
    'PyQt6.sip',
]

# Pandas & Excel
hiddenimports += [
    'pandas',
    'openpyxl',
    'openpyxl.styles',
    'openpyxl.utils',
]

# Numpy & Scipy (Used internally by Cartopy)
hiddenimports += [
    'numpy',
    'numpy.core._multiarray_umath',
    'scipy',
    'scipy.special',
    'scipy.spatial',
]

# Shapely (dipakai Cartopy)
hiddenimports += collect_submodules('shapely')

# ── Analysis ──────────────────────────────────────────────────────────────────

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=['.'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude unused files (reduce file size)
        'tkinter',
        'wx',
        'PySide2',
        'PySide6',
        'PyQt5',
        'IPython',
        'jupyter',
        'notebook',
        'pytest',
        'sphinx',
        'cv2',          # OpenCV is not used
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GeoPlate Analyst',          # .exe file name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                            # Compress with UPX (reduce file size)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,                       # False = no black terminal window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='assets/icon.ico',            # Uncomment if there is an .ico icon file
)
