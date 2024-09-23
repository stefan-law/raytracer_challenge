from ..src import ray_shapes as rs
from ..src import ray_functions as rf

def normal_at(s: rs.Sphere, p: rf.point):
    """Return the normal vector at point p on Sphere s"""
    return (p - rf.point(0,0,0)).normal()