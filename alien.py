import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Classe que representa um unico alien"""

    def __init__(self, ai_game):
        """Inicializa um alien e define sua posição inicial"""
        super().__init__()
        self.screen = ai_game.screen

        # Carrega a imagem do alien e define atributos do retangulo
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Inicializa cada alien no canto esquerdo/topo da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição horizontal do alien
        self.x = float(self.rect.x)
