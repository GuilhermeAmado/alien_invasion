import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Classe para gerenciar as balas atiradas pela nave"""

    def __init__(self, ai_game):
        """Cria um objeto de projétil de bala na posição atual da nave"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Cria um retangulo de bala em (0, 0) e então seta a posição correta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Guarda a posição da bala como um valor decimal
        self.y = float(self.rect.y)

    def update(self):
        """Move a bala em direção ao topo da tela"""
        # Atualiza o valor decimal da posição da bala
        self.y -= self.settings.bullet_speed
        # Atualiza a posição do retangulo
        self.rect.y = self.y

    def draw_bullet(self):
        """Renderiza uma bala na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
