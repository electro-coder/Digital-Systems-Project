import pygame
import sys

# Define colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# WIDTH, HEIGHT = 400, 200
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Logic Gates")

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

    #constructor overloaded for flexibility in no. of inputs
    def __init__(self, x=150, y=80, z=90, input1=False, input2=False, input3=False):
        self.x = x
        self.y = y
        self.z=z
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.input3=input3
        self.output = input1 and input2 and input3

    # def draw(self):
    #     pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    #     pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self,x=150, y=80, input1=None, input2=None, input3=None):
        self.input1 = input1
        self.input2 = input2
        self.output = input1 and input2
        if (input3!=None): self.output=input1 and input2 and input3
        return self.output
    
    # def set_input(self,input1,input2,input3):
    #     self.input1=input1
    #     self.input2=input2
    #     self.input3=input3
    #     self.output= input1 and input2 and input3

class NANDGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 and input2)

    #constructor overloaded for flexibility in no. of inputs
    def __init__(self, x=150, y=80, z=90, input1=False, input2=False, input3=False):
        self.x = x
        self.y = y
        self.z=z
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.input3=input3
        self.output = not(input1 and input2 and input3)

    # def draw(self):
    #     pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    #     pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self,x=150, y=80, input1=None, input2=None, input3=None):
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 and input2)
        if (input3!=None): self.output=not(input1 and input2 and input3)
        return self.output
    
    # def set_input(self,input1,input2,input3):
    #     self.input1=input1
    #     self.input2=input2
    #     self.input3=input3
    #     self.output= not(input1 and input2 and input3)

class ORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = input1 or input2

    #constructor overloaded for flexibility in no. of inputs
    def __init__(self, x=150, y=80, z=90, input1=False, input2=False, input3=False):
        self.x = x
        self.y = y
        self.z=z
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.input3=input3
        self.output = input1 or input2 or input3

    # def draw(self):
    #     pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    #     pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self,x=150, y=80, input1=None, input2=None, input3=None):
        self.input1 = input1
        self.input2 = input2
        self.output = input1 or input2
        if (input3!=None): self.output=input1 or input2 or input3
        return self.output
    
    # def set_input(self,input1,input2,input3):
    #     self.input1=input1
    #     self.input2=input2
    #     self.input3=input3
    #     self.output= input1 or input2 or input3

class NORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = not(input1 or input2)

    #constructor overloaded for flexibility in no. of inputs
    def __init__(self, x=150, y=80, z=90, input1=False, input2=False, input3=False):
        self.x = x
        self.y = y
        self.z=z
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.input3=input3
        self.output = not(input1 or input2 or input3)

    # def draw(self):
    #     pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    #     pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self,x=150, y=80, input1=None, input2=None, input3=None):
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 or input2)
        if (input3!=None): self.output=not(input1 or input2 or input3)
        return self.output
    
    # def set_input(self,input1,input2,input3):
    #     self.input1=input1
    #     self.input2=input2
    #     self.input3=input3
    #     self.output= not(input1 or input2 or input3)

class NOTGate:
    def __init__(self, x=150, y=80, input1=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = not input1

    # def draw(self):
    #     pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    #     pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self, input1, input2):
        self.input1 = input1
        self.output = not input1
        return self.output

class XORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = input1 ^ input2

    #constructor overloaded for flexibility in no. of inputs
    def __init__(self, x=150, y=80, z=90, input1=False, input2=False, input3=False):
        self.x = x
        self.y = y
        self.z=z
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.input3=input3
        self.output = input1 ^ input2 ^ input3

    # def draw(self):
    #     pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    #     pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self,x=150, y=80, input1=None, input2=None, input3=None):
        self.input1 = input1
        self.input2 = input2
        self.output = input1 ^ input2
        if (input3!=None): self.output=input1 ^ input2 ^ input3
        return self.output
    
    # def set_input(self,input1,input2,input3):
    #     self.input1=input1
    #     self.input2=input2
    #     self.input3=input3
    #     self.output=input1 ^ input2 ^ input3

class XNORGate:
    def __init__(self, x=150, y=80, input1=False, input2=False):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 ^ input2)

    #constructor overloaded for flexibility in no. of inputs
    def __init__(self, x=150, y=80, z=90, input1=False, input2=False, input3=False):
        self.x = x
        self.y = y
        self.z=z
        self.width = 50
        self.height = 40
        self.input1 = input1
        self.input2 = input2
        self.input3=input3
        self.output = not(input1 ^ input2 ^ input3)

    # def draw(self):
    #     pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))
    #     pygame.draw.line(screen, BLACK, (self.x, self.y + self.height // 2), (self.x + self.width, self.y + self.height // 2))
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x - 20, self.y + self.height // 2 + 40), 6)
    #     pygame.draw.circle(screen, BLACK, (self.x + self.width + 20, self.y + self.height // 2), 6)

    def set_input(self,x=150, y=80, input1=None, input2=None, input3=None):
        self.input1 = input1
        self.input2 = input2
        self.output = not (input1 ^ input2)
        if (input3!=None): self.output=not(input1 ^ input2 ^ input3)
        return self.output
    
    # def set_input(self,input1,input2,input3):
    #     self.input1=input1
    #     self.input2=input2
    #     self.input3=input3
    #     self.output= not(input1 ^ input2 ^ input3)

# Create AND gate instances with overloaded constructors
# and_gate1 = ANDGate()  # Uses default values (x=150, y=80, input1=False, input2=False)
# and_gate2 = ANDGate(50, 30, True, True)  # Custom values (x=50, y=30, input1=True, input2=True)
# or_gate=ORGate()
# nor_gate=NORGate()
# nand_gate=NANDGate()
# not_gate=NOTGate()
# xor_gate=XORGate()
# xnor_gate=XNORGate()

# Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             pygame.quit()
#             sys.exit()

#     # Clear the screen
#     #screen.fill(BLACK)

#     # Draw the AND gates
#     #and_gate1.draw()
#     #and_gate2.draw()
#     '''or_gate.draw()
#     not_gate.draw()
#     nor_gate.draw()
#     nand_gate.draw()
#     xor_gate.draw()'''
#     xnor_gate.draw()

#     # Update the display
#     pygame.display.update()

# Quit Pygame
#pygame.quit()
