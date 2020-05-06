class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.bg_color = (125, 125, 125)
        self.caption = 'Alien Invasion'
        self.screen_width = 750
        self.screen_height = 500

        # Ship settings.
        # self.ship_speed = 10  # was 1.5
        self.ship_limit = 3
        self.game_over = 0

        # Bullet settings.
        # self.bullet_speed = self.ship_speed * 1.5
        self.bullet_width = 3  # was 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_limit = 3

        # Alien settings.
        # self.alien_speed = 5  # was .5
        self.fleet_drop_speed = 25  # was 35
        # fleet_direction of 1 represents right; -1 represents left.
        # self.fleet_direction = 1

        # How quickly the game speeds up from level to level.
        self.speed_increase = 1.1
        self.score_increase = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 10
        self.bullet_speed = self.ship_speed * 1.5
        self.alien_speed = 5

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speed_increase
        self.bullet_speed *= self.speed_increase
        self.alien_speed *= self.speed_increase
        self.alien_points = int(self.alien_points * self.score_increase)
