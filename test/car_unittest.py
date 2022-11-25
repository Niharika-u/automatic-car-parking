# import sys
# sys.path.insert(0, '/Users/shubh/automatic-car-parking')
import unittest
import numpy as np

from Car import determine_empty_spot
from Car import get_parking_coordinates

from ParkingLot import ParkingLot


class car_unittest(unittest.TestCase):
    def test_correct_determine_empty_spot(self):
        pl = ParkingLot([5])
        parkingenv = pl.get_cars()
        expected_emptyspots = np.array([5])
        output_expected = determine_empty_spot(parkingenv)
        self.assertEqual(expected_emptyspots, output_expected)

    def test_incorrect_determine_empty_spot(self):
        pl = ParkingLot([6])
        parkingenv = pl.get_cars()
        expected_emptyspots = np.array([5])
        output_expected = determine_empty_spot(parkingenv)
        self.assertNotEqual(expected_emptyspots, output_expected)

    def test_correct_left_get_parking_coordinates(self):
        expected = (35, 56)
        output = get_parking_coordinates()
        self.assertEqual(expected, output)

    def test_correct_right_get_parking_coordinates(self):
        expected = (35, 56)
        output = get_parking_coordinates()
        self.assertEqual(expected, output)

    def test_incorrect_get_parking_coordinates(self):
        expected = 0
        output = get_parking_coordinates()
        self.assertNotEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
