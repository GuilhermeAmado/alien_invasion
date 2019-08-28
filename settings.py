class Settings:
    """Uma classe para guardar todas as configurações."""

    def __init__(self):
        """Inicializa as configurações do jogo."""
        # Configurações de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configurações da nave
        self.ship_speed = 1.5

        # Configurações do projétil de bala
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
