import unittest

from Environment import Environment


class EnvironmentTest(unittest.TestCase):
    # TODO complete test
    def test_correct_rotate_car(self):
        expected_matrix = [[-19, 40],[20,40], [19, -40], [-20, -40]]
        input_matrix = [[40,20], [40, -20], [-40, -20], [-40, 20]]
        output_matrix = Environment.rotate_car(input_matrix, 90)
        # self.assertEqual(EXPECTED_OUTPUT, output_MATRIX)

    # TODO complete test
    def test_incorrect_rotate_car(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
