"""TODO"""

from __future__ import annotations

import math

from ..src import ray_functions as rf
from ..src import ray_ds
from ..src import ray_transformations as rt
from ..src import ray_matrix as rm


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
        self.transform = rt.identity()
        
    def set_transform(self, transform: rm.Matrix) -> None:
        """Sets Sphere transform matrix"""
        self.transform = transform
        
class Intersection:
    """Object representing intersection between ray and object"""
    def __init__(self, t: float, item: object) -> None:
        self.t = t
        self.item = item
        
    def __lt__(self, b: Intersection) -> bool:
        if self.t < b.t:
            return True
        
        return False
        

def intersect(sphere: Sphere, ray: Ray):
    """Returns a list of t-values for intersections between sphere and ray"""
    # We transform the ray by the inverse of the sphere's transformation matrix
    # This allows us to maintain the sphere at origin for calculations
    ray2 = transform(ray, sphere.transform.inverse())
    
    # x^2 + y^2 + z^2 = R^2 describes a sphere
    #Calculate the vector between ray origin and sphere origin
    sphere_to_ray = ray2.origin - rf.point(0,0,0)
    
    #Calculate dot product of ray direction
    # equivalent to it's magnitude^2
    a = ray2.direction.dot(ray2.direction)
    
    #Calculate 2 * dot(ray.direction, sphere_to_ray)
    # This is 2* projection of ray.direction on sphere_to_ray
    b = ray2.direction.dot(sphere_to_ray) * 2
    
    #Calculate |sphere_to_ray|^2 - 1
    c = sphere_to_ray.dot(sphere_to_ray) - 1
    
    #Determine discriminant of the quadratic function
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return []
    # If discriminant is zero, there is one solution, else 2
    t1 = (-b - math.sqrt(discriminant)) / (2*a)
    t2 = (-b + math.sqrt(discriminant)) / (2*a)
    
    return [Intersection(t1, sphere), Intersection(t2, sphere)]

def intersections(*intersects: Intersection):
    """Returns a list of intersections"""
    output_list = [intersect for intersect in intersects]
        
    return output_list

def hit(intersections: list[Intersection]) -> Intersection:
    """Returns lowest nonnegative intersection"""
    positive_intersections = [intersection for intersection in intersections if intersection.t >= 0]
    
    if len(positive_intersections) == 0:
        return None
    
    return min(positive_intersections)

def transform(item: Ray, matrix:rm.Matrix):
    """Transforms a ray using a matrix"""
    transformed_origin = matrix * item.origin
    transformed_direction = matrix * item.direction
    return Ray(transformed_origin, transformed_direction) 
    
    
    
    
    
       