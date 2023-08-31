import pygame
from pygame.sprite import Sprite

class Car(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images/cars_down/b_car.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 220
        self.rect.y = -50

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)
        

    def update(self):
        """Move the car"""
        self.y += self.settings.car_speed
        self.rect.y = self.y
        if self.y > 800:
            self.y = -50


class Car1(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images\cars_down\g_car.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 300
        self.rect.y = -50

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the car"""
        self.y += self.settings.car_speed1
        self.rect.y = self.y
        if self.y > 800:
            self.y = -50


class Car2(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images/cars_down/r_car.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 700
        self.rect.y = -50

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the car"""
        self.y += self.settings.car_speed2
        self.rect.y = self.y
        if self.y > 800:
            self.y = -50


class Car3(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images\cars_down\w_car.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 780
        self.rect.y = -50

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the car"""
        self.y += self.settings.car_speed3
        self.rect.y = self.y
        if self.y > 800:
            self.y = -50


class Car4(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images/cars_up/r_car1.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 400
        self.rect.y = 800

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the car"""
        self.y -= self.settings.car_speed4
        self.rect.y = self.y
        if self.y < -50:
            self.y = 800


class Car5(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images\cars_up\w_car1.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 470
        self.rect.y = 800

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the car"""
        self.y -= self.settings.car_speed5
        self.rect.y = self.y
        if self.y < -50:
            self.y = 800

class Car6(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images\cars_up\g_car3.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 880
        self.rect.y = 800

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the car"""
        self.y -= self.settings.car_speed6
        self.rect.y = self.y
        if self.y < -50:
            self.y = 800

class Car7(Sprite):
    """Class to manage a single car"""
    
    def __init__(self, cc_game):
        """Initialize the car and set its start point"""
        super().__init__()
        self.screen = cc_game.screen
        self.settings = cc_game.settings

        # Load the car image and set its rect attribute
        self.image = pygame.image.load("images/cars_up/b_car2.png")
        self.rect = self.image.get_rect()
        

        # Start car near top left of the screen
        self.rect.x = 960
        self.rect.y = 800

        # Store the cars exact horizontal position
        self.y = float(self.rect.y)

    def update(self):
        """Move the car"""
        self.y -= self.settings.car_speed7
        self.rect.y = self.y
        if self.y < -50:
            self.y = 800