import pygame


class Ship:
    """Classe que gerencia a nave espacial."""

    def __init__(self, ai_game):
        """Inicializa a nave e define a posição inicial"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carrega a imagem da nave e define o rect (retangulo).
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # Inicializa uma nova nave no centro na parte inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom

        # Armazena um valor decimal para a posição horizontal da nave
        self.x = float(self.rect.x)

        # Flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualiza a posição da nave baseado nas flags de movimento."""
        # Atualiza a posição x da nave baseado na configuração de velocidade
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # Atualiza o objeto retangulo a partir do self.x
        self.rect.x = self.x

    def blitme(self):
        """Renderiza a nave na sua posição atual"""
        self.screen.blit(self.image, self.rect)
