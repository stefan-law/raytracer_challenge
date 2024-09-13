"""TODO"""
from . import ray_functions as rf

class Matrix:
    """TODO"""
    def __init__(self, m: int, n: int) -> None:
        self.matrix = [[0.0 for i in range(n)]for i in range(m)]
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
