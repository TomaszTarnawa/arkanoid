from abc import ABC, abstractmethod

import pygame


# Klasa pod koniec wyłączona z użycia, zastąpiona Spritem

class MovingObjects(ABC, ):
    def __init__(self, x, y):
        self.speed = 0
        self._position = [x, y]
        self.direction = []

    @abstractmethod
    def get_event(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def bounce(self):
        pass

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_pos(self):
        return tuple(self._position)

    def set_pos(self, x, y):
        self._position = [x, y]
        return x, y

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, xy):
        self._direction = xy
