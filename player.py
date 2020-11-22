from huesitos import Huesito
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x=50, y=400, width=64, height=64):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.game = game
        self.settings = game.settings
        self.win = game.win
        self.width = width
        self.height = height
        self.in_jump = False
        self.left = False
        self.right = False
        self.jump_step = 0
        self.jump_y0 = self.y
        self.jump_max_height = 2
        self.walk_count = 0
        self.animals_animation = game.animals_animation
        self.frame_count = 0
        self.animation_direction = 1

    def draw(self, win):
        if self.frame_count + 1 >= 3 * self.settings.framesPerKeyframe:
            self.frame_count = 0

        if self.left:
            self.animals_animation.draw_frame(
                win,
                self.x, self.y,
                self.frame_count // self.settings.framesPerKeyframe,
                1
            )
        elif self.right:
            self.animals_animation.draw_frame(
                win,
                self.x, self.y,
                self.frame_count // self.settings.framesPerKeyframe,
                2
            )
        else:
            self.animals_animation.draw_frame(
                win,
                self.x, self.y,
                self.frame_count // self.settings.framesPerKeyframe,
                0
            )

    def stand(self):
        self.left = False
        self.right = False
        self.frame_count += 1

    def shoot(self):
        if len(self.game.huesitos) < self.settings.bullets_allowed:
            new_huesito = Huesito(self)
            self.game.huesitos.add(new_huesito)

    def update(self):
        if self.left:
            if self.x < self.settings.x_vel:
                self.x = 0
            else:
                self.x -= self.settings.x_vel
            self.frame_count += 1
        elif self.right:
            if (self.x + self.settings.x_vel) > (self.settings.screen_width - self.width):
                self.x = (self.settings.screen_width - self.width)
            else:
                self.x += self.settings.x_vel
            self.frame_count += 1
        else:
            self.frame_count += 1

        if self.in_jump:
            self.y = self.jump_y0 - (
                self.settings.jump_v0 * (self.jump_step * self.settings.t_const) +
                self.settings.g * (self.jump_step * self.settings.t_const) ** 2 / 2
            )
            self.jump_step += 1
            if self.y > self.jump_y0:
                self.y = self.jump_y0
                self.in_jump = False
                self.jump_step = 0
