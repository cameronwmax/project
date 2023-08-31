import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from character import Character
from cars import *
from buttons import Button
from finish import Finish
from scoreboard import Scoreboard


class ChickenCross:
    """Overall class to manage the game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create its resources"""
        pygame.init()
        self.cock = pygame.time.Clock()
        self.settings = Settings()
        self.game_active = False

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("ChickenCross")

        # Make the play button
        self.play_button = Button(self, "Play")
        
        # Create an instance to store game stats
        #   and create scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.character = Character(self)
        self.cars = pygame.sprite.Group()
        self.finish = Finish(self)

        self._create_cars()



    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            
            
            if self.game_active:
                self.character.update()
                self._update_level()
                self._update_cars()
                
            
            self._update_screen()
            self.cock.tick(60)
            
    def _check_events(self):
        """Respond to keypresses and mouse movements"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                   self._check_keydown(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_button(mouse_pos)

    def _check_button(self, mouse_pos):
        """Start a new game when Play button is clicked"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.game_active = True
            self.sb.prep_level()
            self.sb.prep_lives()

            # clear cars
            self.cars.empty()

            # Reset cars and reset character position
            self._create_cars()
            self.character.reset()

            # Hide mouse cursor while game active
            pygame.mouse.set_visible(False)        

    def _check_keydown(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.character.moving_left = True
        elif event.key == pygame.K_UP:
            self.character.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.character.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.character.moving_left = False
        elif event.key == pygame.K_UP:
            self.character.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.character.moving_down = False

    def _create_cars(self):
        """Create cars"""
        # Make a car
        car = Car(self)
        self.cars.add(car)
        
        car1 = Car1(self)
        self.cars.add(car1)

        car2 = Car2(self)
        self.cars.add(car2)

        car3 = Car3(self)
        self.cars.add(car3)

        car4 = Car4(self)
        self.cars.add(car4)

        car5 = Car5(self)
        self.cars.add(car5)
        
        car6 = Car6(self)
        self.cars.add(car6)

        car7 = Car7(self)
        self.cars.add(car7)
        

    def _update_cars(self):
        """Update the postition of all the cars"""
        self.cars.update()
        if pygame.sprite.spritecollideany(self.character, self.cars):
            self._chicken_hit()

    def _update_level(self):
        """Update the level"""
        if self.character.rect.colliderect(self.finish.rect):
            self.character.reset()
            self.cars.empty()
            self._create_cars()
            self.settings.increase_speed()

            sleep(0.5)

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()
            self.sb.check_highest_level()

    def _chicken_hit(self):
        """React to the chicken being hit by car"""
        if self.stats.chickens_left > 0:
            # Decrement chickes left
            self.stats.chickens_left -= 1
            self.sb.prep_lives()

            self.cars.empty()

            # Create new cars
            self._create_cars()
            self.character.reset()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.background, (0, 0))
        self.character.blitme()
        self.finish.blitme()
        self.cars.draw(self.screen)

        self.sb.show_score()

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    cc = ChickenCross()
    cc.run_game()