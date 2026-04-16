import numpy as np

def get_kinematic_transform(pos_eci, vel_eci, vis_scale, exaggeration=1.0):
    """
    Computes a 4x4 transformation matrix to translate, scale, and rotate 
    the spacecraft to align with its velocity vector.
    
    Args:
        pos_eci (array): [x, y, z] position in meters.
        vel_eci (array): [vx, vy, vz] velocity in m/s.
        vis_scale (float): The base 1e-6 rendering scale.
        exaggeration (float): Artificial multiplier to make the ship visible.
    """

    v_norm = np.linalg.norm(vel_eci)
    if v_norm == 0:
        forward = np.array([0, 0, 1])
    else:
        forward = vel_eci / v_norm

    base_forward = np.array([0, 0, 1])

    axis = np.cross(base_forward, forward)
    axis_norm = np.linalg.norm(axis)
    
    transform = np.eye(4)
    
    if axis_norm > 1e-6:
        axis = axis / axis_norm
        angle = np.arccos(np.clip(np.dot(base_forward, forward), -1.0, 1.0))
        
        K = np.array([
            [0, -axis[2], axis[1]],
            [axis[2], 0, -axis[0]],
            [-axis[1], axis[0], 0]
        ])
        R = np.eye(3) + np.sin(angle) * K + (1 - np.cos(angle)) * (K @ K)
        transform[:3, :3] = R

    # Apply Scaling
    # A 10m spacecraft at 1e-6 scale is 0.00001 units. You won't see it. exaggeration makes it large enough to see on screen while keeping trajectory true.
    total_scale = vis_scale * exaggeration
    transform[:3, :3] *= total_scale

    # Applying Translation (scaled to visualization coordinates)
    transform[0, 3] = pos_eci[0] * vis_scale
    transform[1, 3] = pos_eci[1] * vis_scale
    transform[2, 3] = pos_eci[2] * vis_scale

    return transform