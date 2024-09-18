"""TODO"""
from ..src import ray_matrix, ray_ds

def test_matrix_gen4by4():
    """"""
    m = ray_matrix.Matrix(4,4)
    m[0,0] = 1
    m[0,1] = 2
    m[0,2] = 3
    m[0,3] = 4
    m[1,0] = 5.5
    m[1,1] = 6.5
    m[1,2] = 7.5
    m[1,3] = 8.5
    m[2,0] = 9
    m[2,1] = 10
    m[2,2] = 11
    m[2,3] = 12
    m[3,0] = 13.5
    m[3,1] = 14.5
    m[3,2] = 15.5
    m[3,3] = 16.5

    assert m[0,0] == 1
    assert m[0,3] == 4
    assert m[1,0] == 5.5
    assert m[1,2] == 7.5
    assert m[2,2] == 11
    assert m[3,0] == 13.5
    assert m[3,2] == 15.5

def test_matrix_gen2by2():
    """"""
    m = ray_matrix.Matrix(2,2)
    m[0,0] = -3
    m[0,1] = 5
    m[1,0] = 1
    m[1,1] = -2

    assert m[0,0] == -3
    assert m[0,1] == 5
    assert m[1,0] == 1
    assert m[1,1] == -2

def test_matrix_gen3by3():
    """"""
    m= ray_matrix.Matrix(3,3)
    m[0,0] = -3
    m[0,1] = 5
    m[0,2] = 0
    m[1,0] = 1
    m[1,1] = -2
    m[1,2] = -7
    m[2,0] = 0
    m[2,1] = 1
    m[2,2] = 1

    assert m[0,0] == -3
    assert m[1,1] == -2
    assert m[2,2] == 1

def test_matrix_eq():
    a = ray_matrix.Matrix(4,4)
    a[0,0] = 1
    a[0,1] = 2
    a[0,2] = 3
    a[0,3] = 4
    a[1,0] = 5
    a[1,1] = 6
    a[1,2] = 7
    a[1,3] = 8
    a[2,0] = 9
    a[2,1] = 8
    a[2,2] = 7
    a[2,3] = 6
    a[3,0] = 5
    a[3,1] = 4
    a[3,2] = 3
    a[3,3] = 2
    b = ray_matrix.Matrix(4,4)
    b[0,0] = 1
    b[0,1] = 2
    b[0,2] = 3
    b[0,3] = 4
    b[1,0] = 5
    b[1,1] = 6
    b[1,2] = 7
    b[1,3] = 8
    b[2,0] = 9
    b[2,1] = 8
    b[2,2] = 7
    b[2,3] = 6
    b[3,0] = 5
    b[3,1] = 4
    b[3,2] = 3
    b[3,3] = 2

    assert a == b
    
def test_matrix_mul():
    """TODO"""
    # Initialize two matrices
    a = ray_matrix.Matrix(4,4)
    a[0,0] = 1
    a[0,1] = 2
    a[0,2] = 3
    a[0,3] = 4
    a[1,0] = 5
    a[1,1] = 6
    a[1,2] = 7
    a[1,3] = 8
    a[2,0] = 9
    a[2,1] = 8
    a[2,2] = 7
    a[2,3] = 6
    a[3,0] = 5
    a[3,1] = 4
    a[3,2] = 3
    a[3,3] = 2
    b = ray_matrix.Matrix(4,4)
    b[0,0] = -2
    b[0,1] = 1
    b[0,2] = 2
    b[0,3] = 3
    b[1,0] = 3
    b[1,1] = 2
    b[1,2] = 1
    b[1,3] = -1
    b[2,0] = 4
    b[2,1] = 3
    b[2,2] = 6
    b[2,3] = 5
    b[3,0] = 1
    b[3,1] = 2
    b[3,2] = 7
    b[3,3] = 8
    
    # Initialize reference matrix
    t = ray_matrix.Matrix(4,4)
    t[0,0] = 20
    t[0,1] = 22
    t[0,2] = 50
    t[0,3] = 48
    t[1,0] = 44
    t[1,1] = 54
    t[1,2] = 114
    t[1,3] = 108
    t[2,0] = 40
    t[2,1] = 58
    t[2,2] = 110
    t[2,3] = 102
    t[3,0] = 16
    t[3,1] = 26
    t[3,2] = 46
    t[3,3] = 42
    
    #Multiply AB and test equality with reference matrix
    test = a*b
    assert test == t
    
