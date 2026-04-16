# Artemis Orbital Trajectory Visualizer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![GNC](https://img.shields.io/badge/Domain-GNC%20%7C%20Astrodynamics-orange)
![Visualization](https://img.shields.io/badge/Rendering-3D%20Physics--Based-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)

A high-fidelity **Guidance, Navigation, and Control (GNC) visualization tool** for rendering and analyzing spacecraft orbital trajectories in Earth–Moon space. The project transforms ephemeris-based state vectors into physically consistent 3D motion for engineering review, mission analysis, and trajectory inspection.

---

## Mission Context

This tool supports visualization of multi-body orbital dynamics, including:

- Translunar injection and lunar flybys  
- Earth–Moon trajectory propagation  
- Spacecraft state evolution in inertial space  

It prioritizes **numerical consistency, frame fidelity, and real-time rendering performance** over purely aesthetic visualization.

---

## Preview

> ![Trajectory Animation](output/artemis_trajectory.gif)

```text
[ Artemis II Trajectory Visualization ]
Earth–Moon system with spacecraft trajectory overlay
- Real-time propagated orbit
- Scaled celestial bodies
- Orion CAD model integration
