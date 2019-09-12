from abc import ABC, abstractmethod

import pygame

from Game.help_function import get_imag, if_is_dead


class Bricks(ABC, pygame.sprite.Sprite):
    def __init__(self, sub_event):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 0
        self.image = None
        self.height = 21
        self.width = 43
        self.__sub_event = sub_event
        self.rect = None

    def update(self):
        self.damaged()

    def get_pos(self):
        pos = ''
        flag = 0
        for char in self.__sub_event:
            if char == '(':
                flag = 1
                continue
            if char == ',':
                x = int(pos)
                pos = ''
                continue
            if char == ')':
                y = int(pos)
                continue
            if flag:
                pos += char
        return x, y

    def get_image(self):
        return self.image

    @if_is_dead  # funkcja zwraca "Dead" kiedy lives = 0
    def get_event(self):
        return self.__sub_event

    def damaged(self):
        self.lives -= 1
        if not self.lives:
            self.kill()


class BlueBrick(Bricks):

    def __init__(self, sub_event):
        super().__init__(sub_event)
        self.lives = 1
        self.image, self.rect, self.mask = get_imag('../textures/blue_brick.png')
        self.rect.topleft = self.get_pos()
        self.rect = self.rect.inflate(-1, -2)


class BlueHardBrick(Bricks):

    def __init__(self, sub_event):
        super().__init__(sub_event)
        self.lives = 2
        self.image, self.rect, self.mask = get_imag('../textures/blue_hard_brick.png')
        self.rect.topleft = self.get_pos()
        self.rect = self.rect.inflate(-1, -2)

    def update(self):
        super().update()
        if self.lives == 1:
            self.image, self.rect, self.mask = get_imag('../textures/blue_hard_brick_damaged.png')
            self.rect.topleft = self.get_pos()
            self.rect = self.rect.inflate(-1, -2)


class GreenBrick(Bricks):

    def __init__(self, sub_event):
        super().__init__(sub_event)
        self.lives = 1
        self.image, self.rect, self.mask = get_imag('../textures/green_brick.png')
        self.rect.topleft = self.get_pos()
        self.rect = self.rect.inflate(-1, -2)


class GreenHardBrick(Bricks):

    def __init__(self, sub_event):
        super().__init__(sub_event)
        self.lives = 2
        self.image, self.rect, self.mask = get_imag('../textures/green_hard_brick.png')
        self.rect.topleft = self.get_pos()
        self.rect = self.rect.inflate(-1, -2)

    def update(self):
        super().update()
        if self.lives == 1:
            self.image, self.rect, self.mask = get_imag('../textures/green_hard_brick_damaged.png')
            self.rect.topleft = self.get_pos()
            self.rect = self.rect.inflate(-1, -2)


class RedBrick(Bricks):

    def __init__(self, sub_event):
        super().__init__(sub_event)
        self.lives = 1
        self.image, self.rect, self.mask = get_imag('../textures/red_brick.png')
        self.rect.topleft = self.get_pos()
        self.rect = self.rect.inflate(-1, -2)


class RedHardBrick(Bricks):

    def __init__(self, sub_event):
        super().__init__(sub_event)
        self.lives = 2
        self.image, self.rect, self.mask = get_imag('../textures/red_hard_brick.png')
        self.rect.topleft = self.get_pos()
        self.rect = self.rect.inflate(-1, -2)

    def update(self):
        super().update()
        if self.lives == 1:
            self.image, self.rect, self.mask = get_imag('../textures/red_hard_brick_damaged.png')
            self.rect.topleft = self.get_pos()
            self.rect = self.rect.inflate(-1, -2)


class VeryHardBrick(Bricks):

    def __init__(self, sub_event):
        super().__init__(sub_event)
        self.lives = 3
        self.image, self.rect, self.mask = get_imag('../textures/very_hard_brick.png')
        self.rect.topleft = self.get_pos()
        self.rect = self.rect.inflate(-1, -2)

    def update(self):
        super().update()
        if self.lives == 1:
            self.image, self.rect, self.mask = get_imag('../textures/very_hard_brick_badly_damaged.png')
            self.rect.topleft = self.get_pos()
            self.rect = self.rect.inflate(-1, -2)
        if self.lives == 2:
            self.image, self.rect, self.mask = get_imag('../textures/very_hard_brick_damaged_2.png')
            self.rect.topleft = self.get_pos()
            self.rect = self.rect.inflate(-1, -2)
