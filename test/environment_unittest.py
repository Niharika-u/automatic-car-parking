# import sys
# sys.path.insert(0, '/Users/smitvaghela/Desktop/CS/automatic-car-parking')
import unittest
import numpy as np

from Environment import Environment
import argparse
from Car import determine_empty_spot
from Car import get_parking_coordinates
from Environment import Environment
from ParkingLot import ParkingLot
from Car import Car


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

    def test_correct_determine_empty_spot(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--x_start', type=int, default=50, help='X of start')
        parser.add_argument('--y_start', type=int, default=0, help='Y of start')
        parser.add_argument('--parking_spot', type=list, default=[5], help='empty car position in parking out of 12')
        args = parser.parse_args()

        pl = ParkingLot(args.parking_spot)

        parkingenv = pl.get_cars()
        expected_emptyspots = np.array([5])
        output_expeted = determine_empty_spot(parkingenv)
        self.assertEqual(expected_emptyspots, output_expeted)

    def test_incorrect_determine_empty_spot(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--x_start', type=int, default=50, help='X of start')
        parser.add_argument('--y_start', type=int, default=0, help='Y of start')
        parser.add_argument('--parking_spot', type=list, default=[6], help='empty car position in parking out of 12')
        args = parser.parse_args()

        pl = ParkingLot(args.parking_spot)

        parkingenv = pl.get_cars()
        expected_emptyspots = np.array([5])
        output_expeted = determine_empty_spot(parkingenv)
        self.assertNotEqual(expected_emptyspots, output_expeted)

    def test_correct_left_get_parking_coordinates(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--x_start', type=int, default=50, help='X of start')
        parser.add_argument('--y_start', type=int, default=0, help='Y of start')
        parser.add_argument('--parking_spot', type=list, default=[5], help='empty car position in parking out of 12')
        args = parser.parse_args()

        pl = ParkingLot(args.parking_spot)

        parkingenv = pl.get_cars()
        emptySpots = determine_empty_spot(parkingenv)

        cars = {1: [[45, 20]], 2: [[65, 20]],
        3: [[35, 32]], 4: [[65, 32]],
        5: [[35, 44]], 6: [[65, 44]],
        7: [[35, 56]], 8: [[65, 56]],
        9: [[35, 68]], 10: [[65, 68]],
        11: [[35, 80]], 12: [[65, 80]]}

        expected = (35,56)
        output = get_parking_coordinates()
        self.assertEqual(expected, output)

    def test_correct_right_get_parking_coordinates(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--x_start', type=int, default=50, help='X of start')
        parser.add_argument('--y_start', type=int, default=0, help='Y of start')
        parser.add_argument('--parking_spot', type=list, default=[6], help='empty car position in parking out of 12')
        args = parser.parse_args()

        pl = ParkingLot(args.parking_spot)

        parkingenv = pl.get_cars()
        emptySpots = determine_empty_spot(parkingenv)

        cars = {1: [[45, 20]], 2: [[65, 20]],
        3: [[35, 32]], 4: [[65, 32]],
        5: [[35, 44]], 6: [[65, 44]],
        7: [[35, 56]], 8: [[65, 56]],
        9: [[35, 68]], 10: [[65, 68]],
        11: [[35, 80]], 12: [[65, 80]]}

        expected = (35,56)
        output = get_parking_coordinates()
        self.assertEqual(expected, output)

    def test_incorrect_get_parking_coordinates(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--x_start', type=int, default=50, help='X of start')
        parser.add_argument('--y_start', type=int, default=0, help='Y of start')
        parser.add_argument('--parking_spot', type=list, default=[6], help='empty car position in parking out of 12')
        args = parser.parse_args()

        pl = ParkingLot(args.parking_spot)

        parkingenv = pl.get_cars()
        emptySpots = []

        cars = {1: [[45, 20]], 2: [[65, 20]],
        3: [[35, 32]], 4: [[65, 32]],
        5: [[35, 44]], 6: [[65, 44]],
        7: [[35, 56]], 8: [[65, 56]],
        9: [[35, 68]], 10: [[65, 68]],
        11: [[35, 80]], 12: [[65, 80]]}

        expected = 0
        output = get_parking_coordinates()
        self.assertNotEqual(expected, output)
    


if __name__ == '__main__':
    unittest.main()