def test_matrix_vector_mul():
    """TODO"""
    # Initialize one matrix
    a = ray_matrix.Matrix(4,4)
    a[0,0] = 1
    a[0,1] = 2
    a[0,2] = 3
    a[0,3] = 4
    a[1,0] = 2
    a[1,1] = 4
    a[1,2] = 4
    a[1,3] = 2
    a[2,0] = 8
    a[2,1] = 6
    a[2,2] = 4
    a[2,3] = 1
    a[3,0] = 0
    a[3,1] = 0
    a[3,2] = 0
    a[3,3] = 1
    
    b = ray_ds.RayTuple(1, 2, 3, 1)
    
    t = ray_ds.RayTuple(18, 24, 33, 1)
    assert a * b == t
    
def test_identity_matrix():
    """Multiplying a matrix by and identity matrix returns the same matrix"""
    # Initialize one matrix
    a = ray_matrix.Matrix(4,4)
    a[0,0] = 0
    a[0,1] = 1
    a[0,2] = 2
    a[0,3] = 4
    a[1,0] = 1
    a[1,1] = 2
    a[1,2] = 4
    a[1,3] = 8
    a[2,0] = 2
    a[2,1] = 4
    a[2,2] = 8
    a[2,3] = 16
    a[3,0] = 4
    a[3,1] = 8
    a[3,2] = 16
    a[3,3] = 32
    
    # Initialize an identity matrix for 4x4 matrix
    i = ray_matrix.Matrix(4,4)
    i[0,0] = 1
    i[0,1] = 0
    i[0,2] = 0
    i[0,3] = 0
    i[1,0] = 0
    i[1,1] = 1
    i[1,2] = 0
    i[1,3] = 0
    i[2,0] = 0
    i[2,1] = 0
    i[2,2] = 1
    i[2,3] = 0
    i[3,0] = 0
    i[3,1] = 0
    i[3,2] = 0
    i[3,3] = 1
    
    assert a * i == a
    
def test_transpose():
    """Test transpose of a matrix (swapping rows and columns)"""
    # Initialize test matrix
    a = ray_matrix.Matrix(4,4)
    a[0,0] = 0
    a[0,1] = 9
    a[0,2] = 3
    a[0,3] = 0
    a[1,0] = 9
    a[1,1] = 8
    a[1,2] = 0
    a[1,3] = 8
    a[2,0] = 1
    a[2,1] = 8
    a[2,2] = 5
    a[2,3] = 3
    a[3,0] = 0
    a[3,1] = 0
    a[3,2] = 5
    a[3,3] = 8
    
    # Initialize comparison matrix
    t = ray_matrix.Matrix(4,4)
    t[0,0] = 0
    t[0,1] = 9
    t[0,2] = 1
    t[0,3] = 0
    t[1,0] = 9
    t[1,1] = 8
    t[1,2] = 8
    t[1,3] = 0
    t[2,0] = 3
    t[2,1] = 0
    t[2,2] = 5
    t[2,3] = 5
    t[3,0] = 0
    t[3,1] = 8
    t[3,2] = 3
    t[3,3] = 8
    
    assert a.transpose() == t
    
def test_determinant():
    """Test determinant function for 2x2 matrices"""
    a = ray_matrix.Matrix(2,2)
    a[0,0] = 1
    a[0,1] = 5
    a[1,0] = -3
    a[1,1] = 2
    assert a.determinant() == 17
    
