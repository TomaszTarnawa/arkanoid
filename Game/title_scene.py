import pygame
from pygame import locals as key

from Game.game_scene import GameScene
from Game.help_function import create_text, font_preferences
from Game.scene_base import SceneBase


class TitleScene(SceneBase):

    title_game = ''

    def __init__(self, button, button1):
        super().__init__()
        self.button_aim = False
        self.play_game_button = button("PLAY GAME")
        self.quit_game_button = button1("QUIT")


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if self.play_game_button.pressed_on(event, pressed_keys):
                self.SwitchToScene(GameScene())  # Move to the next scene when the user click PLAY GAME
            if self.quit_game_button.pressed_on(event, pressed_keys):
                self.Terminate()

    def Update(self):
        play_title = self.play_game_button.title
        quit_title = self.quit_game_button.title
        self.play_game_button.image = create_text(play_title, font_preferences, 30, self.play_game_button.get_color())
        self.quit_game_button.image = create_text(quit_title, font_preferences, 30, self.quit_game_button.get_color())
        self.title_game = create_text("ARKANOID", font_preferences, 72, (128, 0, 0))

    def Render(self, screen):
        screen.fill((255, 255, 255))
        screen_half_x = screen.get_size()[0]//2
        screen_half_y = screen.get_size()[1]//2

        width_play_game_image = screen_half_x - self.play_game_button.image.get_width() // 2
        height_play_game_image = screen_half_y - 17 - self.play_game_button.image.get_height() // 2

        width_quit_game_image = screen_half_x - self.quit_game_button.image.get_width() // 2
        height_quit_game_image = screen_half_y + 23 - self.quit_game_button.image.get_height() // 2

        screen.blit(self.play_game_button.image, (width_play_game_image, height_play_game_image))
        screen.blit(self.quit_game_button.image, (width_quit_game_image, height_quit_game_image))
        screen.blit(self.title_game, (screen_half_x - self.title_game.get_width() // 2, 20 + self.title_game.get_height() // 2))

