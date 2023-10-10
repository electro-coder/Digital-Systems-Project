import pygame
import sys
import random
import os
pygame.init()

# Constants
window_width = 400
window_height = 500
led_radius = 20
led_spacing = 10
led_color_on = (255, 255, 0)
led_color_off = (50, 50, 50)
update_interval = 1000
button_width = 100
button_height = 50
button_color = (0, 255, 0)
button_text_color = (255, 255, 255)
font_size = 24
button_txt = "Start Game"

# Initialize
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("CodeDefuse")
num_leds = 8
led_states = [False]*num_leds
last_update_time = pygame.time.get_ticks()  # update state
font = pygame.font.Font(None, font_size)

# Start Menu button
button_rect = pygame.Rect(
    (window_width - button_width) // 2,
    (window_height - button_height) // 2,
    button_width,
    button_height,
)
#trial game
main_menu = True
game_started = False
while main_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_menu = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
            if button_rect.collidepoint(event.pos):
                game_started = True

    screen.fill((0, 0, 0))

    if not game_started:
        pygame.draw.rect(screen, button_color, button_rect)
        button_text = font.render(button_txt, True, button_text_color)
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)
    else:
        current_time = pygame.time.get_ticks()
        if current_time - last_update_time >= update_interval:
            led_states = [random.choice([True, False]) for _ in range(num_leds)]
            for i in led_states:
                print(int(i), end=' ')
            print()
            last_update_time = current_time
        for i, led_on in enumerate(led_states):
            led_x = window_width // 2
            led_y = i * (led_radius * 2 + led_spacing) + led_radius + led_spacing
            color = led_color_on if led_on else led_color_off
            pygame.draw.circle(screen, color, (led_x, led_y), led_radius)
    pygame.display.flip()

pygame.quit()
sys.exit()
