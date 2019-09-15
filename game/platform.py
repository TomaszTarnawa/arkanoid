import pygame

from game.help_function import get_imag
from game.moving_objects import MovingObjects

START_POSE_PLATFORM = 559, 590


class Platform(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect, self.mask = get_imag('../textures/platforma_max.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.centerx, self.rect.top = START_POSE_PLATFORM
        self.move = 6

    def get_image(self):
        return self.image

    def update(self):
        keys_status = pygame.key.get_pressed()
        if keys_status[pygame.K_LEFT]:
            self.move_left()
        if keys_status[pygame.K_RIGHT]:
            self.move_right()
        if self.rect.right > self.area.right:
            self.rect.right = self.area.right
        if self.rect.left < self.area.left:
            self.rect.left = self.area.left

    def move_left(self):
        self.rect.x -= self.move

    def move_right(self):
        self.rect.x += self.move

    def angle(self, b_x, b_y, b_move_x, b_move_y):  # podział platformy na 5 sektorów o długości 57
        plat_x = self.rect.topleft[0]
        if plat_x < b_x < plat_x + 57:
            if b_move_x < 0:
                return round(b_move_x * 0.6)
            return round(b_move_x * 1.4)

        if plat_x + 57 < b_x < plat_x + 57 * 2:
            if b_move_x < 0:
                return round(b_move_x * 0.8)
            return round(b_move_x * 1.2)

        if plat_x + 57*2 < b_x < plat_x + 57 * 3:
            return b_move_x

        if plat_x + 57*3 < b_x < plat_x + 57 * 4:
            if b_move_x < 0:
                return round(b_move_x * 1.2)
            return round(b_move_x * 0.8)

        if plat_x + 57*4 < b_x < plat_x + 57 * 5:
            if b_move_x < 0:
                return round(b_move_x * 1.4)
            return round(b_move_x * 0.6)

        return b_move_x



