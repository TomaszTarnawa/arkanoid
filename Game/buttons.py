from abc import ABC, abstractmethod

import pygame


class Button(ABC):

    def __init__(self, name):
        self.title = name
        self.color = (0, 128, 0)

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def pressed_on(self, events, pressed_keys):
        pass


class PlayButton(Button):
    image = None

    def pressed_on(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        button_aimed = 475 < x < 644 and 276 < y < 310
        mouse_click = pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]
        if button_aimed and mouse_click:  # Move to the next scene when the user click PLAY GAME
            return True

    def get_color(self):
        x, y = pygame.mouse.get_pos()
        if 475 < x < 644 and 276 < y < 310:
            value = (0, 0, 128)
        else:
            value = (0, 128, 0)
        self.color = value
        return self.color


class QuitButton(Button):
    image = None

    def pressed_on(self, events, pressed_keys):
        x, y = pygame.mouse.get_pos()
        button_aimed = 523 < x < 595 and 326 < y < 360
        mouse_click = pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]
        if button_aimed and mouse_click:
            return True

    def get_color(self):
        x, y = pygame.mouse.get_pos()
        if 523 < x < 595 and 326 < y < 360:
            value = (0, 0, 128)
        else:
            value = (0, 128, 0)
        self.color = value
        return self.color

