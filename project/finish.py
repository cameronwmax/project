import pygame

class Finish:
    """Class to manage the finish area"""
    def __init__(self, cc_game):
        """Initialize the finish area and set its position"""
        self.screen = cc_game.screen
        self.screen_rect = cc_game.screen.get_rect()

        # Load the image for the finish area
        self.image = pygame.image.load("images\crown\crowns.png")
        
        self.rect = self.image.get_rect()

        # Set position for finish area
        self.rect.x = 1100
        self.rect.y = 400

    def blitme(self):
        """Draw the finish area at its position"""
        self.screen.blit(self.image, self.rect)