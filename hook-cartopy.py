# hook-cartopy.py
# PyInstaller hook to make sure all Cartopy data files are bundled
# Place this file in the same folder as sundaland.spec

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

datas = collect_data_files('cartopy', includes=['**/*'])
hiddenimports = collect_submodules('cartopy')
