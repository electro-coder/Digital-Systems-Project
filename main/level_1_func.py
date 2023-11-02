import pygame
import sys
import random
from logic_gates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate, XNORGate

class level_1_up:
    def __init__(self, screen):
        def __init__(self,screen):

        #initialize Pygame
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse Level 1")

    def run_level(self):
         WHITE = (255, 255, 255)
        DROPZONE_COLOR = (0, 255, 0)
        IMAGE_SIZE = (50, 50)
        CIRCLE_COLOR_ON = (255, 255, 0)
        CIRCLE_COLOR_OFF=(255,255,255)
        CIRCLE_RADIUS=30
        num_leds=4
    
        path_or="../Resources/or.png"
        path_and="../Resources/and.png"
        path_nor="../Resources/nor.png"
        path_xor="../Resources/xor.png"
        path_nand="../Resources/nand.png"
        path_xnor="../Resources/xnor.png"
    
        try:
            image1 = pygame.image.load(path_or)  # Replace with your image file
            image2 = pygame.image.load(path_nor)  # Replace with your image file
            image3 = pygame.image.load(path_and)  # Replace with your image file
            image4 = pygame.image.load(path_nand)  # Replace with your image file
            image5 = pygame.image.load(path_xor)  # Replace with your image file
            image6 = pygame.image.load(path_xnor)  # Replace with your image file
        except(FileNotFoundError):
            image1 = pygame.image.load(path1.replace("..","."))  # Replace with your image file
            image2 = pygame.image.load(path2.replace("..","."))  # Replace with your image file
            image3 = pygame.image.load(path3.replace("..","."))  # Replace with your image file
            image4 = pygame.image.load(path4.replace("..","."))  # Replace with your image file
            image5 = pygame.image.load(path5.replace("..","."))  # Replace with your image file
            image6 = pygame.image.load(path6.replace("..","."))  # Replace with your image file

        image1_rect = image1.get_rect(topleft=(50, 25))
        image2_rect = image2.get_rect(topleft=(140, 25))
        image3_rect = image3.get_rect(topleft=(230, 25))
        image4_rect = image4.get_rect(topleft=(350, 25))
        image5_rect = image5.get_rect(topleft=(460, 25))
        image6_rect = image6.get_rect(topleft=(590, 25))

    
    