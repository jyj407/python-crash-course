class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (255, 0, 0) # RGB -- Red
        #self.bg_color = (0, 255, 0) # RGB -- Green 
        #self.bg_color = (0, 0, 255) # RGB -- Blue
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
