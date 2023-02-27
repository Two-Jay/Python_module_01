import unittest
from vector import Vector

class test(unittest.TestCase):
    def test(self):
        pass

class test_subject_cases(unittest.TestCase):
    def test_declare_00(self):
        test_input = [[1.,2.,3.],]
        vector = Vector(test_input)
        self.assertEqual(vector.get_elem(), test_input)

    def test_declare_01(self):
        test_input = [[1.,], [2.,], [3.,]]
        vector = Vector(test_input)
        self.assertEqual(vector.get_elem(), test_input)

    def test_declare_00(self):
        test_input = [[1.,2.,3.],]
        vector = Vector(test_input)
        self.assertEqual(vector, test_input)

    def test_declare_01(self):
        test_input = [[1.,], [2.,], [3.,]]
        vector = Vector(test_input)
        self.assertEqual(vector, test_input)


if __name__ == '__main__':
    unittest.main()