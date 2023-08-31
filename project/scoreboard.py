import pygame.font
from pygame.sprite import Group

from character import Character

class Scoreboard:
    """Class to report scoring info"""

    def __init__(self, cc_game):
        """Initialize scorekeeping attributes"""
        self.cc_game = cc_game
        self.screen = cc_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = cc_game.settings
        self.stats = cc_game.stats

        # Font settings for info
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prep initial scoreboard image
        self.prep_level()
        self.prep_highest_level()
        self.prep_lives()

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = str(f"Level: {self.stats.level}")
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)
        
        # Position the level info
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 10
        self.level_rect.top = 60

    def prep_highest_level(self):
        """Turn the highest level score into a rendered image"""
        highest_level = self.stats.highest_level
        highest_level_str = (f"HS LVL: {highest_level:,}")
        self.highest_level_image = self.font.render(highest_level_str, True,
                    self.text_color, self.settings.bg_color)
        
        # Place the highest level at the top center of the screen
        self.highest_level_rect = self.highest_level_image.get_rect()
        self.highest_level_rect.right = self.screen_rect.right - 10
        self.highest_level_rect.top = 10

    def check_highest_level(self):
        """Check to see if there is a new high level"""
        if self.stats.level > self.stats.highest_level:
            self.stats.highest_level = self.stats.level
            self.prep_highest_level()

    def show_score(self):
        """Draw level info to the screen"""
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.highest_level_image, self.highest_level_rect)
        self.lifes.draw(self.screen)

    def prep_lives(self):
        """Show how many lifes player has left"""
        self.lifes = Group()
        for life_number in range(self.stats.chickens_left):
            life = Character(self.cc_game)
            life.rect.x = 10 + life_number * life.rect.width
            life.rect.y = 10
            self.lifes.add(life)
