import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Define a cor do background.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Inicializa o loop principal do jogo."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        # Monitora e responde eventos de mouse e teclado.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responde a teclas pressionadas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responde a teclas quando soltas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Cria uma nova bala e adiciona ao grupo de balas"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Atualiza a posição das balas e elimina as balas antigas"""
        # Atualiza posição das balas
        self.bullets.update()
        # Elimina as balas que estão fora da tela
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Cria uma frota de aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Calcula o espaço disponível para os aliens em uma linha
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determina o número de linhas de aliens que cabe na tela
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Cria uma frota inteira de aliens
        for row_number in range(number_rows - 5):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Cria um alien e adiciona na primeira linha"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        # Preenche a tela com a cor escolhida em cada passagem do loop.
        self.screen.fill(self.settings.bg_color)
        # Renderiza a nave na tela
        self.ship.blitme()
        # Renderiza o grupo de balas atiradas
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Renderiza frota de aliens
        self.aliens.draw(self.screen)
        # Deixa visível a ultima tela recentemente renderizada.
        pygame.display.flip()


if __name__ == '__main__':
    # Cria uma instancia e roda o jogo.
    ai = AlienInvasion()
    ai.run_game()
