import pygame
import sys
import random

class level_3:
    def __init__(self,screen):

        #initialize Pygame
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse Level 3")

    def run_level(self):

        # Game Logic to be added here


# Testing of Level-3
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    level3=level_3(screen)
    level3.run_level()
    pygame.quit()