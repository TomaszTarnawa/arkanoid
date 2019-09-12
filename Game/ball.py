from math import cos, sin, radians, sqrt

import pygame

from Game.help_function import get_imag
from Game.moving_objects import MovingObjects

START_POSE_BALL = 554, 573
START_SPEED = 6, -6


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect, self.mask = get_imag('../textures/ball25.png')
        self.rect = self.rect.inflate(-10, -10)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.center = START_POSE_BALL
        self.move_x, self.move_y = START_SPEED

        # self.direction = [pos[0] - 1, pos[1] - self.get_speed()]
        # self.__A = None
        # self.__B = None
        # self.bounce_flag = 0

    @property
    def speed_y(self):
        return self.move_y

    @property
    def speed_x(self):
        return self.move_x

    @speed_x.setter
    def speed_x(self, new_x):
        if -START_SPEED[0] < new_x < START_SPEED[0]:
            self.move_x = new_x
            self.move_y = round(sqrt(72 - new_x ** 2))

    def get_image(self):
        return self.image

    def update(self, spri=None):
        if spri:
            self.bounce(spri)
        self._fly()

        # angle = 90
        # pos_x, pos_y = self.get_pos()
        # len_vector = self.get_speed()
        # new_x = (pos_x + len_vector) * cos(radians(angle)) - (pos_y + len_vector) * sin(radians(angle))
        # new_y = (pos_x + len_vector) * sin(radians(angle)) + (pos_y + len_vector) * cos(radians(angle))
        # self.direction = [new_x, new_y]

    def bounce(self, spri):
        if self.rect.bottom > spri.rect.top:
            if self.move_x < 0 and self.move_y > 0:
                self.move_y *= -1
            if self.move_x > 0 and self.move_y > 0:
                self.move_y *= -1
        if self.rect.top < spri.rect.bottom:
            if self.move_x < 0 and self.move_y < 0:
                self.move_y *= -1
            if self.move_x > 0 and self.move_y < 0:
                self.move_y *= -1
        if self.rect.left < spri.rect.right:
            if self.move_x < 0 and self.move_y < 0:
                self.move_x *= -1
            if self.move_x < 0 and self.move_y > 0:
                self.move_x *= -1
        if self.rect.right > spri.rect.left:
            if self.move_x > 0 and self.move_y < 0:
                self.move_x *= -1
            if self.move_x > 0 and self.move_y > 0:
                self.move_x *= -1


    def _fly(self):
        # print(self.move_x, self.move_y)
        new_pos = self.rect.move((self.move_x, self.move_y))
        # self.rect = new_pos
        if not self.area.contains(new_pos):
            if self.rect.left < self.area.left:
                self.rect.left = self.area.left
                self.move_x *= -1
            if self.rect.right > self.area.right:
                self.rect.right = self.area.right
                self.move_x *= -1
            if self.rect.bottom > self.area.bottom:
                self.rect.bottom = self.area.bottom
                self.move_y *= -1
            if self.rect.top < self.area.top:
                self.rect.top = self.area.top
                self.move_y *= -1
            new_pos = self.rect.move((self.move_x, self.move_y))
        self.rect = new_pos

    # PONIŻEJ NIC CIEKAWEGO

    # x_a, y_a = self.get_pos()
    # x_b, y_b = self.direction
    # self.set_pos(x_b, y_b)
    # vector_xy = [x_b - x_a, y_b - y_a]
    # new_x = sqrt(vector_xy[1] ** 2 + vector_xy[1] ** 2)
    # self.__A = (y_a - y_b) / (x_a - x_b)
    # self.__B = (y_a - (y_a - y_b) / (x_a - x_b)) * x_a
    # new_y = self.__A * new_x + self.__B
    # self.direction = [new_x, new_y]

    # if self.move_x == 0:
    #     self.move_y = -self.move_y
    # if self.move_y == 0:
    #     self.move_x = -self.move_x
    # if self.move_x < 0:
    #     if self.move_y < 0 or self.move_y > 0:
    #         if self.rect.left < self.area.left:
    #             self.move_x = -self.move_x
    #         if self.rect.top < self.area.top or self.rect.bottom > self.area.bottom:
    #             self.move_y = -self.move_y
    # if self.move_x > 0:
    #     if self.move_y < 0 or self.move_y > 0:
    #         if self.rect.right < self.area.right:
    #             self.move_x = -self.move_x
    #         if self.rect.top < self.area.top or self.rect.bottom > self.area.bottom:
    #             self.move_y = -self.move_y

    #     x, y = self.direction
    #     if x > 1118 or y > 620:
    #         distant_to_frame = [1118 - x, 620 - y]
    #         self.direction = [x - distant_to_frame[0], y - distant_to_frame[1]]
    #         self.set_pos(distant_to_frame)
    #     if  x < 0  or y < 0:
    #         distant_to_frame = [0 + x, 0 + y]
    #         self.direction = [x - distant_to_frame[0], y - distant_to_frame[1]]
    #         self.set_pos(distant_to_frame)
    #
    #
    #
    #
    #
