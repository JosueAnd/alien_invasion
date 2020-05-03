import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode(
        #     (0, 0), pygame.FULLSCREEN
        # )
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption(self.settings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            # Set ship right movement flag to True.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Set ship left movement flag to True.
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            # Shortcut to quit the game.
            sys.exit()

    def _check_key_up_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            # Set ship right movement flag to False.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Set ship left movement flag to False.
            self.ship.moving_left = False

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        """Create a fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Determine the number of columns of aliens that fit on the screen.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_of_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_of_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _delete_old_bullets(self):
        """Get rid of bullets that have gone off screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _draw_all_bullets(self):
        """Draw each bullet in the bullets group."""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_limit:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update the position of each bullet along the y axis.
        self.bullets.update()
        self._delete_old_bullets()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        # Redraw the ship during each pass through the loop.
        self.ship.blitme()
        # Redraw each bullet during each pass through the loop.
        # pygame.sprite.Group() has an update method that calls each group member's
        # update method. We could add the draw_bullet method to the update method in
        # the Bullet class however we are trying to keep each method doing one thing,
        # what the name of the method makes clear is happening, so we make that a
        # method in this class and call it here.
        self._draw_all_bullets()
        # Redraw the alien fleet during each pass through the loop.
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