def test_submatrix_1():
    """Test changing 3x3 matrix to a 2x2 by removing row 0 and column 2"""
    a = ray_matrix.Matrix(3,3)
    a[0,0] = 1
    a[0,1] = 5
    a[0,2] = 0
    a[1,0] = -3
    a[1,1] = 2
    a[1,2] = 7
    a[2,0] = 0
    a[2,1] = 6
    a[2,2] = -3
    
    t = ray_matrix.Matrix(2,2)
    t[0,0] = -3
    t[0,1] = 2
    t[1,0] = 0
    t[1,1] = 6
    
    assert a.submatrix(0, 2) == t
    
def test_submatrix_2():
    """Test changing 4x4 matrix to a 3x3 by removing row 2 and column 1"""
    a = ray_matrix.Matrix(4,4)
    a[0,0] = -6
    a[0,1] = 1
    a[0,2] = 1
    a[0,3] = 6
    a[1,0] = -8
    a[1,1] = 5
    a[1,2] = 8
    a[1,3] = 6
    a[2,0] = -1
    a[2,1] = 0
    a[2,2] = 8
    a[2,3] = 2
    a[3,0] = -7
    a[3,1] = 1
    a[3,2] = -1
    a[3,3] = 1
    
    t = ray_matrix.Matrix(3,3)
    t[0,0] = -6
    t[0,1] = 1
    t[0,2] = 6
    t[1,0] = -8
    t[1,1] = 8
    t[1,2] = 6
    t[2,0] = -7
    t[2,1] = -1
    t[2,2] = 1
    
    assert a.submatrix(2, 1) == t

def test_minor():
    """Test minor function with a 3x3 matrix"""
    a = ray_matrix.Matrix(3,3)
    a[0,0] = 3
    a[0,1] = 5
    a[0,2] = 0
    a[1,0] = 2
    a[1,1] = -1
    a[1,2] = -7
    a[2,0] = 6
    a[2,1] = -1
    a[2,2] = 5
    
    b = a.submatrix(1,0)
    
    assert b.determinant() == 25
    assert a.minor(1,0) == 25

def test_cofactor():
    """Test cofactor function  with a 3x3 matrix"""
    a = ray_matrix.Matrix(3,3)
    a[0,0] = 3
    a[0,1] = 5
    a[0,2] = 0
    a[1,0] = 2
    a[1,1] = -1
    a[1,2] = -7
    a[2,0] = 6
    a[2,1] = -1
    a[2,2] = 5
    
    assert a.minor(0,0) == -12
    assert a.cofactor(0,0) == -12
    assert a.minor(1,0) == 25
    assert a.cofactor(1,0) == -25

def test_determinant_3x3():
    """Test determinant and cofactor functions with a 3x3 matrix"""
    a = ray_matrix.Matrix(3,3)
    a[0,0] = 1
    a[0,1] = 2
    a[0,2] = 6
    a[1,0] = -5
    a[1,1] = 8
    a[1,2] = -4
    a[2,0] = 2
    a[2,1] = 6
    a[2,2] = 4
    
    assert a.cofactor(0,0) == 56
    assert a.cofactor(0,1) == 12
    assert a.cofactor(0,2) == -46
    assert a.determinant() == -196
    
def test_determinant_4x4():
    """Test determinant and cofactor functions with a 4x4 matrix"""
    a = ray_matrix.Matrix(4,4)
    a[0,0] = -2
    a[0,1] = -8
    a[0,2] = 3
    a[0,3] = 5
    a[1,0] = -3
    a[1,1] = 1
    a[1,2] = 7
    a[1,3] = 3
    a[2,0] = 1
    a[2,1] = 2
    a[2,2] = -9
    a[2,3] = 6
    a[3,0] = -6
    a[3,1] = 7
    a[3,2] = 7
    a[3,3] = -9
    
    assert a.cofactor(0,0) == 690
    assert a.cofactor(0,1) == 447
    assert a.cofactor(0,2) == 210
    assert a.cofactor(0,3) == 51
    assert a.determinant() == -4071