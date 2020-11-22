import pygame


class SpriteAnimations:
    def __init__(self, base_image_name, number_of_sprites_x, number_of_sprites_y):
        self.scale_factor = 2

        self.base_image = pygame.image.load(base_image_name)
        self.base_image = pygame.transform.scale(
            self.base_image,
            (self.base_image.get_rect().size[0] * self.scale_factor,
             self.base_image.get_rect().size[1] * self.scale_factor)
        )
        self.sprite_width = self.base_image.get_rect().size[0] / number_of_sprites_x
        self.sprite_height = self.base_image.get_rect().size[1] / number_of_sprites_y

    def draw_frame(self, win, x, y, frame_x, frame_y):
        win.blit(
            self.base_image,
            (x, y),
            (frame_x * self.sprite_width, frame_y * self.sprite_height, self.sprite_width, self.sprite_height)
        )
