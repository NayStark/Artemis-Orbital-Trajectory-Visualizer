import numpy as np
import pyvista as pv
import trimesh
import os
import pandas as pd
from data_io import load_trajectory
from render_config import *
from gnc import get_kinematic_transform

# Artemis Trajectory
df_artemis = load_trajectory("data/artemis.csv")
df_artemis[["x", "y", "z"]] *= 1000.0
r = df_artemis[["x", "y", "z"]].values
v = df_artemis[["vx", "vy", "vz"]].values

# Moon Trajectory
df_moon = load_trajectory("data/moon.csv") 
df_moon[["x", "y", "z"]] *= 1000.0 # KM to M
moon_r = df_moon[["x", "y", "z"]].values


pv.set_plot_theme("dark")
plotter = pv.Plotter(lighting="none")
plotter.set_background("black")

sun = pv.Light(position=(1e8, 1e8, 1e8), focal_point=(0, 0, 0), color="white")
plotter.add_light(sun)

earth = pv.Sphere(radius=6371000 * VIS_SCALE)
plotter.add_mesh(earth, color="royalblue", lighting=True)

if not os.path.exists('models/orion_clean.obj'):
    mesh = trimesh.load('models/orion.obj')
    mesh.export('models/orion_clean.obj')
orion = pv.read("models/orion_clean.obj")
orion_actor = plotter.add_mesh(orion, color="silver", lighting=True)

moon_poly = pv.Sphere(radius=(1737400 * VIS_SCALE))
moon_actor = plotter.add_mesh(moon_poly, color="lightgrey", lighting=True)


moon_line = pv.lines_from_points(moon_r * VIS_SCALE)
plotter.add_mesh(moon_line, color="lightgray", line_width=1)

artemis_path = pv.lines_from_points(r[:1] * VIS_SCALE)
artemis_path_actor = plotter.add_mesh(artemis_path, color="yellow", line_width=2)

plotter.show(interactive_update=True)
plotter.camera.clipping_range = (0.1, 1e9)
plotter.open_gif("output/artemis_trajectory.gif", fps=30)

for i in range(len(r)):
    pos_orion = r[i] * VIS_SCALE
    orion_actor.user_matrix = get_kinematic_transform(r[i], v[i], VIS_SCALE, exaggeration=200000.0)
    
    pos_moon = moon_r[i] * VIS_SCALE
    moon_mat = np.eye(4)
    moon_mat[:3, 3] = pos_moon
    moon_actor.user_matrix = moon_mat
    
    current_path = pv.lines_from_points(r[:i+1] * VIS_SCALE)
    artemis_path_actor.mapper.dataset.copy_from(current_path)
    
    plotter.camera.focal_point = pos_orion
    cam_dist = 150.0 
    plotter.camera.position = pos_orion + np.array([cam_dist, cam_dist, cam_dist])
    plotter.camera.reset_clipping_range()
    
    plotter.update()
    plotter.write_frame()

plotter.close()