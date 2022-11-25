# import sys
# sys.path.insert(0, '/Users/shubh/automatic-car-parking')
import unittest
import numpy as np
from Environment import Environment


class EnvironmentTest(unittest.TestCase):
    def test_correct_rotate_car(self):
        expected_matrix = np.array([[-35, 26], [0, 44], [35, -26], [0, -44]])
        input_matrix = np.array([[40, 20], [40, -20], [-40, -20], [-40, 20]])
        output_matrix = Environment.rotate_car(self, input_matrix, 90)
        self.assertEqual(expected_matrix.tolist(), output_matrix.tolist())

    def test_incorrect_rotate_car(self):
        expected_matrix = np.array([[-35, 26], [0, 44], [35, -26], [0, -44]])
        input_matrix = np.array([[40, 60], [40, 50], [-40, 40], [-40, 30]])
        output_matrix = Environment.rotate_car(self, input_matrix, 90)
        self.assertNotEqual(expected_matrix.tolist(), output_matrix.tolist())


if __name__ == '__main__':
    unittest.main()
