import sys
sys.path.insert(0, '/Users/smitvaghela/Desktop/CS/automatic-car-parking')
import unittest
import numpy as np

from Car import determine_empty_spot
from Car import get_parking_coordinates
from ParkingLot import ParkingLot


class car_unittest((unittest.TestCase)):
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
        pl = ParkingLot([5])
        parkingenv = pl.get_cars()
        determine_empty_spot(parkingenv)
        expected = (35, 56)
        output = get_parking_coordinates()
        self.assertEqual(expected, output)

    def test_correct_right_get_parking_coordinates(self):
        pl = ParkingLot([6])
        parkingenv = pl.get_cars()
        determine_empty_spot(parkingenv)

        expected = (35, 56)
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
        emptySpots = [5]

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
