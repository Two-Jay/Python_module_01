import unittest
from vector import Vector

def test_divide_call_00():
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = v1 / 0.0

def test_divide_call_01():
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = v1 / 0.0

def test_divide_call_02():
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    v2 = 2.0 / v1

def test_divide_call_03():
    v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
    v2 = 2.0 / v1

class test_reference(unittest.TestCase):
    def test_value_reference_00(self):
        test_asnwer = [[1.,2.,3.],]
        self.assertListEqual(Vector([[1.,2.,3.],]).values, test_asnwer)

    def test_value_reference_01(self):
        test_asnwer = [[1.,], [2.,], [3.,]]
        self.assertListEqual(Vector([[1.,], [2.,], [3.,]]).values, test_asnwer)

    def test_value_reference_02(self):
        test_answer = [[0.0], [1.0], [2.0], [3.0]]
        self.assertListEqual(Vector([[0.0], [1.0], [2.0], [3.0]]).values, test_answer)

    def test_shape_reference_00(self):
        self.assertTupleEqual(Vector([[1.,2.,3.],]).shape, (1, 3))

    def test_shape_reference_01(self):
        self.assertTupleEqual(Vector([[1.,], [2.,], [3.,]]).shape, (3, 1))
    
    def test_shape_reference_02(self):
        self.assertTupleEqual(Vector([[0.0], [1.0], [2.0], [3.0]]).shape, (4, 1))

    def test_shape_reference_03(self):
        self.assertTupleEqual(Vector([[0.0, 1.0, 2.0, 3.0]]).shape, (1, 4)) 


class test_operation(unittest.TestCase):
    def test_add_00(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = Vector([[2.0], [3.0], [4.0], [5.0]])
        v3 = v1 + v2
        self.assertListEqual(v3.values, [[2.0], [4.0], [6.0], [8.0]])

    def test_add_01(self):
        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v2 = Vector([[1.0, 5.0, 4.0, 8.0]])
        v3 = v1 + v2
        self.assertListEqual(v3.values, [[1.0, 6.0, 6.0, 11.0]])

    def test_substract_00(self):
        v1 = Vector([[6.0], [3.0], [1.0], [-4.0]])
        v2 = Vector([[2.0], [3.0], [4.0], [5.0]])
        v3 = v1 - v2
        self.assertListEqual(v3.values, [[4.0], [0.0], [-3.0], [-9.0]])

    def test_substract_01(self):
        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v2 = Vector([[1.0, 5.0, 4.0, 8.0]])
        v3 = v1 - v2
        self.assertListEqual(v3.values, [[-1.0, -4.0, 2.0, -5.0]])

    def test_multiply_00(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = v1 * 5
        self.assertListEqual(v2.values, [[0.0], [5.0], [10.0], [15.0]])

    def test_multiply_01(self):
        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v2 = v1 * 5
        self.assertListEqual(v2.values, [[0.0, 5.0, 10.0, 15.0]])

    def test_divide_exception_00(self):
        with self.assertRaises(ZeroDivisionError) : test_divide_call_00()

    def test_divide_exception_01(self):
        with self.assertRaises(ZeroDivisionError) : test_divide_call_01()

    def test_divide_exception_02(self):
        with self.assertRaises(NotImplementedError) : test_divide_call_02()

    def test_divide_exception_03(self):
        with self.assertRaises(NotImplementedError) : test_divide_call_03()

    def test_divide_00(self):
        v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
        v2 = v1 / 2.0
        self.assertListEqual(v2.values, [[0.0], [0.5], [1.0], [1.5]])

    def test_divide_01(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = v1 / 2.0
        self.assertListEqual(v2.values, [[0.0, 0.5, 1.0, 1.5]])

    def test_dot_product_00(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
        self.assertEqual(v1.dot(v2), 18.0)

    def test_dot_product_01(self):
        v3 = Vector([[1.0, 3.0]])
        v4 = Vector([[2.0, 4.0]])
        self.assertEqual(v3.dot(v4), 13.0)

class test_duck_taping(unittest.TestCase):

    def test_repr_00(self):
        test_answer = [[0.0], [1.0], [2.0], [3.0]]
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertListEqual(v1, test_answer)

    def test_repr_01(self):
        test_answer = [[0.0, 1.0, 2.0, 3.0]]
        v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        self.assertListEqual(v2, test_answer)

    def test_str_00(self):
        test_answer = str([[0.0], [1.0], [2.0], [3.0]])
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertEqual(str(v1), test_answer)

    def test_str_01(self):
        test_answer = str([[0.0, 1.0, 2.0, 3.0]])
        v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        self.assertEqual(str(v2), test_answer)

class test_T(unittest.TestCase):
    def test_T_00(self):
        v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
        self.assertTupleEqual(v1.shape, (4, 1))
        self.assertEqual(v1.T(), Vector([[0.0, 1,0, 2.0, 3.0]]))
        self.assertTupleEqual(v1.T().shape, (1, 4))

    def test_T_01(self):
        v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
        self.assertTupleEqual(v2.shape, (1, 4))
        self.assertEqual(v2.T(), Vector([[0.0], [1.0], [2.0], [3.0]]))
        self.assertTupleEqual(v2.T().shape, (4, 1))


if __name__ == '__main__':
    unittest.main()