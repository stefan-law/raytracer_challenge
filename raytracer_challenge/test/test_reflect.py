"""TODO"""

from ..src import ray_reflect as rr
from ..src import ray_shapes as rs
from ..src import ray_functions as rf

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