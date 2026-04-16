# Artemis Orbital Trajectory Visualizer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458)
![PyVista](https://img.shields.io/badge/PyVista-3D%20Rendering-2E8B57)
![VTK](https://img.shields.io/badge/VTK-Visualization-FF6F00)
![Astrodynamics](https://img.shields.io/badge/Domain-Orbital%20Mechanics-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

The system converts raw Earth-Centered Inertial (ECI) state vectors into synchronized 3D scene updates. The architecture focuses on consistent frame-based rendering of ephemeris-derived orbital trajectories.

## Preview

![Artemis Orbit Simulation](output/artemis_trajectory.gif)

## System Overview

This tool visualizes spacecraft motion using precomputed ephemeris state vectors, converting them into a dynamic 3D scene with consistent inertial-frame representation.

The spacecraft attitude is approximated using a **velocity-aligned (prograde) kinematic model**, providing physically intuitive orientation during orbital motion.

---

## Features

### Real-Time Trajectory Playback
Incremental rendering of spacecraft motion using ephemeris-derived state vectors, enabling smooth playback of orbital trajectories.

### Velocity-Aligned Spacecraft Orientation
Spacecraft attitude is computed by aligning its forward axis with the instantaneous velocity vector (prograde direction), providing intuitive motion visualization.

### Earth–Moon System Visualization
Scaled rendering of the Earth–Moon system provides spatial context for trajectory analysis in an inertial reference frame.

### GIF Export
Frame-by-frame export of trajectory simulations for reporting, documentation, and analysis.

### Modular Architecture
Trajectory datasets and visualization components are structured for easy swapping between different mission scenarios or ephemeris inputs.

---

## Data Sources

- **Ephemeris Data:** NASA JPL Horizons System  
  https://ssd.jpl.nasa.gov/horizons/

- **Spacecraft Geometry:** Orion CAD model from NASA 3D Resources  
  https://nasa3d.arc.nasa.gov/

---

## Technical Implementation

The visualization pipeline operates as follows:

1. Load ephemeris-derived ECI state vectors
2. Scale physical positions for visualization
3. Construct spacecraft attitude using velocity vector alignment
4. Apply SE(3) transformation per timestep
5. Render incremental trajectory updates in PyVista

---

## Core Stack

- **Visualization Engine:** PyVista (VTK-based rendering)
- **Geometry Processing:** trimesh (CAD mesh conversion)
- **Numerical Processing:** NumPy, Pandas
- **Custom Utilities:** Rigid-body transformation tools (SE(3)) and velocity-aligned kinematic attitude model

---

## Mathematical Model

The visualization represents spacecraft motion in an Earth-centered inertial (ECI) frame using ephemeris-derived state vectors.

The spacecraft orientation is defined using a velocity-aligned kinematic model, while position is taken directly from NASA JPL Horizons data.

### Velocity-aligned attitude

The spacecraft forward direction is aligned with its instantaneous velocity vector:

$$
\hat{\mathbf{v}} = \frac{\mathbf{v}}{\|\mathbf{v}\|}
$$

where:
- $\mathbf{v}$ is the inertial velocity vector
- $\hat{\mathbf{v}}$ defines the prograde (forward) direction


### Attitude construction

A body-fixed frame is constructed by aligning the spacecraft forward axis with $\hat{\mathbf{v}}$ using a standard axis-angle rotation (Rodrigues’ formula):

$$
\mathbf{R} = \mathbf{I} + \sin\theta [\mathbf{K}] + (1 - \cos\theta)[\mathbf{K}]^2
$$

where:
- $\theta$ is the angle between the reference forward axis and $\hat{\mathbf{v}}$
- $[\mathbf{K}]$ is the skew-symmetric matrix of the rotation axis

### Position and scaling (visualization only)

The spacecraft position is taken directly from ephemeris data in ECI coordinates. A uniform scaling factor is applied for visualization purposes to improve numerical display at interplanetary distances.

---

### Notes

This model is kinematic and used strictly for visualization. It preserves:
- Ephemeris-based trajectory fidelity
- Velocity-aligned spacecraft orientation
- Frame-consistent inertial rendering

It does not include spacecraft dynamics, control laws, or numerical propagation.

---

## Usage

### 1. Prepare Data

Place ephemeris files in `data/`:

- `artemis.csv`
- `moon.csv`

Format:
```text
JDTDB, x, y, z, vx, vy, vz
```

Where

- **JDTDB** = Julian Date (TDB)  
- **x, y, z** = ECI position (meters after conversion)  
- **vx, vy, vz** = ECI velocity (m/s)  

---

## 2. Run Simulation

```bash
python main.py
```

## Repository Structure
```text
Artemis-Orbital-Trajectory-Visualizer/
├── data/
│   ├── artemis.csv
│   └── moon.csv
├── models/
│   ├── orion.obj
│   └── orion_clean.obj
├── output/
│   └── artemis_trajectory.gif
├── src/
│   ├── data_io.py
│   ├── export.py
│   ├── gnc.py
│   ├── main.py
│   ├── render_config.py
│   └── viz.py
└── README.md
```
