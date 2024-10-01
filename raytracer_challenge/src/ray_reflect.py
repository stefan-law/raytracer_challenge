from __future__ import annotations

from ..src import ray_shapes as rs
from ..src import ray_functions as rf
from ..src import ray_ds as rd

class PointLight:
    """Represents a point light"""
    
    def __init__(self, position: rf.point, intensity: rf.color) -> None:
        self.intensity = intensity
        self.position = position

class Material: 
    """Represents a material"""
    
    def __init__(self) -> None:
        self.color = rf.color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
    
    def __eq__(self, value: Material) -> bool:
        if self.color != value.color:
            return False
        elif self.ambient != value.ambient:
            return False
        elif self.diffuse != value.diffuse:
            return False
        elif self.specular != value.specular:
            return False
        elif self.shininess != value.shininess:
            return False
        
        return True
            
    
def normal_at(s: rs.Sphere, world_point: rf.point):
    """Return the normal vector at point p on Sphere s"""
    # Return object to origin
    object_point = s.transform.inverse() * world_point
    # Calculate normal at origin
    object_normal = object_point - rf.point(0,0,0)
    # Translate normal to world space
    world_normal = s.transform.inverse().transpose() * object_normal
    # Do below, otherwise would need to mult by 3x3 submatrix of transform
    world_normal.w = 0
    return world_normal.normal()

def reflect(v: rf.vector, n: rf.vector):
    """Reflect a vector v around a normal vector n"""
    return v - n * 2 * (v.dot(n))

def lighting(material: Material, light: PointLight, point: rf.point, eyev: rf.vector, normalv: rf.vector) -> rd.ColorTuple:
    """Calculates lighting intensity using Phong Reflection Model"""
    # combine the surface color with the light's color/intensity
    effective_color = material.color * light.intensity
    
    # find the direction to the light source
    lightv = (light.position - point).normal()
    
    # compute the ambient contribution
    ambient = effective_color * material.ambient
    
    # light_dot_normal represents cos theta between light vector and 
    # normal vector. A negative number means the light is on the other
    # side of the surface
    light_dot_normal = lightv.dot(normalv)
    
    if light_dot_normal < 0:
        diffuse = rf.color(0, 0, 0)
        specular = rf.color(0, 0, 0)
    else:
        #compute the diffuse contribution
        diffuse = effective_color * material.diffuse * light_dot_normal
        
        #reflect_dot_eye represents cos theta between reflection vector
        # and the eye vector. A negative number means the light reflects 
        # away from the eye
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = reflectv.dot(eyev)
        
        if reflect_dot_eye <= 0:
            specular = rf.color(0,  0,0)
        else:
            # compute the specular contribution
            factor = reflect_dot_eye ** material.shininess
            specular = light.intensity * material.specular * factor
            
    
    # Add the three contributions together to get the final shading
    total = ambient + diffuse + specular
    return total