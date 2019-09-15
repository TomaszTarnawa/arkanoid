import pygame

from pygame.sprite import collide_rect, collide_circle, collide_mask, collide_rect_ratio

from game.ball import Ball, START_POSE_BALL, START_SPEED
from game.brick_factory import BrickFactory
from game.bricks import BlueBrick, BlueHardBrick, GreenBrick, GreenHardBrick, RedBrick, RedHardBrick, VeryHardBrick
from game.bricks_wall import BricksWall
from game.end_scene import EndScene
from game.help_function import get_imag
from game.platform import Platform, START_POSE_PLATFORM
from game.scene_base import SceneBase


class GameScene(SceneBase):
    temp_brick = None

    def __init__(self):
        SceneBase.__init__(self)
        self.live = 3
        self.start_move = False
        self.background = '../textures/background.png'
        self.bricks_factory = BrickFactory(BlueBrick, BlueHardBrick, GreenBrick, GreenHardBrick, RedBrick, RedHardBrick,
                                           VeryHardBrick)
        self.level_generator = BricksWall(self.bricks_factory)
        self.temp_brick = self.level_generator.level_one()
        self.spriteBall = pygame.sprite.RenderPlain(Ball())
        self.spritePlatform = pygame.sprite.RenderPlain(Platform())
        self.spriteBricks = pygame.sprite.RenderPlain(*self.temp_brick)
        self.all_sprite = pygame.sprite.Group(self.spriteBall, self.spritePlatform)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass
        if pressed_keys[pygame.K_SPACE]:
            self.start_move = True

    def Update(self):
        ball = self.spriteBall.sprites()[0]
        platform = self.spritePlatform.sprites()[0]
        if ball.rect.center[1] > platform.rect.top:
            self.live -= 1
            if not self.live:
                self.SwitchToScene(EndScene("GAME OVER. Press ENTER to Try Again or ESCAPE to Quit"))
            self.start_move = False
            ball.rect.center = START_POSE_BALL
            ball.move_x = START_SPEED[0]
            ball.move_y = START_SPEED[1]
            platform.rect.centerx = START_POSE_PLATFORM[0]
            platform.rect.top = START_POSE_PLATFORM[1]

        if self.start_move:
            # najbardziej problematyczna część gry kolizje
            hit_sprite = pygame.sprite.spritecollide(ball, self.spriteBricks, 0, collide_rect)
            if hit_sprite:
                for hit in hit_sprite:
                    self.spriteBall.update(hit)
                    hit.update()
            
            bounce_platform = pygame.sprite.collide_rect(ball, platform)
            if bounce_platform:
                b_move_x, b_move_y = ball.speed_x, ball.speed_y
                b_x, b_y = ball.rect.x, ball.rect.y
                ball.rect.bottom = platform.rect.top
                # ball.move_y += 1
                ball.speed_x = platform.angle(b_x, b_y, b_move_x, b_move_y)
                if platform.rect.topleft[0] <= b_x <= platform.rect.topright[0]:
                    ball.move_y *= -1
            self.all_sprite.update()

    def Render(self, screen):
        screen.blit(get_imag(self.background)[0], (0, 0))
        self.spriteBricks.draw(screen)
        self.spriteBall.draw(screen)
        self.spritePlatform.draw(screen)
