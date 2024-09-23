"""TODO"""

from ..src import ray_functions as rf
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
    assert xs[0].t == 4.0
    assert xs[1].t == 6.0
    
def test_intersect_2():
    """Compute tangent intersection of a ray and sphere"""
    r = rs.Ray(rf.point(0, 1, -5), rf.vector(0,0,1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0].t == 5
    assert xs[1].t == 5
    
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
    assert xs[0].t == -1
    assert xs[1].t == 1
    
def test_intersect_5():
    """Show a ray with sphere behind direction vector"""
    r = rs.Ray(rf.point(0, 0, 5), rf.vector(0,0,1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0].t == -6.0
    assert xs[1].t == -4.0
    
def test_Intersection():
    """Test instance of Intersection objecrt"""
    s = rs.Sphere()
    i = rs.Intersection(3.5, s)
    assert rf.float_equal(i.t, 3.5)
    assert i.item == s
    
def test_intersects():
    """Create a collection of intersections"""
    s = rs.Sphere()
    i1 = rs.Intersection(1, s)
    i2 = rs.Intersection(2, s)
    xs = rs.intersections(i1, i2)
    
    assert len(xs) == 2
    assert xs[0].t == 1
    assert xs[1].t == 2
    
def test_intersect_object():
    """Intersect sets the object on the intersection"""
    r = rs.Ray(rf.point(0,0,-5), rf.vector(0, 0, 1))
    s = rs.Sphere()
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0].item == s
    assert xs[1].item == s
    
def test_hit_1():
    """Test hit when all intersections have positive t"""
    s = rs.Sphere()
    i1 = rs.Intersection(1, s)
    i2 = rs.Intersection(2, s)
    xs = rs.intersections(i2, i1)
    i = rs.hit(xs)
    assert i == i1
    
def test_hit_2():
    """Test hit when some intersections have negative t"""
    s = rs.Sphere()
    i1 = rs.Intersection(-1, s)
    i2 = rs.Intersection(1, s)
    xs = rs.intersections(i2, i1)
    i = rs.hit(xs)
    assert i == i2
    
def test_hit_3():
    """Test hit when all intersections have negative t"""
    s = rs.Sphere()
    i1 = rs.Intersection(-2, s)
    i2 = rs.Intersection(-1, s)
    xs = rs.intersections(i2, i1)
    i = rs.hit(xs)
    assert i == None
    
def test_hit_4():
    """Test that the hit is always the lowest distance nonnegative intersection"""
    s = rs.Sphere()
    i1 = rs.Intersection(5, s)
    i2 = rs.Intersection(7, s)
    i3 = rs.Intersection(-3, s)
    i4 = rs.Intersection(2, s)
    xs = rs.intersections(i1, i2, i3, i4)
    i = rs.hit(xs)
    assert i == i4
    
def test_transform_1():
    "Translating a ray"
    r = rs.Ray(rf.point(1, 2, 3), rf.vector(0, 1, 0))
    m = rt.translation(3, 4, 5)
    r2 = rs.transform(r, m)
    assert r2.origin == rf.point(4, 6, 8)
    assert r2.direction == rf.vector(0, 1, 0)
    

def test_transform_2():
    "Scaling a ray"
    r = rs.Ray(rf.point(1, 2, 3), rf.vector(0, 1, 0))
    m = rt.scale(2, 3, 4)
    r2 = rs.transform(r, m)
    assert r2.origin == rf.point(2, 6, 12)
    assert r2.direction == rf.vector(0, 3, 0)
    
def test_transform_3():
    """Show that a sphere's default transform is identity matrix"""
    s = rs.Sphere()
    assert s.transform == rt.identity()
    
def test_transform_4():
    """Show that a sphere's transform can be updated"""
    s = rs.Sphere()
    t = rt.translation(2, 3, 4)
    s.set_transform(t)
    assert s.transform == t
    
def test_transform_and_intersect_1():
    """Intersect a scaled sphere with a ray"""
    r = rs.Ray(rf.point(0, 0, -5), rf.vector(0, 0, 1))
    s = rs.Sphere()
    s.set_transform(rt.scale(2, 2, 2))
    xs = rs.intersect(s, r)
    assert len(xs) == 2
    assert xs[0].t == 3
    assert xs[1].t == 7
    
def test_transform_and_intersect_2():
    """Intersect a translated sphere with a ray"""
    r = rs.Ray(rf.point(0, 0, -5), rf.vector(0, 0, 1))
    s = rs.Sphere()
    s.set_transform(rt.translation(5, 0, 0))
    xs = rs.intersect(s, r)
    assert len(xs) == 0
    