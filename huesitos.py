import pygame
from pygame.sprite import Sprite


class Huesito(Sprite):
    """A class to manage little bones fired by the Pupín"""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.win = game.win
        self.settings = game.settings
        self.x = game.x
        self.y = game.y
        self.angle = 0

        # Create a bullet rect at (0, 0) and then set correct position.

        # Store the bullet's position as a decimal value.
        self.y = float(self.y)
        self.x = float(self.x)

    def update_pos(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.x += self.settings.bullet_speed
        self.angle += 5

    def draw(self):
        """Draw the bullet to the screen."""
        temp_img = pygame.image.load('huesito2.png')
        temp_img = pygame.transform.rotate(temp_img, self.angle)
        self.win.blit(temp_img, (self.x, self.y))
