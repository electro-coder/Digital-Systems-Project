import pygame
import sys
import random

class level_2:
    def __init__(self,screen):

        #initialize Pygame
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse Level 2")

    def run_level(self):

        # Game Logic to be added here


# Testing of Level-2
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    level2=level_2(screen)
    level2.run_level()
    pygame.quit()