import pygame
import sys
from level_1 import level_1
#import level_2
#import level_3

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
START_SCREEN_COLOR = (0, 0, 0)
LEVEL_WIN_COLOR = (0, 255, 0)
FONT_SIZE = 36

# Initialize the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("CodeDiffuse")

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

# Game states
START_SCREEN = "start_screen"
LEVEL_1 = "level_1"
LEVEL_2 = "level_2"
LEVEL_3 = "level_3"
GAME_OVER = "game_over"
WIN = "win"

# Initialize the game state
current_state = START_SCREEN

# Instantiation of levels
level1=level_1(screen)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    if current_state == START_SCREEN:
        screen.fill(START_SCREEN_COLOR)
        start_text = font.render("Press Space to Start", True, LEVEL_WIN_COLOR)
        text_rect = start_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(start_text, text_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            current_state = LEVEL_1

    elif current_state == LEVEL_1:
        level_result = level1.run_level()

        if level_result == True:
            current_state = True
        elif level_result == False:
            current_state = GAME_OVER

    elif current_state == True:
        screen.fill(LEVEL_WIN_COLOR)
        win_text = font.render("You Won!", True, START_SCREEN_COLOR)
        text_rect = win_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(win_text, text_rect)

    elif current_state == GAME_OVER:
        screen.fill(LEVEL_WIN_COLOR)
        game_over_text = font.render("Game Over", True, START_SCREEN_COLOR)
        text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        screen.blit(game_over_text, text_rect)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
