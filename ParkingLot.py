import numpy as np

import config


class ParkingLot:
    # Constructor
    def __init__(self, empty_parking_spot):
        # Initializing the parked cars
        self.parked_cars = self.create_car()

        # Creating the walls
        self.walls = [[70, i] for i in range(-5, 90)] + \
                     [[30, i] for i in range(10, 105)]

        self.obs = np.array(self.walls)
        self.cars = config.cars

        self.big_cars = config.big_cars
        self.small_cars = config.small_cars

        # This is the empty space for the car in the parking lot
        # defined in arguments
        for pos in empty_parking_spot:
            self.cars.pop(pos)

    def create_car(self):
        # meshgrid function is used to create a rectangular grid out of two given one-dimensional
        # arrays representing the Cartesian indexing or Matrix indexing.
        car_coordinate_x, car_coordinate_y = np.meshgrid(
            np.arange(-2, 2), np.arange(-4, 4))
        # The dstack() is used to stack arrays in sequence depth wise (along third axis)
        parked_cars = np.dstack(
            [car_coordinate_x, car_coordinate_y]).reshape(-1, 2)
        return parked_cars

    def create_small_car(self):
        # meshgrid function is used to create a rectangular grid out of two given one-dimensional
        # arrays representing the Cartesian indexing or Matrix indexing.
        car_coordinate_x, car_coordinate_y = np.meshgrid(
            np.arange(-2, 2), np.arange(-3, 3))
        # The dstack() is used to stack arrays in sequence depth wise (along third axis)
        parked_cars = np.dstack(
            [car_coordinate_x, car_coordinate_y]).reshape(-1, 2)
        return parked_cars

    def create_big_car(self):
        # meshgrid function is used to create a rectangular grid out of two given one-dimensional
        # arrays representing the Cartesian indexing or Matrix indexing.
        car_coordinate_x, car_coordinate_y = np.meshgrid(
            np.arange(-2, 2), np.arange(-5, 5))
        # The dstack() is used to stack arrays in sequence depth wise (along third axis)
        parked_cars = np.dstack(
            [car_coordinate_x, car_coordinate_y]).reshape(-1, 2)
        return parked_cars

    def generate_obstacles(self):
        for i in self.cars.keys():
            for j in range(len(self.cars[i])):
                if i in self.small_cars:
                    obstacle = self.create_small_car() + self.cars[i]
                elif i in self.big_cars:
                    obstacle = self.create_big_car() + self.cars[i]
                else:
                    obstacle = self.create_car() + self.cars[i]
                self.obs = np.append(self.obs, obstacle)
        return np.array(self.obs).reshape(-1, 2)

    def get_cars(self):
        return self.cars
