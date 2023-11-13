import pygame
import sys
from level_1_func import level_1
from level_2 import level_2
from level_3 import level_3
from main_start_screen import StartScreen

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
START_SCREEN_COLOR = (0, 0, 0)
LEVEL_WIN_COLOR = (0, 255, 0)
FONT_SIZE = 36

class Manager:
    def __init__(self,screen):
        self.screen=screen
        self.current_state="start_screen"
        self.start_screen=StartScreen(800,600)

    def display_rules(self):
        screen.fill((255,255,0))
        y=100
        rules=[
            'CODEDIFFUSE',
            'RULES',
            'Press W to start the game'
        ]
        for rule in rules:
            text=font.render(rule, True, (0,0,0))
            text_rect=text.get_rect(center=(WINDOW_WIDTH//2,y))
            screen.blit(text,text_rect)
            y+=40
        pygame.display.flip()

    def run_game(self):

        # Rules Page
        self.display_rules()
        waiting=True
        while waiting:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    waiting=False
        font = pygame.font.Font("freesansbold.ttf", 36)
        # Main loop
        try:
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                # Clear the screen
                if self.current_state == "start_screen":
                    # screen.fill(START_SCREEN_COLOR)
                    # start_text = font.render("Press Space to Start", True, LEVEL_WIN_COLOR)
                    # text_rect = start_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                    # screen.blit(start_text, text_rect)
                    result=self.start_screen.run()

                    #keys = pygame.key.get_pressed()
                    #if keys[pygame.K_SPACE]:
                    if result:
                        self.current_state = "level_1"

                elif self.current_state == "level_1":
                    self.level1=level_1(self.screen)
                    level_result = self.level1.run_level()

                    if level_result == True:
                        self.current_state = "level_3"
                    elif level_result == False:
                        self.current_state = "game_over"

                elif self.current_state == "level_2":
                    self.level2=level_2(self.screen)
                    level_result = self.level2.run_level()
                    if level_result == True:
                        self.current_state = "level_3"
                    elif level_result == False:
                        self.current_state = "game_over"

                elif self.current_state=="level_3":
                    self.level3=level_3(self.screen)
                    level_result=self.level3.run_level()
                    if level_result:
                        self.current_state=True
                    else:
                        self.current_state="game_over"

                elif self.current_state == True:
                    screen.fill(LEVEL_WIN_COLOR)
                    win_text = font.render("You Won!", True, START_SCREEN_COLOR)
                    text_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                    screen.blit(win_text, text_rect)

                elif self.current_state == "game_over":
                    screen.fill(LEVEL_WIN_COLOR)
                    game_over_text = font.render("Game Over", True, START_SCREEN_COLOR)
                    text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                    screen.blit(game_over_text, text_rect)

                pygame.display.flip()

        except FileNotFoundError:
            font = pygame.font.Font("freesansbold.ttf", 20)
            error_text = font.render(f"Sorry, we couldn't locate the path of a file !", True, (255, 0, 0))
            error_rect = error_text.get_rect(center=(400,300))
            self.screen.blit(error_text, error_rect)
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False

        except Exception as e:
            font = pygame.font.Font('freesansbold.ttf', 20)
            error_text = font.render(f"An Unexpected error: {e} has occured. Please restart the game!", True, (255, 0, 0))
            error_rect = error_text.get_rect(center=(400,300))
            self.screen.blit(error_text, error_rect)
            print(e)
            pygame.display.flip()
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        waiting = False

        # Quit Pygame
        pygame.quit()
        sys.exit()

if __name__=="__main__":
    pygame.init()
    # Initialize the window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("CodeDiffuse")

    # Create a font
    font = pygame.font.Font(None, FONT_SIZE)
    game_manager=Manager(screen)
    game_manager.run_game()
