import sys

import pygame

from settings import Settings


class AlienInvasion:
    """Classe geral para gerenciar recursos e comportamentos."""

    def __init__(self):
        """Inicializa o jogo e cria recursos."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Define a cor do background.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Inicializa o loop principal do jogo."""
        while True:
            # Monitora eventos de mouse e teclado.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Preenche a tela com a cor escolhida em cada passagem do loop.
            self.screen.fill(self.settings.bg_color)

            # Deixa visível a ultima tela recentemente renderizada.
            pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instancia e roda o jogo.
    ai = AlienInvasion()
    ai.run_game()
