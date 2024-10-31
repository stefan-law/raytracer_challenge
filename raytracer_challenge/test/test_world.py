"""TODO"""

import sys
sys.path.append('raytracer_challenge')

from imports import *


def test_genesis():
    """Create an empty world"""
    w = World()
    assert w.light == None
    assert w.objects == []

def test_genesis_default():
    """Create a world and set it to default values"""
    w = World()
    w.default_world()
    light = PointLight(point(-10, 10, -10), color(1, 1, 1))

    # Define expected sphere properties
    expected_sphere1 = Sphere()
    expected_sphere1.material.color = color(0.8, 1.0, 0.6)
    expected_sphere1.material.diffuse = 0.7
    expected_sphere1.material.specular = 0.2

    expected_sphere2 = Sphere()
    expected_sphere2.set_transform(scale(0.5, 0.5, 0.5))

    # Check if spheres with expected properties exist in the world
    assert expected_sphere1 in w.objects
    assert expected_sphere2 in w.objects
    assert w.light == light
    
def test_intersect_world():
    """Intersect a world with a ray"""
    w = World()
    w.default_world()
    r = Ray(point(0,0,-5), vector(0,0,1))
    xs = intersect_world(w, r)
    assert len(xs) == 4
    assert xs[0].t == 4.0
    assert xs[1].t == 4.5
    assert xs[2].t == 5.5
    assert xs[3].t == 6.0
    
