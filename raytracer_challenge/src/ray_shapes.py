"""TODO"""
import math

from ..src import ray_functions as rf
from ..src import ray_canvas
from ..src import ray_ds
from ..src import ray_transformations as rt

class Ray:
    """Object representing a ray"""
    def __init__(self, origin: ray_ds.RayTuple, direction: ray_ds.RayTuple) -> None:
        self.origin = origin
        self.direction = direction
        
    def position(self, t: float) -> ray_ds.RayTuple:
        """Calculate and return position at time t"""
        pos = (self.direction * t) + self.origin
        
        return pos
    
class Sphere:
    """Object representing a sphere"""
    def __init__(self) -> None:
        self.origin = rf.point(0,0,0)
        self.radius = 1.0
        
class Intersection:
    """Object representing intersection between ray and object"""
    def __init__(self, t: float, item: object) -> None:
        self.t = t
        self.item = item
        

def intersect(sphere: Sphere, ray: Ray):
    """Returns a list of t-values for intersections between sphere and ray"""
    #Calculate the vector between ray origin and sphere origin
    sphere_to_ray = ray.origin - rf.point(0,0,0)
    
    #Calculate dot product of ray direction
    # equivalent to it's magnitude^2
    a = ray.direction.dot(ray.direction)
    
    #Calculate 2 * dot(ray.direction, sphere_to_ray)
    # This is 2* projection of ray.direction on sphere_to_ray
    b = ray.direction.dot(sphere_to_ray) * 2
    
    #Calculate |sphere_to_ray|^2 - 1
    c = sphere_to_ray.dot(sphere_to_ray) - 1
    
    #Determine discriminant of the quadratic function
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return []
    # If discriminant is zero, there is one solution, else 2
    t1 = (-b - math.sqrt(discriminant)) / (2*a)
    t2 = (-b + math.sqrt(discriminant)) / (2*a)
    
    return [t1,t2]