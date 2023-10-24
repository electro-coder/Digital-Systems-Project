import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
DROPZONE_COLOR = (0, 255, 0)
IMAGE_SIZE = (50, 50)

# Create the display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Drag and Drop")

image1 = pygame.image.load("../Resources/or.png")  # Replace with your image file
image2 = pygame.image.load("../Resources/and.png")  # Replace with your image file
image3 = pygame.image.load("../Resources/nor.png")  # Replace with your image file
image4 = pygame.image.load("../Resources/xor.png")  # Replace with your image file
image5 = pygame.image.load("../Resources/nor.png")  # Replace with your image file
image6 = pygame.image.load("../Resources/nor.png")  # Replace with your image file

# Initial positions of images
image1_rect = image1.get_rect(topleft=(50, 25))
image2_rect = image2.get_rect(topleft=(140, 25))
image3_rect = image3.get_rect(topleft=(230, 25))
image4_rect = image4.get_rect(topleft=(350, 25))
image5_rect = image5.get_rect(topleft=(460, 25))
image6_rect = image6.get_rect(topleft=(590, 25))

# Original positions of images
image1_original_rect = image1_rect.copy()
image2_original_rect = image2_rect.copy()
image3_original_rect = image3_rect.copy()
image4_original_rect = image4_rect.copy()
image5_original_rect = image5_rect.copy()
image6_original_rect = image6_rect.copy()

# Create drop zones
dropzone_rect1 = pygame.Rect(700, 250, 70, 70)
dropzone_rect2 = pygame.Rect(500, 250, 70, 70)
dropzone_rect3 = pygame.Rect(500, 400, 70, 70)
dropzone_rect4 = pygame.Rect(500, 100, 70, 70)
dropzone_rect5 = pygame.Rect(200, 200, 70, 70)
dropzone_rect6 = pygame.Rect(200, 300, 70, 70)

# List of images, their original positions, and flags for indicating if they are in a drop zone
images = [(image1, image1_rect, False),
          (image2, image2_rect, False),
          (image3, image3_rect, False),
          (image4, image4_rect, False),
          (image5, image5_rect, False),
          (image6, image6_rect, False)]

# Dictionary to keep track of which image is in which drop zone
dropzone_contents = {tuple(dropzone_rect1.topleft): None,
                    tuple(dropzone_rect2.topleft): None,
                    tuple(dropzone_rect3.topleft): None,
                    tuple(dropzone_rect4.topleft): None,
                    tuple(dropzone_rect5.topleft): None,
                    tuple(dropzone_rect6.topleft): None}

dragging = None

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
                        dragging = img, img_rect, in_dropzone
                        images.remove((img, img_rect, in_dropzone))
        if event.type == pygame.MOUSEMOTION:
            if dragging is not None:
                _, img_rect, _ = dragging
                img_rect.topleft = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if dragging is not None:
                img, img_rect, in_dropzone = dragging
                drop_zones = [dropzone_rect1, dropzone_rect2, dropzone_rect3, dropzone_rect4, dropzone_rect5, dropzone_rect6]

                # Check if any of the drop zones is empty, and drop the image if one is
                for i, dropzone_rect in enumerate(drop_zones):
                    if dropzone_rect.colliderect(img_rect):
                        if dropzone_contents[tuple(dropzone_rect.topleft)] is None:
                            img_rect.topleft = dropzone_rect.topleft
                            in_dropzone = True
                            dropzone_contents[tuple(dropzone_rect.topleft)] = img
                            print(f"{img} was dropped in Zone {i + 1}")
                            break
                else:
                    # Return the image to its original position if no drop zone is available
                    img_rect.topleft = image1_original_rect.topleft
                images.append((img, img_rect, in_dropzone))
                dragging = None

    # Clear the screen
    screen.fill(WHITE)

    # Draw drop zones
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect1)
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect2)
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect3)
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect4)
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect5)
    pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect6)

    # Draw the images
    for img, img_rect, in_dropzone in images:
        screen.blit(img, img_rect)
        if in_dropzone:
            pygame.draw.rect(screen, DROPZONE_COLOR, img_rect, 2)  # Add a border to indicate in the drop zone

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
