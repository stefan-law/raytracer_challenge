"""TODO"""

from __future__ import annotations

import math
import pytest

import src.ray_functions as rf
import src.ray_ds as ray_ds
import src.ray_transformations as rt
import src.ray_matrix as rm
import src.ray_reflect as rr

class Shape:
    """
    Parent class for describing different shapes.

    Returns:
        Shape Object
    """
    def __init__(self):
        self.transform = rt.identity()
        self.material = rr.Material()
        self.saved_ray = None
        
    def local_intersect(self, ray: Ray):
        """

        Args:
            ray (Ray): _description_

        Returns:
            _type_: _description_
        """
        self.saved_ray = ray
        
    def local_normal_at(self, p: rf.point) -> rf.vector:
        """
        

        Returns:
            _type_: _description_
        """
        return rf.vector(p.x, p.y, p.z)
        

class Ray:
    """Object representing a ray"""
    def __init__(self, origin: ray_ds.RayTuple, direction: ray_ds.RayTuple) -> None:
        self.origin = origin
        self.direction = direction
        
    def position(self, t: float) -> ray_ds.RayTuple:
        """Calculate and return position at time t"""
        pos = (self.direction * t) + self.origin
        
        return pos
    
class Sphere(Shape):
    """Object representing a sphere"""
    def __init__(self) -> None:
        self.origin = rf.point(0,0,0)
        self.radius = 1.0
        super().__init__()

        
    def set_transform(self, transform: rm.Matrix) -> None:
        """Sets Sphere transform matrix"""
        self.transform = transform
        
    def __eq__(self, sphere: Sphere) -> bool:
        if not isinstance(sphere, Sphere):
            return False
        if (self.origin == sphere.origin and
                self.radius == sphere.radius and
                self.transform == sphere.transform and
                self.material == sphere.material):
            return True

        return False
    
    def local_intersect(self, ray: Ray):
        """Returns a list of t-values for intersections between sphere and ray"""
        # We transform the ray by the inverse of the sphere's transformation matrix
        # This allows us to maintain the sphere at origin for calculations
        ray2 = transform(ray, self.transform.inverse())
        
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
        
        return [Intersection(t1, self), Intersection(t2, self)]
    
    def local_normal_at(self, local_point: rf.point):
        """Return the normal vector at point p on Sphere s"""

        # Calculate normal at origin
        local_normal = local_point - rf.point(0,0,0)
    
        return local_normal
        
class Intersection:
    """Object representing intersection between ray and object"""
    def __init__(self, t: float, item: object) -> None:
        self.t = t
        self.item = item
        
    def __lt__(self, b: Intersection) -> bool:
        if self.t < b.t:
            return True
        
        return False
    
class Plane(Shape):
    """
    Object representing a Plane Shape
    """
    def __init__(self):
        super().__init__()
        
    def local_intersect(self, ray: Ray):
        # Check for a parallel ray
        if abs(ray.direction.y) < rf.EPSILON:
            return None
        # Calculate intersection of Ray with Plane
        t = -(ray.origin.y)/ray.direction.y
        return [Intersection(t, self)]
    
    def local_normal_at(self, local_point: rf.point) -> rf.vector:
        return rf.vector(0,1,0)

        
def intersect(shape: Shape, ray: Ray):
    """
    

    Args:
        shape (Shape): _description_
        ray (Ray): _description_
    """
    local_ray = transform(ray, shape.transform.inverse())
    return shape.local_intersect(local_ray)

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

def set_transform(shape: Shape, transform: rm.Matrix):
    """Set shape's transformation matrix"""
    shape.transform = transform

@pytest.mark.skip(reason="not a test")    
def test_shape():
    """Creates a test shape"""
    return Shape()
    
    
    
    
       