"""
Helper functions for implementation of ray tracer
"""

EPSILON = 0.00001

import src.ray_ds as ray_ds

def point(x: float, y: float, z: float):
    """Helper method to create points"""
    return ray_ds.RayTuple(x, y, z)

def vector(x:float, y: float, z: float):
    """Helper method to create vectors"""
    return ray_ds.RayTuple(x, y, z, 0.0)

def color(r: float, g: float, b: float):
    """Helper method to create colors"""
    return ray_ds.ColorTuple(r, g, b)

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

