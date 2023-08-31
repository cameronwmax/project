import pygame
import random

class Settings:
    """A class to store all settings for the game"""

    def __init__(self):
        """Initialize the games static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.background = pygame.image.load("images/road_grass/background.png")

        # Character settings
        self.chickens_limit = 3

        # How quickly game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout"""
        # Character settings
        self.character_speed = 2.5
        
        # Cars settings
        self.car_speed = 3.25
        self.car_speed1 = 4.3
        self.car_speed2 = 3.5
        self.car_speed3 = 4.1
        self.car_speed4 = 3.3
        self.car_speed5 = 4.4
        self.car_speed6 = 3.5
        self.car_speed7 = 4.25

    def increase_speed(self):
        """Increase speed settings"""
        self.character_speed *= self.speedup_scale
        self.car_speed *= self.speedup_scale
        self.car_speed1 *= self.speedup_scale
        self.car_speed2 *= self.speedup_scale
        self.car_speed3 *= self.speedup_scale
        self.car_speed4 *= self.speedup_scale
        self.car_speed5 *= self.speedup_scale
        self.car_speed6 *= self.speedup_scale
        self.car_speed7 *= self.speedup_scale