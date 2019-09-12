import os
import random

import pygame

# funkcje związane z czcionka zaczerpnięte ze strony https://nerdparadise.com/programming/pygame/part5

font_preferences = [
    'Times New Roman',
    'Arial',
    'Consolas',
    'Tahoma',
    'Comic Sans MS']


def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names
    choices = map(lambda x: x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)


_cached_fonts = {}


def get_font(font_preference, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font is None:
        font = make_font(font_preference, size)
        _cached_fonts[key] = font
    return font


_cached_text = {}


def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image is None:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image


# funkcja związana z teksturami zaczerpnięte ze strony https://nerdparadise.com/programming/pygame/part2

_image_library = {}


def get_imag(path):   # funkcja do usprawnienia chimp.py pygame load_image
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        image.convert()
        image.set_colorkey((255, 255, 255))
        _image_library[path] = image
    return image, image.get_rect(), pygame.mask.from_surface(image)


def if_is_dead(func):  # decorator dla metody w klasie Brick
    def wrapper(self):
        if self.lives == 0:
            return "Dead"
        return func(self)
    return wrapper
