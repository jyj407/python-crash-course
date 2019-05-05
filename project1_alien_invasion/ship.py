import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship_rotate_right_90_degree.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the top center of the screen.
        self.rect.centery = self.screen_rect.centery
        self.rect.top = self.screen_rect.top
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centery)

        # Movement flags
        self.moving_bottom = False
        self.moving_top = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        # Check the bottom of ship is within the bottom boundary of the display screen.
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        # Note here we use another if instead of elif so that the ship stands still
        # when both the top and bottom keys are pressed bottom simultaneously.
        # Check the top of ship is within the top boundary of the display screen.
        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centery = self.center
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

