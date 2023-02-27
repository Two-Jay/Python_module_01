from abc import ABC


# 정의할 exception
# ZeroDivisionError : division by zero
# NotImplementedError : Division of a scalar by a Vector is NOT defined here
# 

class Vector:
    def __init__(self, elems : list):
        self.values = elems
        self.shape = (len(elems), len(elems[0]))
        
    def get_elem(self) -> list:
        return self.values

    def get_dimention(self) -> tuple:
        return self.shape

    def T(self) -> 'Vector':
        return self

    def __repr__(self):
        return self.values

    def __str__(self) -> str:
        return str(self.values)