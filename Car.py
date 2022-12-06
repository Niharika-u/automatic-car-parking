import cv2
import numpy as np

import config

all_empty_spots = []
empty_spots = []


class Car:
    # Constructor to initialize the time, length, x xis, y axis and angle
    def __init__(self, x_0, y_0, psi_0, length):
        self.L = length
        self.x = x_0
        self.y = y_0
        self.psi = psi_0

    # This function will update the state of the car
    def update_car_state(self, x=0, y=0, psi=0):
        self.x = self.x + x
        self.y = self.y + y
        self.psi = psi

    # This function will calculate all the angles and acceleration needed to park the car
    # once the parking spot is found and is feasible
    def park(self, env):
        if empty_spots[0] % 2:
            self.park_left(env)
        else:
            self.park_right(env)

    def park_left(self, env):
        print("Initiating Parking Sequence.")
        self.update_car_state(y=2, psi=np.deg2rad(90))
        res = env.render(self.x, self.y, self.psi)
        cv2.imshow('environment', res)
        cv2.waitKey(5000)

        self.update_car_state(y=3, psi=np.deg2rad(90))
        res = env.render(self.x, self.y, self.psi)
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        print("Starting to back up.")
        self.update_car_state(x=-2, y=-2)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-3, y=-3)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-2, y=-2)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-3, y=-3)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-1, y=-1)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-2, y=-2)
        res = env.render(self.x, self.y, np.deg2rad(45))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=-2, y=3)
        res = env.render(self.x, self.y, np.deg2rad(90))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        print("Parking complete.")

    def park_right(self, env):
        self.update_car_state(y=2, psi=np.deg2rad(90))
        res = env.render(self.x, self.y, self.psi)
        cv2.imshow('environment', res)
        cv2.waitKey(5000)

        self.update_car_state(y=3, psi=np.deg2rad(90))
        res = env.render(self.x, self.y, self.psi)
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        print("Starting to back up.")
        self.update_car_state(x=2, y=-2)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=3, y=-3)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=2, y=-2)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=3, y=-3)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=1, y=-1)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=2, y=-2)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=2, y=3)
        res = env.render(self.x, self.y, np.deg2rad(90))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)
        print("Parking complete.")

    # Function to move car
    def move_car(self, env, parking):

        parking_environment = parking.get_cars()
        determine_empty_spot(parking_environment)
        to_park_x, to_park_y = get_parking_coordinates()
        to_park_y = to_park_y - 12

        for i in range(30):
            if i == 13 and (5 in config.big_cars):
                cv2.waitKey(1500)
                print("Feasibility Check.")
                print("Not enough Space")
            if i % 6 == 0:
                print("Locating empty parking spot.")
            self.update_car_state(y=to_park_y / 30 + 0.2, psi=np.deg2rad(90))
            res = env.render(self.x, self.y, self.psi)
            cv2.imshow('environment', res)
            cv2.waitKey(150)
        if to_park_y == 92:
            print("Could not find an empty parking spot.")
        else:
            print("Located parking spot.")

        cv2.waitKey(1000)
        if not to_park_y == 92:
            self.park(env)


def get_parking_coordinates():
    if empty_spots and empty_spots[0] != len(config.cars):
        if empty_spots[0] % 2:
            coord = config.cars.get(empty_spots[0] + 2)
        else:
            coord = config.cars.get(empty_spots[0] + 1)
        x, y = coord[0]
        return x, y
    else:
        return 35, 104


def determine_empty_spot(parking_environment):
    for i in range(1, len(parking_environment)):
        if i not in parking_environment:
            all_empty_spots.append(i)
        if i not in parking_environment and (i + 2 not in config.big_cars or i - 2 not in config.big_cars):
            empty_spots.append(i)

    return empty_spots
