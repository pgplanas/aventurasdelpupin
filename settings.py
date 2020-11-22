class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 852
        self.screen_height = 480
        self.bg = 'bg.jpg'

        # World settings
        self.framesPerKeyframe = 3
        self.FPS = 33
        self.t_const = self.FPS / 1000
        self.px_const = 0.02625  # m/px
        self.g = -9.81 / self.px_const

        # Player settings
        self.lives = 3
        self.x_vel = 6
        self.jump_v0 = 5 / self.px_const

        # Bullet settings
        self.bullets_allowed = 10
        self.bullet_speed = 15
