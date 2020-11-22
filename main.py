import sys
import pygame
from sprite_animations import SpriteAnimations
from player import Player
from settings import Settings


class AventurasDelPupin:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.win = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Las Aventuras del Pupín")

        self.animals_animation = SpriteAnimations('animals2.png', 12, 8)
        self.huesito = SpriteAnimations('huesito.png', 1, 1)
        self.bg = pygame.image.load('bg.jpg')
        self.clock = pygame.time.Clock()

        self.pupin = Player(self)
        self.huesitos = pygame.sprite.Group()

    def run_game(self):
        """Run the game"""
        while True:
            self.clock.tick(self.settings.FPS)
            self._check_events()
            self._update_all()
            self._redraw_game_window()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            self._check_keydown_events(event)
            self._check_keyup_events(event)

    def _update_all(self):
        self.pupin.update()
        self._update_huesitos()

    def _redraw_game_window(self):
        self.win.blit(self.bg, (0, 0))
        self._draw_huesitos()
        self.pupin.draw(self.win)
        pygame.display.flip()

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.pupin.left = False
                self.pupin.right = True
            if event.key == pygame.K_LEFT:
                self.pupin.left = True
                self.pupin.right = False
            if event.key == pygame.K_UP:
                self.pupin.in_jump = True
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_SPACE:
                self.pupin.shoot()
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key presses."""
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.pupin.right = False
            if event.key == pygame.K_LEFT:
                self.pupin.left = False

    def _update_huesitos(self):
        """Respond to key presses."""
        for huesito in self.huesitos.copy():
            if huesito.x >= self.settings.screen_width:
                self.huesitos.remove(huesito)
            else:
                huesito.update_pos()

    def _draw_huesitos(self):
        """Respond to key presses."""
        for huesito in self.huesitos:
            huesito.draw()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ap = AventurasDelPupin()
    ap.run_game()