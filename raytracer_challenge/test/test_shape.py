"""TODO"""
from __future__ import annotations

import sys
sys.path.append('raytracer_challenge')

from imports import *

def test_shape_1():
    """
    Test default transformation
    """
    s = test_shape()
    assert s.transform == identity()
    
def test_shape_2():
    """
    Assigning a transformation
    """
    s = test_shape()
    set_transform(s, translation(2,3,4))
    assert s.transform == translation(2,3,4)

def test_shape_3():
    """
    Test the default material
    """
    s = test_shape()
    m = s.material
    assert m == Material()
    
def test_shape_4():
    """
    Test assigning a material
    """
    s = test_shape()
    m = Material()
    m.ambient = 1
    s.material = m
    assert s.material == m
    
def test_shape_5():
    """
    Intersecting a scaled shape with a ray
    """
    r = Ray(point(0,0,-5), vector(0,0,1))
    s = test_shape()
    set_transform(s, scale(2,2,2))
    xs = intersect(s,r)
    assert s.saved_ray.origin == point(0,0,-2.5)
    assert s.saved_ray.direction == vector(0,0,0.5)
    
def test_shape_6():
    """
    Intersecting a translated shape with a ray
    """
    r = Ray(point(0,0,-5), vector(0,0,1))
    s = test_shape()
    set_transform(s, translation(5,0,0))
    xs = intersect(s,r)
    assert s.saved_ray.origin == point(-5,0,-5)
    assert s.saved_ray.direction == vector(0,0,1)

def test_shape_7():
    """
    Computing the normal on a translated shape
    """
    s = test_shape()
    set_transform(s, translation(0,1,0))
    n = normal_at(s, point(0, 1.70711, -0.70711))
    assert n == vector(0, 0.70711, -0.70711)
    
def test_shape_8():
    """
    Computing the normal on a transformed shape
    """
    s = test_shape()
    m = scale(1, 0.5, 1) * rotation_z(math.pi/5)
    set_transform(s, m)
    n = normal_at(s, point(0, math.sqrt(2)/2, -math.sqrt(2)/2))
    assert n == vector(0, 0.97014, -0.24254)

def test_shape_9():
    """
    A Sphere is a Shape
    """
    s = Sphere()
    assert isinstance(s, Shape)

def test_plane_1():
    """
    The normal of a plane is constant everywhere
    """
    p = Plane()
    n1 = p.local_normal_at(point(0,0,0))
    n2 = p.local_normal_at(point(10, 0, -10))
    n3 = p.local_normal_at(point(-5,0,150))
    
    assert n1 == vector(0,1,0)
    assert n2 == vector(0,1,0)
    assert n2 == vector(0,1,0)
    
def test_plane_2():
    """
    Intersect with a ray parallel to the plane
    """
    p = Plane()
    r = Ray(point(0,10,0), vector(0,0,1))
    xs = p.local_intersect(r)
    assert xs is None
    
def test_plane_3():
    """
    Intersect with a coplanar ray
    """
    p = Plane()
    r = Ray(point(0,0,0), vector(0,0,1))
    xs = p.local_intersect(r)
    assert xs is None
    
def test_plane_4():
    """
    A ray intersecting a plane from above
    """
    p = Plane()
    r = Ray(point(0,1,0), vector(0,-1,0))
    xs = p.local_intersect(r)
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].item == p

def test_plane_5():
    """
    A ray intersecting a plane from below
    """
    p = Plane()
    r = Ray(point(0,-1,0), vector(0,1,0))
    xs = p.local_intersect(r)
    assert len(xs) == 1
    assert xs[0].t == 1
    assert xs[0].item == p
    