import pygame
import sys
import random

class start_screen:
    def __init__(self, screen):

        #Initialize pygame
        pygame.init()

        #Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse")