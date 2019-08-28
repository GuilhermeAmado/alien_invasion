import pygame


class Ship:
    """Classe que gerencia a nave espacial."""

    def __init__(self, ai_game):
        """Inicializa a nave e define a posição inicial"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave e define o rect (retangulo).
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Inicializa uma nova nave no centro na parte inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Renderiza a nave na sua posição atual"""
        self.screen.blit(self.image, self.rect)
