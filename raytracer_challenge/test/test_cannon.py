"""TODO"""
from ..src import ray_ds
from ..src import ray_functions as rf
from ..src import ray_canvas


class Projectile:
    """Creates a projectile object"""
    def __init__(self, position, velocity) -> None:
        self.position = position
        self.velocity = velocity

class Environment:
    """Creates an environment"""
    def __init__(self, gravity, wind) -> None:
        self.gravity = gravity
        self.wind = wind

def tick(environment, projectile):
    """TODO"""
    position = projectile.position + projectile.velocity
    velocity = projectile.velocity + environment.gravity + environment.wind
    return Projectile(position, velocity)

def test_projectile1():
    """Test projectile and environment objects"""
    p = Projectile(rf.point(0,1,0), rf.vector(1,1.8,0).normal() * 11.25)
    e = Environment(rf.vector(0,-0.1,0), rf.vector(-0.01,0,0))
    c = ray_canvas.Canvas(900, 550)
    red = ray_ds.ColorTuple(1,0,0)

    count = 0
    while 0 <= int(c.height - p.position.y) < c.height and 0 <= int(p.position.x) < c.width:
        count += 1
        rf.write_pixel(c.canvas, int(p.position.x), int(c.height - p.position.y), red)
        p = tick(e, p)
        

        print(f"Projectile Position: ({p.position.x}, {p.position.y}, {p.position.z})")
        print(count)

    c.canvas_to_ppm()
    assert p
