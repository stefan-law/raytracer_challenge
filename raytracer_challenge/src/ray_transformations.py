"""TODO"""
from . import ray_matrix as rm
import math

def degree_to_rad(degree: float) -> float:
    return math.pi * (degree/180)

def translation(x: int, y: int, z: int) -> rm.Matrix:
    """Returns a translation matrix"""
    trans = rm.Matrix(4,4)
    trans[0,0] = 1
    trans[1,1] = 1
    trans[2,2] = 1
    trans[3,3] = 1
    trans[0,3] = x
    trans[1,3] = y
    trans[2,3] = z
    
    return trans

def scale(x: int, y: int, z: int) -> rm.Matrix:
    """Returns a scaling translation matrix"""
    scale_matrix = rm.Matrix(4,4)
    scale_matrix[0,0] = x
    scale_matrix[1,1] = y
    scale_matrix[2,2] = z
    scale_matrix[3,3] = 1
    
    return scale_matrix

def rotation_x(radians: float) ->rm.Matrix:
    """Returns a rotation matrix for the x-axis"""
    rot_x_matrix = rm.Matrix(4,4)
    rot_x_matrix[0,0] = 1
    rot_x_matrix[1,1] = math.cos(radians)
    rot_x_matrix[1,2] = -math.sin(radians)
    rot_x_matrix[2,1] = math.sin(radians)
    rot_x_matrix[2,2] = math.cos(radians)
    rot_x_matrix[3,3] = 1
    
    return rot_x_matrix

def rotation_y(radians: float) -> rm.Matrix:
    """Returns a rotation matrix for the y-axis"""
    rot_y_matrix = rm.Matrix(4,4)
    rot_y_matrix[0,0] = math.cos(radians)
    rot_y_matrix[0,2] = math.sin(radians)
    rot_y_matrix[1,1] = 1
    rot_y_matrix[2,0] = -math.sin(radians)
    rot_y_matrix[2,2] = math.cos(radians)
    rot_y_matrix[3,3] = 1
    
    return rot_y_matrix

def rotation_z(radians: float) -> rm.Matrix:
    """Returns a rotation matrix for the z-axis"""
    rot_z_matrix = rm.Matrix(4,4)
    rot_z_matrix[0,0] = math.cos(radians)
    rot_z_matrix[0,1] = -math.sin(radians)
    rot_z_matrix[2,2] = 1
    rot_z_matrix[1,0] = math.sin(radians)
    rot_z_matrix[1,1] = math.cos(radians)
    rot_z_matrix[3,3] = 1
    
    return rot_z_matrix

def shear(x_y: float, x_z: float, y_x: float, y_z: float, z_x: float, z_y: float) -> rm.Matrix:
    """Returns a shearing transformation matrix"""
    shear_matrix = rm.Matrix(4,4)
    shear_matrix[0,0] = 1
    shear_matrix[0,1] = x_y
    shear_matrix[0,2] = x_z
    shear_matrix[1,0] = y_x
    shear_matrix[1,1] = 1
    shear_matrix[1,2] = y_z
    shear_matrix[2,0] = z_x
    shear_matrix[2,1] = z_y
    shear_matrix[2,2] = 1
    shear_matrix[3,3] = 1
    
    return shear_matrix

def identity() -> rm.Matrix:
    """Returns an identity matrix"""
    identity_matrix = rm.Matrix(4,4)
    identity_matrix[0,0] = 1
    identity_matrix[1,1] = 1
    identity_matrix[2,2] = 1
    identity_matrix[3,3] = 1
    
    return identity_matrix