import pygame
from pygame.sprite import Sprite

class Character(Sprite):
    """A class to manage the character"""

    def __init__(self, cc_game):
        """Initialize the character and set its starting point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings
        self.screen_rect = cc_game.screen.get_rect()

        # Load the characters image and get its rect
        self.image = pygame.image.load("images/chicken/front.png")
    
        self.rect = self.image.get_rect()

        # Start each new life at the middle left side of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the characters exact x and y position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags; start with the character not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the characters position based on the movement flag"""
        # Update the characters x and y value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.image = pygame.image.load("images/chicken/right2.png")
            self.x += self.settings.character_speed
        if self.moving_left and self.rect.left > 0:
            self.image = pygame.image.load("images\chicken\left2.png")
            self.x -= self.settings.character_speed
        if self.moving_up and self.rect.top > 0:
            self.image = pygame.image.load("images/chicken/back2.png")
            self.y -= self.settings.character_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.image = pygame.image.load("images/chicken/front1.png")
            self.y += self.settings.character_speed
        
        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def reset(self):
        """Reset the character on screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)        

    def blitme(self):
        """Draw the character at its current location"""
        self.screen.blit(self.image, self.rect)