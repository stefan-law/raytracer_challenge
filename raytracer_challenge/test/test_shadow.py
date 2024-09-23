"""TODO"""

from ..src import ray_functions as rf
from ..src import ray_transformations as rt
from ..src import ray_canvas as rc
from ..src import ray_shapes as rs

def test_sphere_projection():
    """Project the shadow from a unit sphere onto a square canvas perpendicular to z"""
    ray_origin = rf.point(0, 0, -5)
    wall_z = 10 # This means max y will be 3
    wall_size = 7.0
    
    #Create a 100 x 100 pixel canvas
    canvas_pixels = 100
    canvas = rc.Canvas(100, 100)
    color = rf.color(1, 0, 0) # red
    shape = rs.Sphere()
    shape.transform = rt.scale(0.5,1,1)
    
    # Size of a single pixel (in world space units)
    pixel_size = wall_size / canvas_pixels
    
    # Compute max/min x and y
    half = wall_size / 2
    
    #Algorithm for ray tracing to a 2d canvas perpendicular to
    # and centered on z
    # iterate through each row of pixels in the canvas
    for y in range(canvas_pixels):
        # compute world y-coordinate
        world_y = half - pixel_size * y
        # iterate through each pixel in the row
        for x in range(canvas_pixels):
            # compute world x-coordinate
            world_x = -half + pixel_size * x
            
            # describe a point with these coordinates
            position = rf.point(world_x, world_y, wall_z)
            
            r = rs.Ray(ray_origin, (position - ray_origin).normal())
            xs = rs.intersect(shape, r)
            
            if rs.hit(xs):
                rf.write_pixel(canvas.canvas, x, y, color)
                
    #Print canvas to file
    canvas.canvas_to_ppm()