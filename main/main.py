import pygame
import sys
from level_1 import level_1
from level_2 import level_2
#import level_3

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
        self.level1=level_1(self.screen)
        self.level2=level_2(self.screen)

    def run_game(self):
        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen
            if self.current_state == "start_screen":
                screen.fill(START_SCREEN_COLOR)
                start_text = font.render("Press Space to Start", True, LEVEL_WIN_COLOR)
                text_rect = start_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                screen.blit(start_text, text_rect)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.current_state = "level_1"

            elif self.current_state == "level_1":
                level_result = self.level1.run_level()

                if level_result == True:
                    self.current_state = "level_2"
                elif level_result == False:
                    self.current_state = "game_over"

            elif self.current_state == "level_2":
                level_result = self.level2.run_level()

                if level_result == True:
                    self.current_state = True
                elif level_result == False:
                    self.current_state = "game_over"

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
