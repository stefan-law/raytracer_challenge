"""TODO"""
from __future__ import annotations

import sys
sys.path.append('raytracer_challenge')

from imports import *

def test_shadow_1():
    """Lighting with the surface in shadow"""
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0,0,-10), color(1,1,1))
    in_shadow = True
    position = point(0,0,0)
    m = Material()
    result = lighting(m, light, position, eyev, normalv, in_shadow)
    assert result == color(0.1, 0.1, 0.1)
    
def test_shadow_2():
    """
    There is no shadow when nothing is colinear with
    point and light
    """
    
    w = World()
    w.default_world()
    p = point(0, 10, 0)
    assert not is_shadowed(w, p)
    
def test_shadow_3():
    """
    There is a shadow when an object is between the 
    point and the light
    """
    
    w = World()
    w.default_world()
    p = point(10, -10, 10)
    assert is_shadowed(w, p)
    
def test_shadow_4():
    """
    There is no shadow when an object is behind the light
    """
    
    w = World()
    w.default_world()
    p = point(-20, 20, -20)
    assert not is_shadowed(w, p)
    
def test_shadow_5():
    """
    There is no shadow when an object is behind the point
    """
    
    w = World()
    w.default_world()
    p = point(-2, 2, -2)
    assert not is_shadowed(w, p)

def test_shadow_6():
    """
    shade_hit() is given an intersection in shadow
    """
    w = World()
    w.light = PointLight(point(0,0,-10), color(1,1,1))
    s1 = Sphere()
    w.objects.append(s1)
    s2 = Sphere()
    s2.transform = translation(0,0,10)
    w.objects.append(s2)
    r = Ray(point(0,0,5), vector(0,0,1))
    i = Intersection(4, s2)
    comps = Comps(i, r)
    c = shade_hit(w, comps)
    assert c == color(0.1,0.1,0.1)
    
def test_shadow_7():
    """
    The hit should offset the point
    """
    r = Ray(point(0,0,-5), vector(0,0,1))
    shape = Sphere()
    shape.transform = translation(0,0,1)
    i = Intersection(5, shape)
    comps = Comps(i, r)
    assert comps.over_point.z < -EPSILON/2
    assert comps.point.z > comps.over_point.z
    
def test_big():
    """Creates a test scene"""
    world = World()
    
    # Light source is white, shining from above and to the left
    world.light = PointLight(point(-10, 10, -10), color(1, 1, 1))
    
    # Floor: a flat sphere with a matte texture
    floor = Sphere()
    floor.transform = scale(10, 0.01, 10)
    floor.material = Material()
    floor.material.color = color(1, 0.9, 0.9)
    floor.material.specular = 0
    world.objects.append(floor)
    
    # Left Wall: same scale/color as Floor with addtl rotation/translation
    left_wall = Sphere()
    left_wall.transform = (translation(0, 0, 5) *
                           rotation_y(-math.pi/4) *
                           rotation_x(math.pi/2) *
                           scale(10, 0.01, 10))
    left_wall.material = floor.material
    world.objects.append(left_wall)
    
    # Right Wall: same as left wall, rotated opposite direction in y
    right_wall = Sphere()
    right_wall.transform = (translation(0, 0, 5) *
                           rotation_y(math.pi/4) *
                           rotation_x(math.pi/2) *
                           scale(10, 0.01, 10))
    right_wall.material = floor.material
    world.objects.append(right_wall)
    
    # Large Green Middle Sphere
    middle = Sphere()
    middle.transform = translation(-0.5, 1, 0.5)
    middle.material.color = color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    world.objects.append(middle)
    
    # Small R Green Sphere, half scale
    right = Sphere()
    right.transform = translation(1.5, 0.5, -0.5) * scale(0.5,0.5,0.5)
    right.material.color = color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    world.objects.append(right)
    
    # Small 1/3 scale sphere
    left = Sphere()
    left.transform = translation(-1.5, 0.33, -0.75) * scale(0.33, 0.33, 0.33)
    left.material.color = color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    world.objects.append(left)
    
    # Create a camera
    camera = Camera(100, 50, math.pi/3)
    camera.transform = view_transform(point(0,1.5,-5),
                                      point(0, 1, 0),
                                      vector(0, 1, 0))
    
    # Render the results to a canvas
    canvas = render(camera, world)
    canvas.canvas_to_ppm()