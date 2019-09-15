import pygame

from game.help_function import font_preferences, create_text
from game.scene_base import SceneBase


class EndScene(SceneBase):
    def __init__(self, txt=None):
        super().__init__()
        self.end_txt = txt
        if txt:
            self.end_game = txt

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.Terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from game.main import run_game
                from game.title_scene import TitleScene
                from game.buttons import PlayButton
                from game.buttons import QuitButton
                run_game(1118, 620, 60, TitleScene(PlayButton, QuitButton))
                self.Terminate()

    def Update(self):
        if self.end_game:
            self.end_game = create_text(self.end_txt, font_preferences, 25, (255, 0, 0))

    def Render(self, screen):
        screen_half_x = screen.get_size()[0] // 2
        if self.end_game:
            screen.blit(self.end_game, (screen_half_x - self.end_game.get_width() // 2, 520))
