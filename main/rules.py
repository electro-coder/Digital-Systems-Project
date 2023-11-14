import pygame
import sys
from level_1_func import level_1
from level_2_func import level_2
from level_3 import level_3
from main_start_screen import StartScreen

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
START_SCREEN_COLOR = (0, 0, 0)
LEVEL_WIN_COLOR = (0, 255, 0)
FONT_SIZE = 36

class rules:
    def __init__(self,screen):
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("RULES")

        path_background="../Resources/background3.png"

        try:
            self.background=pygame.image.load(path_background)
        except(FileNotFoundError):
            self.background=pygame.image.load(path_background.replace("..","."))

        self.background = pygame.transform.scale(self.background, (800, 600))

    def display_rules(self):
        self.screen.blit(self.background, (0, 0))
        y=120
        rules=[
            "CODEDIFFUSE",
            "RULES",
            "1. A sequence of leds would be given which are essentially the responses to x,y", 
            "states of (0,0),(0,1),(1,0),(1,1).",
            "2. You have to understand and formulate the function in term of minterms only.",
            "3. Then, drag and drop gates at appropriate places and join the wires", 
            "to produce the function on simulation.",
            "4. Red and white leds would simulate the output you are producing." ,
            "Make sure to check your answer before submitting.",
            "5. You have a maximum of 5 tries to complete a level",
            "6. Make Sure to have fun and contact developers if you face any issue",
            '7. Press W to start the game'
        ]

        try:
            font = pygame.font.Font("Resources/text/Chakra_Petch/ChakraPetch-SemiBold.ttf", 20)
        except(FileNotFoundError):
            font=pygame.font.Font("Resources/text/Chakra_Petch/ChakraPetch-SemiBold.ttf".replace("..","."),20)

        #font = pygame.font.Font("Resources/text/Chakra_Petch/ChakraPetch-SemiBold.ttf", 20)
        for rule in rules:
            text=font.render(rule, True, (255,165,0))
            text_rect=text.get_rect(center=(WINDOW_WIDTH//2,y))
            self.screen.blit(text,text_rect)
            y+=30
        pygame.display.flip()

    def run_level(self):
        self.display_rules()
        running=True
        while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        running=False
                        return True
                    
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    rules_page=rules(screen)
    rules_page.run_level()