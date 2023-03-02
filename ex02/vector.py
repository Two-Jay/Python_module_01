from abc import ABC


# 정의할 exception
# ZeroDivisionError : division by zero
# NotImplementedError : Division of a scalar by a Vector is NOT defined here
# 
class Vector:
	def __init__(self, elems : list):
		if not isinstance(elems, list) or not all(isinstance(i, list) for i in elems):
			raise NotImplementedError
		self.values = elems
		self.shape = (len(elems), len(elems[0]))

	def T(self):
		return Vector([[self.values[j][i] for j in range(self.shape[0])] for i in range(self.shape[1])])

	def dot(self, value : 'Vector'):
		ret = 0
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				ret = ret + (self.values[i][j] * value.values[i][j])
		return ret

	def __repr__(self):
		return f"Vector({self.values})"

	def __str__(self) -> str:
		return str(self.values)

	def __add__(self, value : 'Vector'):
		if self.shape != value.shape:
			raise NotImplementedError
		return Vector([[self.values[i][j] + value.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])])

	def __radd__(self, value : 'Vector'):
		return self.__add__(value)

	def __sub__(self, value : 'Vector'):
		if self.shape != value.shape:
			raise NotImplementedError
		return Vector([[self.values[i][j] + (value.values[i][j] * -1) for j in range(self.shape[1])] for i in range(self.shape[0])])
	
	def __rsub__(self, value : 'Vector'):
		return self.__sub__(value)

	def __mul__(self, value : int or float):
		if isinstance(value, int) == False and isinstance(value, float) == False:
			raise NotImplementedError
		param = [[self.values[i][j] * value for j in range(self.shape[1])] for i in range(self.shape[0])]
		return Vector(param)

	def __rmul__(self, value : int or float):
		return self.__mul__(value)

	def __truediv__(self, value : int or float):
		if isinstance(value, int) == False and isinstance(value, float) == False:
			raise NotImplementedError
		param = [[self.values[j][i] / value for j in range(self.shape[0])] for i in range(self.shape[1])]
		return Vector(param)
	
	def __rtruediv__(self, value : int or float):
		raise NotImplementedError