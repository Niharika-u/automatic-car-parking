import cv2
import numpy as np


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

        self.update_car_state(y=5, psi=np.deg2rad(90))
        res = env.render(self.x, self.y, self.psi)
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=5, y=-5)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=5, y=-5)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=3, y=-3)
        res = env.render(self.x, self.y, np.deg2rad(135))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        self.update_car_state(x=2, y=3)
        res = env.render(self.x, self.y, np.deg2rad(90))
        cv2.imshow('environment', res)
        cv2.waitKey(1000)

        print("Parking complete")

    # Function to move car
    def move_car(self, env):
        for i in range(5):
            print("Accelerating")
            print("Moving forward")
            self.update_car_state(y=10, psi=np.deg2rad(90))
            res = env.render(self.x, self.y, self.psi)
            cv2.imshow('environment', res)
            cv2.waitKey(1000)
