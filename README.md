# 🌏 GeoPlate Analyst — v1.0.0

Professional desktop application for calculating **Sundaland plate motion** based on Euler Pole kinematics (Simons et al., 2007).

---

## 🚀 How to Run

### 1. Install dependencies

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
| 🗺 Load Shapefile | Extracts coordinates from Point/Polygon/Line |
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
| 🌐 Euler Pole | Parameters can be changed from the GUI |

---

## 🗂 Project Structure

```
GeoPlate_Analyst/
├── main.py                  ← Entry point
├── requirements.txt
├── core/
│   ├── constants.py         ← Euler Pole, physical constants
│   └── euler_engine.py      ← Pure math: v = ω × r
├── models/
│   └── data_models.py       ← @dataclass: ObservationPoint, PlateVelocity, …
├── services/
│   ├── input_service.py     ← Load CSV/Excel/SHP, export, save/load project
│   └── calculation_worker.py← QThread worker
├── visualization/
│   └── map_canvas.py        ← Cartopy + Matplotlib embedded in Qt
├── ui/
│   ├── main_window.py       ← Main window, orchestrates all panels
│   ├── input_panel.py       ← Input table + action buttons
│   ├── result_panel.py      ← Results table + Rose Diagram
│   ├── dialogs.py           ← AddPoint, EulerPole, About dialogs
│   └── style.qss            ← Dark scientific stylesheet
└── assets/
    └── create_sample_excel.py
```

---

## 📐 Architecture

```
Multi Input System  (CSV / Excel / SHP / Manual / Map Click)
        ↓
  ObservationPoint  (@dataclass)
        ↓
  CalculationWorker (QThread)  ←── Doesn't block the UI
        ↓
  PlateVelocity     (@dataclass)  ←── v = ω × r
        ↓
  ┌──────────────┬──────────────┐
  │  ResultPanel  │  MapCanvas   │
  │  (Table+Rose) │  (Cartopy)   │
  └──────────────┴──────────────┘
        ↓
  Export: Excel / CSV / PNG / .smp
```

---

## 📚 References

- Simons et al. (2007) *J. Geophys. Res.* 112, B12402
- Bird P. (2003) *Geochem. Geophys. Geosyst.* 4(3):1027

---

## 📋 Input File Format

### CSV / Excel
Must have the following columns (names are not case-sensitive):

| Latitude Column | Longitude Column | Name Column (optional) |
|---|---|---|
| `lat` / `latitude` / `lintang` | `lon` / `longitude` / `bujur` | `name` / `nama` / `lokasi` |

### Shapefile
All geometry types are supported:
- **Point** → coordinates used directly
- **Polygon** → centroid
- **LineString** → midpoint

CRS is automatically converted to WGS84 (EPSG:4326).
