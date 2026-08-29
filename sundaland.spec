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

# Cartopy: needs its internal shapefile data (coastline, borders, etc.)
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

# Matplotlib: font and style data
datas += collect_data_files('matplotlib')

# UI stylesheet
datas += [('ui/style_light.qss', 'ui'), ('ui/style_dark.qss', 'ui')]

# Ikon compass untuk tombol rose diagram di ResultWindow
datas += [('assets/compass_rose.png', 'assets')]

# ── Hidden imports (libraries not detected automatically) ─────────────────────

hiddenimports = []

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

# Numpy & Scipy (used internally by Cartopy)
hiddenimports += [
    'numpy',
    'numpy.core._multiarray_umath',
    'scipy',
    'scipy.special',
    'scipy.spatial',
]

# Shapely (used by Cartopy)
hiddenimports += collect_submodules('shapely')

# ── Analysis ────────────────────────────────────────────────────────────────────

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
        # Exclude what isn't used (reduces file size)
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
        'PIL',          # Pillow not used
        'cv2',          # OpenCV not used
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
    name='GeoPlate Analyst',              # .exe file name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                             # Compress with UPX (reduces size)
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,                        # False = no black console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon='assets/icon.ico',             # Uncomment if an .ico icon file exists
)
