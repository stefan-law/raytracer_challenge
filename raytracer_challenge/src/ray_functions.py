"""
Helper functions for implementation of ray tracer
"""
from . import ray_ds

def point(x: float, y: float, z: float):
    """Helper method to create points"""
    return ray_ds.RayTuple(x, y, z)

def vector(x:float, y: float, z: float):
    """Helper method to create vectors"""
    return ray_ds.RayTuple(x, y, z, 0.0)

def float_equal(a, b):
    """Helper method to compare floats"""
    epsilon = 0.00001

    if abs(a -b) < epsilon:
        return True
    else:
        return False

def write_pixel(canvas: list[list[object]], x: int, y: int, color: object) -> None:
    """Writes a pixel to provided canvas at coordinates [x][y]"""
    canvas[x][y] = color
