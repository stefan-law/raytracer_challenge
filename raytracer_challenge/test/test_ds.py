"""Testing basic data structures for implementation of ray tracing"""
import math

from ..src import ray_ds
from ..src import ray_functions as rf


def test_point() -> None:
    """Tests creation of a point RayTuple"""
    t = ray_ds.RayTuple(4.3, -4.2, 3.1, 1.0)
    assert rf.float_equal(t.x, 4.3)
    assert rf.float_equal(t.y, -4.2)
    assert rf.float_equal(t.z, 3.1)
    assert rf.float_equal(t.w, 1.0)
    assert t.type == "point"
    assert t.type != "vector"

def test_vector():
    """Tests creation of a vector RayTuple"""
    t=ray_ds.RayTuple(4.3, -4.2, 3.1, 0.0)
    assert rf.float_equal(t.x, 4.3)
    assert rf.float_equal(t.y, -4.2)
    assert rf.float_equal(t.z, 3.1)
    assert rf.float_equal(t.w, 0.0)
    assert t.type == "vector"
    assert t.type != "point"

def test_point_func():
    """Tests helper function to create a point"""
    t=rf.point(4, -4, 3)
    assert t == ray_ds.RayTuple(4, -4, 3, 1.0)

def test_vector_func():
    """Tests helper function to create a vector"""
    t=rf.vector(4, -4, 3)
    assert t == ray_ds.RayTuple(4, -4, 3, 0)


def test_add():
    """Tests addition of a point and vector"""
    t1 = ray_ds.RayTuple(3, -2, 5, 1) # point
    t2 = ray_ds.RayTuple(-2, 3, 1, 0) # vector
    s = t1 + t2
    assert s == ray_ds.RayTuple(1, 1, 6, 1)

def test_sub1():
    """Tests subtraction of two points (creating a vector)"""
    point1 = rf.point(3, 2, 1) # point
    point2 = rf.point(5, 6, 7) # point
    d = point1 - point2
    assert d == rf.vector(-2, -4, -6)

def test_sub2():
    """Tests subtraction of a vector from a point (creating a point)"""
    point1 = rf.point(3, 2, 1) # point
    vector1 = rf.vector(5, 6, 7) # point
    d = point1 - vector1
    assert d == rf.point(-2, -4, -6)

def test_sub3():
    """Tests subtraction of a vector from a vector (creating a vector)"""
    vector1 = rf.vector(3, 2, 1) # point
    vector2 = rf.vector(5, 6, 7) # point
    d = vector1 - vector2
    assert d == rf.vector(-2, -4, -6)

def test_neg():
    """Tests negation of a tuple"""
    t1 = ray_ds.RayTuple(1, -2, 3, -4)
    assert -t1 == ray_ds.RayTuple(-1, 2, -3, 4)

def test_mult1():
    """Tests multiplication of tuple by a scalar"""
    t1 = ray_ds.RayTuple(1, -2, 3, -4)
    tmult = t1 * 3.5
    assert tmult == ray_ds.RayTuple(3.5, -7, 10.5, -14)

def test_mult2():
    """Tests multiplication of tuple by a fraction scalar (aka division)"""
    t1 = ray_ds.RayTuple(1, -2, 3, -4)
    tmult = t1 * 0.5
    assert tmult == ray_ds.RayTuple(0.5, -1, 1.5, -2)

def test_div():
    """Tests division of tuple by a scalar"""
    t1 = ray_ds.RayTuple(1, -2, 3, -4)
    tdiv = t1 / 2.0
    assert tdiv == ray_ds.RayTuple(0.5, -1, 1.5, -2)

def test_mag():
    """Tests calculation of magnitude of a vector"""
    v1 = rf.vector(1,0,0)
    assert v1.magnitude() == 1.0
    v2 = rf.vector(0,1,0)
    assert v2.magnitude() == 1.0
    v3 = rf.vector(0,0,1)
    assert v3.magnitude() == 1.0
    v4 = rf.vector(1,2,3)
    assert v4.magnitude() == math.sqrt(14)
    v5 = rf.vector(-1,-2,-3)
    assert v5.magnitude() == math.sqrt(14)

def test_normal():
    """Tests normalization of a vector"""
    v1 = rf.vector(4,0,0)
    assert v1.normal() == rf.vector(1,0,0)
    v2 = rf.vector(1,2,3)
    assert v2.normal() == rf.vector(0.26726, 0.53452, 0.80178)
    assert v2.normal().magnitude() == 1

def test_dot():
    """Tests dot product of two tuples"""
    v1 = rf.vector(1, 2, 3)
    v2 = rf.vector(2, 3, 4)
    assert v1.dot(v2) == 20

def test_cross():
    """Tests cross product of two vectors"""
    v1 = rf.vector(1, 2, 3)
    v2 = rf.vector(2, 3, 4)
    assert v1.cross(v2) == rf.vector(-1, 2, -1)
    assert v2.cross(v1) == rf.vector(1, -2, 1)