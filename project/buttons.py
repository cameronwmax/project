import pygame.font

class Button:
    """Class to build buttons for the game"""

    def __init__(self, cc_game, msg):
        """Initialize button attributes"""
        self.screen = cc_game.screen
        self.screen_rect = self.screen.get_rect()


        # Set dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message only needs to be prepped once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into rendered image and center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blank button, then draw the message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)