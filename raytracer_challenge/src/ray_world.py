"""TODO"""
from __future__ import annotations

import sys
sys.path.append('raytracer_challenge')

from imports import *

class World:
    """Creates a world object in which to contain objects and light source"""
    def __init__(self) -> None:
        self.objects = []
        self.light = None
        
    def default_world(self) -> None:
        "Creates default world with a light source and 2 spheres"
        self.light = PointLight(point(-10,10,-10), color(1,1,1))
        
        s1 = Sphere()
        s1.material.color = color(0.8, 1.0, 0.6)
        s1.material.diffuse = 0.7
        s1.material.specular = 0.2
        
        s2 = Sphere()
        s2.set_transform(scale(0.5,0.5,0.5))
        
        self.objects = [s1, s2]
        
class Camera:
    """
    Creates a camera
    
    params
    -hsize = horizontal size (in pixels) of the canvas
    -vsize = vertical size
    -field_of_view = angle 
    -transform = world orientation matrix
    """
    
    def __init__(self, hsize: int, vsize: int, field_of_view: float, transform: Matrix = identity()) -> None:
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = transform
        self.half_view = math.tan(self.field_of_view / 2)
        self.aspect = self.hsize / self.vsize
        if self.aspect >= 1:
            self.half_width = self.half_view
            self.half_height = self.half_view / self.aspect
        else:
            self.half_width = self.half_view * self.aspect
            self.half_height = self.half_view
        self.pixel_size = (self.half_width * 2) / self.hsize   

def intersect_world(world: World, ray: Ray) -> list[Intersection]:
    """Returns Intersection of ray an Objects in World"""
    intersects = []
    
    for object in world.objects:
        intersects += intersect(object, ray)
    
    intersects.sort()    
    
    return intersects

class Comps:
    """
    Creates an object containing
    -t: intersection.t
    -object: intersection.object
    -point: (in world space) where intersection occurs
    -eyev: eye vector (pointing back to eye or camera)
    -normalv: normal vector
    -inside: bool whether eye/camera is inside of shape
    """
    def __init__(self, intersection: Intersection, ray: Ray):
        """"""

        self.t = intersection.t
        self.object = intersection.item
        self.point = ray.position(intersection.t)
        self.eyev = -ray.direction
        self.normalv = normal_at(self.object, self.point)
        self.inside = False
    
        #Test for ray originating inside shape
        if self.normalv.dot(self.eyev) < 0:
            self.inside = True
            self.normalv *= -1

def shade_hit(world: World, comps: Comps) -> ColorTuple:
    """Returns shading at hit"""
    return lighting(comps.object.material, world.light,
                    comps.point, comps.eyev, comps.normalv)    
    
def color_at(world: World, ray: Ray) -> ColorTuple:
    """Returns color at intersection of world and ray"""
    # Find intersections of ray with world
    intersects = intersect_world(world, ray)
    # Determine the hit
    xs = hit(intersects)
    # If no hit, color will be black
    if xs is None:
        return color(0,0,0)
    # Prepare computations
    c = Comps(xs, ray)
    # Determine shading
    return shade_hit(world, c)

def view_transform(origin: point, to: point, up: vector) -> Matrix:
    """Returns a transform using given points and up vector"""
    # Compute forward vector and normalize it
    forward = (to - origin).normal()
    # Compute left vector by cross product of forward
    # and normalized up vector
    upn = up.normal()
    left = forward.cross(upn)
    # Compute true up vector by cross of left
    # and forward
    true_up = left.cross(forward)
    
    # Create an orientation matrix
    view_matrix = Matrix(4, 4)
    view_matrix[0, 0] = left.x
    view_matrix[0, 1] = left.y
    view_matrix[0, 2] = left.z
    view_matrix[0, 3] = 0
    view_matrix[1, 0] = true_up.x
    view_matrix[1, 1] = true_up.y
    view_matrix[1, 2] = true_up.z
    view_matrix[1, 3] = 0
    view_matrix[2, 0 ] = -forward.x
    view_matrix[2, 1] = -forward.y
    view_matrix[2, 2] = -forward.z
    view_matrix[2, 3] = 0
    view_matrix[3, 0] = 0
    view_matrix[3, 1] = 0
    view_matrix[3, 2] = 0
    view_matrix[3, 3] = 1
    
    # Append a translation to the transform
    # by multiplying view_matrix(orientation)
    # by translation(-origin)
    
    return view_matrix * translation(-origin.x, -origin.y, -origin.z)

def ray_for_pixel(c: Camera, x: float, y: float) -> Ray:
    """
    Create a ray originating from camera and intersecting canvas
    at (x, y)

    Args:
        c (Camera): A Camera object
        x (float): x-coordinate of canvas
        y (float): y-coordinate of canvas

    Returns:
        Ray: A ray that starts at the camera and pass through
        canvas pixel at (x, y)
    """
    
    # Calculate offset from the edge of the canvas to the pixel's center
    xoffset = (x + 0.5) * c.pixel_size
    yoffset = (y + 0.5) * c.pixel_size
    
    # untransformed coordinates of the pixel in world space
    # Camera looks toward -Z, so +x is to the left
    world_x = c.half_width - xoffset
    world_y = c.half_height - yoffset
    
    # Using the camera matrix, transform the canvas point and the origin,
    # and then compute the ray's direction vector. 
    # (remember that the canvas is at z=-1)
    pixel = c.transform.inverse() * point(world_x, world_y, -1)
    origin = c.transform.inverse() * point(0, 0 , 0)
    direction = (pixel - origin).normal()
    
    return Ray(origin, direction)

def render(camera: Camera, world: World) -> Canvas:
    """Renders a canvas using the provided world and camera objects

    Args:
        camera (Camera): A Camera Object
        world (World): A world Object

    Returns:
        Canvas
    """
    image = Canvas(camera.hsize, camera.vsize)
    
    for y in range(camera.vsize - 1):
        for x in range(camera.hsize - 1):
            ray = ray_for_pixel(camera, x, y)
            color = color_at(world, ray)
            write_pixel(image.canvas, x, y, color)
            
    return image
