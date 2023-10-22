import pygame
import sys

class Gate:
    def __init__(self, screen, gate_type, position, input1=False, input2=False):
        self.screen = screen
        self.gate_type = gate_type
        self.position = position
        self.input1 = input1
        self.input2 = input2
        self.output = False

        # Define gate colors and dimensions
        self.color = (255, 255, 255)
        self.width = 60
        self.height = 40

    def draw(self):
        x, y = self.position
        pygame.draw.rect(self.screen, self.color, (x, y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        gate_text = font.render(self.gate_type, True, (0, 0, 0))
        self.screen.blit(gate_text, (x + 10, y + 5))

    def update(self):
        if self.gate_type == "AND":
            self.output = self.input1 and self.input2
        elif self.gate_type == "OR":
            self.output = self.input1 or self.input2
        elif self.gate_type == "NOT":
            self.output = not self.input1

    def set_inputs(self, input1, input2=None):
        self.input1 = input1
        if input2 is not None:
            self.input2 = input2

    def get_output(self):
        return self.output

# Initialize Pygame
pygame.init()

# Define screen dimensions and create a Pygame screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gate Structures in Pygame")

# Create gate objects
and_gate = Gate(screen, "AND", (50, 50))
or_gate = Gate(screen, "OR", (200, 50))
not_gate = Gate(screen, "NOT", (350, 50))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update gate outputs
    and_gate.update()
    or_gate.update()
    not_gate.update()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw gates
    and_gate.draw()
    or_gate.draw()
    not_gate.draw()

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
