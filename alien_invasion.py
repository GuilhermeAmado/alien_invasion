import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Classe geral para gerenciar recursos e comportamentos."""

    def __init__(self):
        """Inicializa o jogo e cria recursos."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Define a cor do background.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Inicializa o loop principal do jogo."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Monitora e responde eventos de mouse e teclado.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # Preenche a tela com a cor escolhida em cada passagem do loop.
        self.screen.fill(self.settings.bg_color)
        # Renderiza a nave na tela
        self.ship.blitme()
        # Deixa visível a ultima tela recentemente renderizada.
        pygame.display.flip()


if __name__ == '__main__':
    # Cria uma instancia e roda o jogo.
    ai = AlienInvasion()
    ai.run_game()
    