def test_comps():
    """Precomputing the state of an intersection"""
    r = Ray(point(0,0,-5), vector(0,0,1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = Comps(i, r)
    assert comps.t == i.t
    assert comps.object == i.item
    assert comps.point == point(0,0,-1)
    assert comps.eyev == vector(0,0,-1)
    assert comps.normalv == vector(0,0,-1)
    
def test_comps_outside():
    """The hit, when intersection outside"""
    r = Ray(point(0,0,-5), vector(0,0,1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = Comps(i, r)
    assert comps.inside == False
    
def test_comps_inside():
    """The hit, when an intersection occurs on the inside"""
    r = Ray(point(0,0,0), vector(0,0,1))
    shape = Sphere()
    i = Intersection(1, shape)
    comps = Comps(i, r)
    assert comps.point == point(0,0,1)  
    assert comps.eyev == vector(0,0,-1)
    assert comps.inside == True
    assert comps.normalv == vector(0,0,-1) # note inversion  
    
def test_shade_hit():
    """Shading an intersection"""
    w = World()
    w.default_world()
    r = Ray(point(0,0,-5), vector(0,0,1))
    shape = w.objects[0]
    i = Intersection(4, shape)
    comps = Comps(i, r)
    c = shade_hit(w, comps)
    print(c.red, c.green, c.blue, sep="\n")
    assert c == color(0.38066, 0.47583, 0.2855)
    
def test_shade_hit_inside():
    """Shading an intersection from inside"""
    w = World()
    w.default_world()
    w.light = PointLight(point(0,0.25,0), color(1,1,1))
    r = Ray(point(0,0,0), vector(0,0,1))
    shape = w.objects[1]
    i = Intersection(0.5, shape)
    comps = Comps(i, r)
    c = shade_hit(w, comps)
    assert c == color(0.90498, 0.90498, 0.90498)
    
def test_color_at_1():
    """The color when a ray misses should be black"""
    w = World()
    w.default_world()
    r = Ray(point(0,0,-5), vector(0,1,0))
    c = color_at(w, r)
    assert c == color(0,0,0)
    
def test_color_at_2():
    """The color when a ray hits"""
    w = World()
    w.default_world()
    r = Ray(point(0,0,-5), vector(0,0,1))
    c = color_at(w, r)
    assert c == color(0.38066, 0.47583, 0.2855)
    
def test_color_at_3():
    """The color with an intersection behind the ray"""
    w = World()
    w.default_world()
    outer = w.objects[0]
    outer.material.ambient = 1
    inner = w.objects[1]
    inner.material.ambient = 1
    r = Ray(point(0,0,0.75), vector(0,0,-1))
    c = color_at(w, r)
    assert c == inner.material.color
    
def test_default_orientation():
    """The transformation matrix for the default orientation"""
    origin = point(0,0,0)
    to = point(0,0,-1)
    up = vector(0,1,0)
    t = view_transform(origin, to, up)
    assert t == identity()
    
def test_orientation_1():
    """A view transformation looking +z direction"""
    origin = point(0,0,0)
    to = point(0,0,1)
    up = vector(0,1,0)
    t = view_transform(origin, to, up)
    assert t == scale(-1,1,-1)
    
def test_orientation_2():
    """The view transformation moves the world"""
    origin = point(0,0,8)
    to = point(0,0,0)
    up = vector(0,1,0)
    t = view_transform(origin, to, up)
    assert t == translation(0,0,-8)
    
def test_orientation_3():
    """An arbitrary view transformation"""
    comp_matrix = Matrix(4, 4)
    comp_matrix[0, 0] = -0.50709
    comp_matrix[0, 1] = 0.50709
    comp_matrix[0, 2] = 0.67612
    comp_matrix[0, 3] = -2.36643
    comp_matrix[1, 0] = 0.76772
    comp_matrix[1, 1] = 0.60609
    comp_matrix[1, 2] = 0.12122
    comp_matrix[1, 3] = -2.82843
    comp_matrix[2, 0] = -0.35857
    comp_matrix[2, 1] = 0.59761
    comp_matrix[2, 2] = -0.71714
    comp_matrix[2, 3] = 0.00000
    comp_matrix[3, 0] = 0.00000
    comp_matrix[3, 1] = 0.00000
    comp_matrix[3, 2] = 0.00000
    comp_matrix[3, 3] = 1.00000
    
    origin = point(1, 3, 2)
    to = point(4, -2, 8)
    up = vector(1,1,0) 
    t = view_transform(origin, to, up)
    assert t == comp_matrix
    
def test_camera_1():
    """Constructing a camera"""
    hsize = 160
    vsize = 120
    field_of_view = math.pi/2
    c = Camera(hsize, vsize, field_of_view)
    
    assert c.hsize == 160
    assert c.vsize == 120
    assert c.field_of_view == math.pi/2
    assert c.transform == identity()

def test_camera_2():
    """Test pixel size for a wide canvas"""
    c = Camera(200, 125, math.pi/2)
    assert float_equal(c.pixel_size, 0.01)
    
def test_camera_3():
    """Test pixel size for a tall canvas"""
    c = Camera(125, 200, math.pi/2)
    assert float_equal(c.pixel_size, 0.01)

def test_camera_4():
    """
    Constructing a ray through center of canvas
    """
    c = Camera(201, 101, math.pi/2)
    r = ray_for_pixel(c, 100, 50)
    assert r.origin == point(0, 0, 0)
    assert r.direction == vector(0, 0, -1)
    
def test_camera_5():
    """
    Constructing a ray through corner of canvas
    """
    c = Camera(201, 101, math.pi/2)
    r = ray_for_pixel(c, 0, 0)
    assert r.origin == point(0, 0, 0)
    assert r.direction == vector(0.66519, 0.33259, -0.66851)
    
def test_camera_6():
    """
    Constructing a ray when the camera is transformed
    """
    c = Camera(201, 101, math.pi/2)
    c.transform = rotation_y(math.pi/4) * translation(0, -2, 5)
    r = ray_for_pixel(c, 100, 50)
    assert r.origin == point(0, 2, -5)
    assert r.direction == vector(math.sqrt(2)/2, 0, -math.sqrt(2)/2)

def test_camera_7():
    """Rendering a world with a camera
    """
    w = World()
    w.default_world()
    c = Camera(11, 11, math.pi/2)
    origin = point(0,0,-5)
    to = point(0,0,0)
    up = vector(0, 1, 0)
    c.transform = view_transform(origin, to, up)
    image = render(c, w)
    assert image.canvas[5][5] == color(0.38066, 0.47583, 0.2855)
    
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