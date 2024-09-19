"""TODO"""

from ..src import ray_functions as rf
from ..src import ray_canvas
from ..src import ray_ds
from ..src import ray_transformations as rt
from ..src import ray_shapes as rs

def test_ray():
    """"Create and query a ray"""
    origin = rf.point(1, 2, 3)
    direction = rf.vector(4, 5, 6)
    r = rs.Ray(origin, direction)
    
    assert r.origin == origin
    assert r.direction == direction
    
def test_distance_compute():
    """Computing a point from a distance"""
    r = rs.Ray(rf.point(2, 3, 4), rf.vector(1, 0 ,0))
    
    assert r.position(0) == rf.point(2, 3, 4)
    assert r.position(1) == rf.point(3,3,4)
    assert r.position(-1) == rf.point(1,3,4)
    assert r.position(2.5) == rf.point(4.5,3,4)

def test_intersect_1():
    """Compute instersection of ray and sphere along x-axis"""
    r = rs.Ray(rf.point(0,0,-5), rf.vector(0,0,1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0] == 4.0
    assert xs[1] == 6.0
    
def test_intersect_2():
    """Compute tangent intersection of a ray and sphere"""
    r = rs.Ray(rf.point(0, 1, -5), rf.vector(0,0,1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0] == 5
    assert xs[1] == 5
    
def test_intersect_3():
    """Show that a ray misses a sphere"""
    r = rs.Ray(rf.point(0, 2, -5), rf.vector(0,0,1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 0
    
def test_intersect_4():
    """Show a ray originating inside sphere"""
    r = rs.Ray(rf.point(0, 0, 0), rf.vector(0,0,1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0] == -1
    assert xs[1] == 1
    
def test_intersect_5():
    """Show a ray with sphere behind direction vector"""
    r = rs.Ray(rf.point(0, 0, 5), rf.vector(0,0,1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0] == -6.0
    assert xs[1] == -4.0
    
def test_Intersection():
    """Test instance of Intersection objecrt"""
    s = rs.Sphere
    i = rs.Intersection(3.5, s)
    assert rf.float_equal(i.t, 3.5)
    assert i.item == s