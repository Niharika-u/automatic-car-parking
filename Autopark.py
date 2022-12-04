import argparse
import np as np

from ParkingLot import ParkingLot
from Environment import Environment
from Car import Car
import cv2


def get_empty_spots_from_sensor():
    empty_spots = [3, 6]
    return empty_spots


if __name__ == '__main__':
    empty_parking_spots = get_empty_spots_from_sensor()

    parser = argparse.ArgumentParser()
    parser.add_argument('--x_start', type=int, default=50, help='X of start')
    parser.add_argument('--y_start', type=int, default=0, help='Y of start')
    parser.add_argument('--parking_spot', type=list, default=empty_parking_spots,
                        help='empty car position in parking out of 12')

    args = parser.parse_args()

    # Default Value initialization
    start = np.array([args.x_start, args.y_start])

    # Creating the parking lot
    parking = ParkingLot(args.parking_spot)

    # Creating obstacles
    obs = parking.generate_obstacles()

    # Create Environment coordinates
    env = Environment(obs)
    # Create my car with base values initialized
    my_car = Car(start[0], start[1], np.deg2rad(90), length=6) #actual length of the car.
    # Display my car in the parking lot
    res = env.render(my_car.x, my_car.y, my_car.psi)
    cv2.imshow('environment', res)
    key = cv2.waitKey(1000)
    my_car.move_car(env, parking)
    key = cv2.waitKey(1000)
    cv2.destroyAllWindows()
