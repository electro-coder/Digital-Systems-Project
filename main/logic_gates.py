import pygame
import sys

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AND Gate Simulation")

# Define the AND gate class
class ANDGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = input1 and input2

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
        pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.output = input1 and input2

class NANDGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 and input2)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
        pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 and input2)

class ORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = input1 or input2

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
        pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.output = input1 or input2

class NORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = not(input1 or input2)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
        pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.output = not(input1 or input2)

class NOTGate:
    def __init__(self, x=150, y=80, input1=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = not input1

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
        pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.output = not input1

class XORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = input1 ^ input2

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
        pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.output = input1 ^ input2

class XNORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 ^ input2)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
        pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
        pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
        pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 ^ input2) 

# Create AND gate instances with overloaded constructors
and_gate1 = ANDGate()  # Uses default values (x=150, y=80, input1=False, input2=False)
and_gate2 = ANDGate(50, 30, True, True)  # Custom values (x=50, y=30, input1=True, input2=True)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the AND gates
    and_gate1.draw()
    and_gate2.draw()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
