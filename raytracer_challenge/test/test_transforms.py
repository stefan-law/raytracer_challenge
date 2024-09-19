"""TODO"""
import math

from ..src import ray_matrix, ray_ds
from ..src import ray_functions as rf
from ..src import ray_transformations as rt


def test_translation_1():
    """Translate a point by multiplying it by a translation matrix"""
    transform = rt.translation(5, -3, 2)
    p = rf.point(-3,4,5)
    
    assert rf.point(2,1,7) == transform * p
    
def test_translation_2():
    """Translate a point in the opposite direction by multiplying by the inverse translation matrix"""
    transform = rt.translation(5, -3, 2)
    inv = transform.inverse()
    p = rf.point(-3,4,5)
    assert rf.point(-8, 7, 3) == inv * p
    
def test_translation_3():
    """Multiplying a vector by a tranlsation matrix should return the vector"""
    transform = rt.translation(5, -3, 2)
    v = rf.vector(-3,4,5)
    assert v == transform * v
    
def test_scaling_1():
    """Applying a scaling matrix to a point"""
    transform = rt.scale(2, 3, 4)
    p = rf.point(-4, 6 , 8)
    assert rf.point(-8, 18, 32) == transform * p
    
def test_scaling_2():
    """Applying a scaling matrix to a vector"""
    transform = rt.scale(2, 3, 4)
    v = rf.vector(-4, 6, 8)
    assert rf.vector(-8, 18, 32) == transform * v
    
def test_scaling_3():
    """Multiplying by the inverse of a scaling matrix (shrinking)"""
    transform = rt.scale(2,3,4).inverse()
    v = rf.vector(-4, 6, 8)
    assert rf.vector(-2, 2, 2) == transform * v
    
def test_scaling_4():
    """Reflection is scaling by a negative value"""
    transform = rt.scale(-1, 1, 1)
    p = rf.point(2, 3, 4)
    assert transform * p == rf.point(-2, 3, 4)
    
def test_rotation_x():
    """Rotating a point around the x axis"""
    p = rf.point(0, 1, 0)
    half_quarter = rt.rotation_x(math.pi / 4)
    full_quarter = rt.rotation_x(math.pi / 2)
    
    assert half_quarter * p == rf.point(0, (math.sqrt(2))/2, (math.sqrt(2))/2)
    assert full_quarter * p == rf.point(0, 0, 1)
    
def test_rotation_x_inv():
    """Show that inverse of an x-rotation rotates in opposite direction"""
    p = rf.point(0, 1, 0)
    half_quarter = rt.rotation_x(math.pi / 4).inverse()
    
    assert half_quarter * p == rf.point(0, (math.sqrt(2))/2, -(math.sqrt(2))/2)
    
def test_rotation_y():
    """Rotating a point around the y axis"""
    p = rf.point(0, 0, 1)
    half_quarter = rt.rotation_y(math.pi / 4)
    full_quarter = rt.rotation_y(math.pi / 2)
    
    assert half_quarter * p == rf.point((math.sqrt(2))/2, 0, (math.sqrt(2))/2)
    assert full_quarter * p == rf.point(1, 0, 0)
    
def test_rotation_z():
    """Rotating a point around the z axis"""
    p = rf.point(0, 1, 0)
    half_quarter = rt.rotation_z(math.pi / 4)
    full_quarter = rt.rotation_z(math.pi / 2)
    
    assert half_quarter * p == rf.point(-(math.sqrt(2))/2, (math.sqrt(2))/2, 0)
    assert full_quarter * p == rf.point(-1, 0, 0)