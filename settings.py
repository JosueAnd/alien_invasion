class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.bg_color = (125, 125, 125)
        self.caption = 'Alien Invasion'
        self.screen_width = 1200
        self.screen_height = 800

        # Ship settings.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_speed = self.ship_speed * 1.5
        self.bullet_width = 300  # was 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_limit = 3

        # Alien settings.
        self.alien_speed = .5
        self.fleet_drop_speed = 35
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
