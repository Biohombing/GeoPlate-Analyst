# 🌏 GeoPlate Analyst v1.0.0

An open-source desktop application for computing and visualizing tectonic plate velocities using Euler pole kinematics, with a focus on the Sundaland region. GeoPlate Analyst integrates the official ITRF2020 Plate Motion Model with regional Sundaland Euler pole estimates and supports comparison between Euler-pole-predicted and GNSS-observed velocities.

---
## Overview

GeoPlate Analyst is a Python-based desktop application designed for tectonic plate motion analysis using Euler pole kinematics. The software provides a graphical interface for entering or importing observation coordinates, selecting or defining Euler pole parameters, computing predicted horizontal velocities, visualizing velocity vectors, and comparing predicted velocities with GNSS observations.

The application provides both the official ITRF2020 Plate Motion Model and regional Euler pole estimates for the Sundaland region, while also allowing users to enter custom Euler pole parameters for research applications.

## 🚀 How to Run

### 1. Install dependencies

## Requirements

- Python 3.x
- Operating system: Windows / Linux / macOS
- Dependencies listed in `requirements.txt`

```bash
pip install -r requirements.txt
```

### 2. Run the application

```bash
python main.py
```

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📍 Manual Input | Form dialog with automatic validation |
| 📊 Load Excel / CSV | Auto-detects lat/lon columns |
| 🗺 Shapefile Input | Supports Point, Polygon, and LineString geometries |
| 🏙 Default Data | 8 Sundaland cities ready to use out of the box |
| ▶ Compute Velocity | Worker thread — UI doesn't freeze |
| 🗺 Cartopy Map | Mercator projection, plate boundaries, velocity vectors |
| 📍 Click on Map | Add points directly by clicking on the map |
| 📋 Results Table | vN, vE, V Total, Azimuth, Direction (16-point compass) |
| 🧭 Rose Diagram | Visualizes the direction of motion for all points |
| 💾 Export Excel | Includes an Euler Pole metadata sheet |
| 📄 Export CSV | Flat format, ready for further processing |
| 🖼 Save Map | High-resolution PNG (200 dpi) |
| 💾 Save Project | JSON format (.smp), restores the session |
| 🌐 Euler Pole Models | ITRF2020, regional Sundaland estimates, and manual parameters |

---

## 🗂 Project Structure


```text
GeoPlate-Analyst/
├── main.py
├── requirements.txt
├── sundaland.spec
├── BUILD.bat
├── build.sh
├── CARA_BUILD.md
│
├── assets/
│   ├── compass_rose.png
│   ├── create_sample_excel.py
│   └── offline_map.json
│
├── core/
│   ├── constants.py
│   ├── euler_engine.py
│   ├── comparator.py
│   └── location_db.py
│
├── models/
│   └── data_models.py
│
├── services/
│   ├── calculation_worker.py
│   ├── gps_service.py
│   ├── input_service.py
│   ├── location_search.py
│   ├── pdf_exporter.py
│   └── search_worker.py
│
├── ui/
│   ├── main_window.py
│   ├── input_panel.py
│   ├── result_panel.py
│   ├── result_window.py
│   ├── gps_panel.py
│   ├── dialogs.py
│   └── ...
│
└── visualization/
    └── map_canvas.py
```

---

## 📐 Architecture

```
Euler Pole Parameters
        ↓
Geographic Coordinates
        ↓
ECEF Transformation
        ↓
Angular Velocity × Position
        ↓
Origin Rate Bias Correction
        ↓
ENU Velocity Components
        ↓
PlateVelocity
        ↓
 ┌─────────────────┬──────────────────┐
 │ Result Table    │ Map Visualization │
 │ + Rose Diagram  │ + Velocity Vector │
 └─────────────────┴──────────────────┘
        ↓
Excel / CSV / PNG / PDF / .smp
```

---

## 📋 Input File Format

### CSV / Excel
Must have the following columns (names are not case-sensitive):

| Latitude Column | Longitude Column | Name Column (optional) |
|---|---|---|
| `lat` / `latitude` / `lintang` | `lon` / `longitude` / `bujur` | `name` / `nama` / `lokasi` |

### Shapefile
The following Shapefile geometry types are supported:
- **Point** → coordinates used directly
- **Polygon** → centroid
- **LineString** → midpoint

For Shapefile input, the source coordinate reference system is automatically transformed to WGS84 (EPSG:4326) when required.

### Coordinate Reference System

Input coordinates are interpreted as geographic coordinates in WGS84 (EPSG:4326).

## Building the Standalone Application

GeoPlate Analyst can be packaged as a standalone executable using PyInstaller.

See [CARA_BUILD.md](CARA_BUILD.md) for detailed build instructions.

The repository includes:

- `sundaland.spec` — PyInstaller specification
- `BUILD.bat` — Windows build script
- `build.sh` — Unix-like build script


## Citation

If you use GeoPlate Analyst in academic research, please cite the associated software publication when available.


## License

GeoPlate Analyst is released under the MIT License.

See the [LICENSE](LICENSE) file for the full license text.


## 📚 References


- Simons, W. J. F., et al. (2007). A decade of GPS in Southeast Asia: Systematic analysis of GPS data and its implications for plate motions. *Journal of Geophysical Research: Solid Earth*, 112, B06401.
- Bird, P. (2003). An updated digital model of plate boundaries. *Geochemistry, Geophysics, Geosystems*, 4(3), 1027.
- Altamimi, Z., Rebischung, P., Métivier, L., & Collilieux, X. (2023). ITRF2020: A new release of the International Terrestrial Reference Frame modeling Earth’s dynamic evolution. *Journal of Geophysical Research: Solid Earth*.
---
