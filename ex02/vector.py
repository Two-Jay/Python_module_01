from abc import ABC

class Vector:
    def __init__(self, elem : list):
        if self.validate(list):
            raise
        self._elem = elem
        self._dimention = (len(elem), len(elem[0]))

    def __init__(self, vec : 'Vector'):
        self._elem = self.get_elem()
        self._dimention = self.get_dimention()
    
    def get_elem(self) -> list:
        return self._elem

    def get_dimention(self) -> tuple:
        return self._dimention

    def __repr__(self) -> list:
        return self._elem