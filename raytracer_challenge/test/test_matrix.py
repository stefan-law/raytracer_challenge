"""TODO"""
from ..src import ray_matrix

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
