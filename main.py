"""
main.py
Entry point for GeoPlate Analyst.

Run with:
    python main.py          <- mode development
    Geoplate Analyst.exe  <- distribution mode (PyInstaller build output)

Requirements:
    pip install PyQt6, cartopy, geopandas, contextily, pandas, openpyxl, matplotlib, numpy
"""

import sys
import os

# CRITICAL: set DPI env BEFORE importing Qt
# Ensures Qt and Matplotlib use consistent pixel units on HiDPI (125/150/200%)
os.environ.setdefault('QT_ENABLE_HIGHDPI_SCALING', '1')

if getattr(sys, 'frozen', False):
    ROOT    = sys._MEIPASS
    APP_DIR = os.path.dirname(sys.executable)
else:
    ROOT    = os.path.dirname(os.path.abspath(__file__))
    APP_DIR = ROOT

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# Point Cartopy to the map data (Natural Earth) that is already bundled within
# .exe, so the application does NOT need to download anything when it is first run.
if getattr(sys, 'frozen', False):
    os.environ['CARTOPY_DATA_DIR'] = os.path.join(ROOT, 'cartopy_data')

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

from ui.main_window import MainWindow
from core.constants import APP_NAME, APP_VERSION


def load_stylesheet(app: QApplication, theme: str = 'light'):
    from ui.theme_manager import apply as apply_theme
    apply_theme(theme, app)


def main():
    # PassThrough: allow fractional DPI (1.5x etc) without rounding
    # devicePixelRatioF() in GeoCoordTransformer handles the scaling correctly
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )

    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName("GeodynamicsLab")

    # App logo/icon (title bar, taskbar when running).
    # Replace or add a file in assets/icon.ico to change the logo.
    icon_path = os.path.join(ROOT, "assets", "icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))

    # Set explicit font to avoid QFont::setPointSize warnings at HiDPI
    font = QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    app.setFont(font)
    
    # Suppress verbose Qt warnings (cosmetic only, not errors)
    os.environ.setdefault('QT_LOGGING_RULES', '*.debug=false;qt.qpa.fonts=false')

    load_stylesheet(app)

    win = MainWindow()
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()