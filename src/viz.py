import numpy as np
import pyvista as pv
import trimesh
from render_config import *

def scale(v):
    return v * VIS_SCALE


def create_scene():
    plotter = pv.Plotter()
    plotter.set_background("black")

    # Earth
    earth = pv.Sphere(radius=EARTH_RADIUS_R)
    plotter.add_mesh(earth, color="blue", smooth_shading=True)

    return plotter


def load_orion(path):

    mesh = trimesh.load(path)

    vertices = np.array(mesh.vertices)
    faces = np.array(mesh.faces)

    vertices = vertices - vertices.mean(axis=0)

    scale = np.linalg.norm(vertices, axis=1).max()

    vertices = vertices / scale * 10.0 # Scaled to 10m size

    faces = np.hstack([np.full((len(faces),1),3), faces]).flatten()

    return pv.PolyData(vertices, faces)