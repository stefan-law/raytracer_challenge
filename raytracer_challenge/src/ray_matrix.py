"""TODO"""

from __future__ import annotations #Allows self-referenced type hinting in class methods

from . import ray_functions as rf
from . import ray_ds as rd


class Matrix:
    """TODO"""
    def __init__(self, m: int, n: int) -> None:
        self.matrix = [[0.0 for _ in range(n)]for _ in range(m)]
        self.m = m
        self.n = n

    def __getitem__(self, pos: tuple[int, int]) -> float:
        m, n = pos
        return float(self.matrix[m][n])

    def __setitem__(self, pos: tuple[int, int], value: float):
        m, n = pos
        self.matrix[m][n] = float(value)
    
    def __eq__(self, matrix) -> bool:
        """TODO"""
        # Check for equal shape
        if self.m != matrix.m or self.n != matrix.n:
            return False
        
        # Check for matching contents
        for m in range(self.m):
            for n in range(self.n):
                if not rf.float_equal(self[m,n], matrix[m,n]):
                    return False
        
        return True
    
    def __mul__(self, matrix_b: Matrix | rd.RayTuple) -> Matrix:
        """TODO"""
        if isinstance(matrix_b, Matrix):
            out_matrix = Matrix(self.m, matrix_b.n)
        
            # Each cell of the output is the dot product of the index row in A And the index column in B
            for i in range(matrix_b.n):
                for j in range(self.m):
                    out_matrix[j,i] = sum([self.matrix[j][n] * matrix_b[n,i] for n in range(self.n)])
                
            return out_matrix
        
        # Handle when a vector is passed
        temp_matrix = Matrix(4,1)
        temp_matrix[0,0] = matrix_b.x
        temp_matrix[1,0] = matrix_b.y
        temp_matrix[2,0] = matrix_b.z
        temp_matrix[3,0] = matrix_b.w
        
        temp_matrix = self * temp_matrix
        out_matrix = rd.RayTuple(temp_matrix[0,0], temp_matrix[1,0], temp_matrix[2,0], temp_matrix[3,0])
        
        return out_matrix
    
    def transpose(self) -> Matrix:
        """Perform transpose function on the matrix"""
        out_matrix = Matrix(self.m, self.n)
        for m in range(self.m):
            for n in range(self.n):
                out_matrix[n,m] = self.matrix[m][n]
        
        return out_matrix


