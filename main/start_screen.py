import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
ELEMENTS = ["AND", "OR", "NOR"]
ELEMENT_FONT = pygame.font.Font(None, 16)
ELEMENT_TEXT_COLOR = (255, 255, 255)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
DROPZONE_COLOR = (50, 100, 10)
IMAGE_SIZE = (50, 50)

# Create the display surface
screen = pygame.display.set_gitmode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Drag and Drop")

# Load images
image1 = pygame.image.load("../Resources/or.png")  # Replace with your image file
image2 = pygame.image.load("../Resources/and.png")  # Replace with your image file
image3 = pygame.image.load("../Resources/or.png")  # Replace with your image file

# Initial positions of images
image1_rect = image1.get_rect(topleft=(70, 70))
image2_rect = image2.get_rect(topleft=(160, 70))
image3_rect = image3.get_rect(topleft=(250, 70))

# Drop zone rect
dropzone_rect = pygame.Rect(700, 250, 70, 70)
dropzone_rect1 = pygame.Rect(600, 250, 70, 70)
dropzone_rect2 = pygame.Rect(700, 250, 70, 70)

# List of images, their original positions, and a flag for indicating if they are in the drop zone
images = [(image1, image1_rect, False), (image2, image2_rect, False), (image3, image3_rect, False)]

dragging = None
currently_dropped = None  # Track the currently dropped image

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for img, img_rect, in_dropzone in images:
                    if img_rect.collidepoint(event.pos) and not in_dropzone:
                        if currently_dropped:
                            # Return the prior image to its original position
                            prior_img, prior_rect, _ = currently_dropped
                            prior_rect.topleft = prior_rect.x, 70
                            images.append((prior_img, prior_rect, False))
                        currently_dropped = (img, img_rect, in_dropzone)
                        dragging = img, img_rect, in_dropzone
                        images.remove((img, img_rect, in_dropzone))
        if event.type == pygame.MOUSEMOTION:
            if dragging is not None:
                _, img_rect, _ = dragging
                img_rect.topleft = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if dragging is not None:
                img, img_rect, in_dropzone = dragging
                if dropzone_rect.colliderect(img_rect):
                    # The image is dropped inside the drop zone
                    img_rect.topleft = dropzone_rect.topleft
                    in_dropzone = True
                if dropzone_rect1.colliderect(img_rect):
                    # The image is dropped inside the drop zone
                    img_rect.topleft = dropzone_rect1.topleft
                    in_dropzone = True
                else:
                    # The image is dropped outside the drop zone
                    img_rect.topleft = img_rect.x, 70  # Return to original position
                images.append((img, img_rect, in_dropzone))
                dragging = None

    # Clear the screen
    screen.fill(WHITE)

    # Draw drop zone
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect)
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect1)

    # Draw the images
    for img, img_rect, in_dropzone in images:
        screen.blit(img, img_rect)
        if in_dropzone:
            pygame.draw.rect(screen, DROPZONE_COLOR, img_rect, 2)  # Add a border to indicate in drop zone

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
