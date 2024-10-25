"""
Data structures for implementation of a ray tracer
"""
import math

import src.ray_functions as rf


class RayTuple:
    """
    Creates a tuple for ray-tracing in 3-dimensional space
    """
    def __init__(self, x: float, y: float, z: float, w=1.0) -> None:
        """"""
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)

        self.type = "point" if w == 1.0 else "vector"

    def __repr__(self) -> str:
        return f'RayTuple({self.x},{self.y},{self.z},{self.w})'

    def __eq__(self, value: object) -> bool:
        return rf.float_equal(self.x, value.x) and rf.float_equal(self.y, value.y) and \
                rf.float_equal(self.z, value.z) and rf.float_equal(self.w, value.w)

    def __add__(self, value: object) -> object:
        new_x = self.x + value.x
        new_y = self.y + value.y
        new_z = self.z + value.z
        new_w = self.w + value.w
        return RayTuple(new_x,new_y,new_z,new_w)

    def __sub__(self, value: object) -> object:
        new_x = self.x - value.x
        new_y = self.y - value.y
        new_z = self.z - value.z
        new_w = self.w - value.w
        return RayTuple(new_x,new_y,new_z,new_w)

    def __neg__(self) -> object:
        new_x = -self.x
        new_y = -self.y
        new_z = -self.z
        new_w = -self.w
        return RayTuple(new_x,new_y,new_z,new_w)

    def __mul__(self, scalar: float) -> object:
        new_x = self.x * scalar
        new_y = self.y * scalar
        new_z = self.z * scalar
        new_w = self.w * scalar
        return RayTuple(new_x, new_y, new_z, new_w)

    def __truediv__(self, scalar: float) -> object:
        new_x = self.x / scalar
        new_y = self.y / scalar
        new_z = self.z / scalar
        new_w = self.w / scalar
        return RayTuple(new_x, new_y, new_z, new_w)

    def magnitude(self) -> float:
        """Calculates and returns magnitude of a vector"""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normal(self) -> object:
        """Calculate and returns normal/unit vector of a vector"""
        return self / self.magnitude()

    def dot(self, vector: object) -> float:
        """Calculate the dot product of two vectors"""
        return self.x*vector.x + self.y*vector.y + \
            self.z*vector.z + self.w*vector.w

    def cross(self, vector: object) -> object:
        """Calculate the cross product of two vectors"""
        new_x = self.y * vector.z - self.z * vector.y
        new_y = self.z * vector.x - self.x * vector.z
        new_z = self.x * vector.y - self.y * vector.x
        return rf.vector(new_x, new_y, new_z)

class ColorTuple:
    """
    Creates a tuple for describing color
    """
    def __init__(self, red: float, green: float, blue: float) -> None:
        """"""
        self.red = float(red)
        self.green = float(green)
        self.blue = float(blue)

    def __eq__(self, value: object) -> bool:
        return rf.float_equal(self.red, value.red) and rf.float_equal(self.green, value.green) and \
                rf.float_equal(self.blue, value.blue)


    def __add__(self, color: object) -> object:
        new_red = self.red + color.red
        new_green = self.green + color.green
        new_blue = self.blue + color.blue
        return ColorTuple(new_red, new_green, new_blue)

    def __sub__(self, color: object) -> object:
        new_red = self.red - color.red
        new_green = self.green - color.green
        new_blue = self.blue - color.blue
        return ColorTuple(new_red, new_green, new_blue)

    def __mul__(self, value) -> object:
        if isinstance(value, float) or isinstance(value, int):
            new_red = self.red * value
            new_green = self.green * value
            new_blue = self.blue * value
        else: # Calculate Hadamard product for colors
            new_red = self.red * value.red
            new_green = self.green * value.green
            new_blue = self.blue * value.blue
        return ColorTuple(new_red, new_green, new_blue)
