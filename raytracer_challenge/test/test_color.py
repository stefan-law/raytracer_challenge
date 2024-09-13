"""Testing canvas and color functions for implementation of ray tracing"""
import math, io

from ..src import ray_ds
from ..src import ray_functions as rf
from ..src import ray_canvas

def test_color():
    "Test init of a color value"
    c = ray_ds.ColorTuple(-0.5, 0.4, 1.7)
    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7

def test_color_add():
    "Test add of color values"
    c1 = ray_ds.ColorTuple(0.9, 0.6, 0.75)
    c2 = ray_ds.ColorTuple(0.7, 0.1, 0.25)
    c_sum = c1 + c2
    assert c_sum == ray_ds.ColorTuple(1.6, 0.7, 1.0)

def test_color_sub():
    "Test sub of color values"
    c1 = ray_ds.ColorTuple(0.9, 0.6, 0.75)
    c2 = ray_ds.ColorTuple(0.7, 0.1, 0.25)
    c_sub = c1 - c2
    assert c_sub == ray_ds.ColorTuple(0.2, 0.5, 0.5)

def test_color_mult():
    "Test mult of color values"
    c = ray_ds.ColorTuple(0.2, 0.3, 0.4)
    c_mult = c * 2
    assert c_mult  == ray_ds.ColorTuple(0.4, 0.6, 0.8)
    c1 = ray_ds.ColorTuple(1, 0.2, 0.4)
    c2 = ray_ds.ColorTuple(0.9, 1, 0.1)
    assert c1 * c2 == ray_ds.ColorTuple(0.9, 0.2, 0.04)

def test_canvas_init():
    "Test proper initializtion of canvas"
    c = ray_canvas.Canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for x in range(c.width):
        for y in range(c.height):
            assert c.canvas[x][y] == ray_ds.ColorTuple(0, 0, 0)

def test_canvas_write():
    """Test writing a pixel to canvas"""
    c = ray_canvas.Canvas(10, 20)
    red = ray_ds.ColorTuple(1,0,0)
    rf.write_pixel(c.canvas, 2, 3, red)
    assert c.canvas[2][3] == ray_ds.ColorTuple(1,0,0)

def test_canvas_print_data(capsys, monkeypatch): #capsys fixture to capture IO
    monkeypatch.setattr('sys.stdin', io.StringIO('ppm_trial'))
    """Test printing all data for PPM output"""
    c = ray_canvas.Canvas(10, 2)
    c1 = ray_ds.ColorTuple(1, 0.8, 0.6)
    for y in range(c.height):
        for x in range(c.width):
            rf.write_pixel(c.canvas, x, y, c1)
    c.canvas_to_ppm()
    captured = capsys.readouterr()
    assert c
