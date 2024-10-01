"""TODO"""

from ..src import ray_reflect as rr
from ..src import ray_shapes as rs
from ..src import ray_functions as rf
from ..src import ray_transformations as rt

import math

def test_sphere_normal_1():
    """The normal on a sphere at a point on the x-axis"""
    s = rs.Sphere()
    n = rr.normal_at(s, rf.point(1, 0, 0))
    assert n == rf.vector(1, 0, 0)

def test_sphere_normal_2():
    """The normal on a sphere at a point on the y-axis"""
    s = rs.Sphere()
    n = rr.normal_at(s, rf.point(0, 1, 0))
    assert n == rf.vector(0, 1, 0)

def test_sphere_normal_3():
    """The normal on a sphere at a point on the z-axis"""
    s = rs.Sphere()
    n = rr.normal_at(s, rf.point(0, 0, 1))
    assert n == rf.vector(0, 0, 1)

def test_sphere_normal_4():
    """The normal on a sphere at a non-axial point"""
    s = rs.Sphere()
    n = rr.normal_at(s, rf.point(math.sqrt(3)/3, math.sqrt(3)/3, math.sqrt(3)/3))
    assert n == rf.vector(math.sqrt(3)/3, math.sqrt(3)/3, math.sqrt(3)/3)
    
def test_translated_sphere_normal_1():
    """The normal on a translated sphere"""
    s = rs.Sphere()
    s.set_transform(rt.translation(0, 1, 0))
    n = rr.normal_at(s, rf.point(0, 1.70711, -0.70711))
    assert n == rf.vector(0, 0.70711, -0.70711)
    
def test_translated_sphere_normal_2():
    """The normal on a transformed sphere"""
    s = rs.Sphere()
    m = rt.scale(1, 0.5, 1) * rt.rotation_z(math.pi/5)
    s.set_transform(m)
    n = rr.normal_at(s, rf.point(0, math.sqrt(2)/2, -math.sqrt(2)/2))
    assert n == rf.vector(0, 0.97014, -0.24254)
    
def test_reflect_1():
    """Reflecting a vector approaching at 45 degrees"""
    v = rf.vector(1, -1, 0)
    n = rf.vector(0, 1, 0)
    r = rr.reflect(v, n)
    assert r == rf.vector(1, 1, 0)
    
def test_reflect_2():
    """Reflecting a vector off of a slanted surface"""
    v = rf.vector(0, -1, 0)
    n = rf.vector(math.sqrt(2)/2, math.sqrt(2)/2, 0)
    r = rr.reflect(v, n)
    assert r == rf.vector(1, 0, 0)
    
def test_point_light():
    """A point light has a position and intensity"""
    intensity = rf.color(1, 1, 1)
    position = rf.point(0, 0, 0)
    light = rr.PointLight(position, intensity)
    assert light.position == position
    assert light.intensity == intensity

def test_material_default():
    """Show attributes of default material"""
    m = rr.Material()
    assert m.color == rf.color(1,1,1)
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200.0
    
def test_sphere_material_default():
    """A sphere has default material"""
    s = rs.Sphere()
    m = s.material
    assert m == rr.Material()
    
def test_sphere_material_assign():
    """A sphere may be assigned a material"""
    s = rs.Sphere()
    m = rr.Material()
    m.ambient = 1.0
    s.material = m
    assert s.material == m
    
def test_lighting_1():
    """Test lighting with eye between light and surface"""
    m = rr.Material()
    position = rf.point(0,0,0)
    eyev = rf.vector(0,0,-1)
    normalv = rf.vector(0,0,-1)
    light = rr.PointLight(rf.point(0,0,-10), rf.color(1,1,1))
    result = rr.lighting(m, light, position, eyev, normalv)
    assert result == rf.color(1.9,1.9,1.9)
    
def test_lighting_2():
    """Test lighting with eye between light and surface and eye offset by 45 degrees"""
    m = rr.Material()
    position = rf.point(0,0,0)
    eyev = rf.vector(0,math.sqrt(2)/2,-math.sqrt(2)/2)
    normalv = rf.vector(0,0,-1)
    light = rr.PointLight(rf.point(0,0,-10), rf.color(1,1,1))
    result = rr.lighting(m, light, position, eyev, normalv)
    assert result == rf.color(1.0,1.0,1.0)

def test_lighting_3():
    """Test lighting with eye opposite surface, light offset by 45 degrees"""
    m = rr.Material()
    position = rf.point(0,0,0)
    eyev = rf.vector(0,0,-1)
    normalv = rf.vector(0,0,-1)
    light = rr.PointLight(rf.point(0,10,-10), rf.color(1,1,1))
    result = rr.lighting(m, light, position, eyev, normalv)
    assert result == rf.color(0.7364, 0.7364, 0.7364)

def test_lighting_4():
    """Test lighting with eye in the path of the reflection vector"""
    m = rr.Material()
    position = rf.point(0,0,0)
    eyev = rf.vector(0, -math.sqrt(2)/2, -math.sqrt(2)/2)
    normalv = rf.vector(0,0,-1)
    light = rr.PointLight(rf.point(0,10,-10), rf.color(1,1,1))
    result = rr.lighting(m, light, position, eyev, normalv)
    assert result == rf.color(1.6364, 1.6364, 1.6364)
    
def test_lighting_5():
    """Lighting with light behind the surface"""
    m = rr.Material()
    position = rf.point(0,0,0)
    eyev = rf.vector(0,0,-1)
    normalv = rf.vector(0,0,-1)
    light = rr.PointLight(rf.point(0,0,10), rf.color(1,1,1))
    result = rr.lighting(m, light, position, eyev, normalv)
    assert result == rf.color(0.1, 0.1, 0.1)
    