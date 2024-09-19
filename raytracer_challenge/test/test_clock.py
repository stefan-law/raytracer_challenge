"""TODO"""
import math

from ..src import ray_functions as rf
from ..src import ray_canvas
from ..src import ray_ds
from ..src import ray_transformations as rt

def test_clock():
    """Demonstrate drawing the hours of a clock face using rotation matrices"""
    
    #Create a blank canvas and a point centered at origin
    c = ray_canvas.Canvas(100,100)
    p = rf.point(0, 1 ,0)
    red = ray_ds.ColorTuple(1,0,0)
    scale = 25
    
    #Rotate around z-axis
    transform = rt.rotation_z(math.pi / 6)
    
    for _ in range(12):
        rf.write_pixel(c.canvas, int(scale * p.x + 50), int(scale * p.y + 50), red)
        p = transform * p
        
    c.canvas_to_ppm()