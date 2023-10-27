import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
DROPZONE_COLOR = (0, 255, 0)
IMAGE_SIZE = (50, 50)
# WHITE = (255, 255, 255)
CIRCLE_COLOR = (255, 0, 0)
CIRCLE_RADIUS = 50
# connections = [((20,20),(60,60)),((270, 300), (300, 300)),((200,320), (270,320)),((270, 450), (270, 160)),((248, 420),
#                (300, 420)),((270, 450), (270, 160)),((200,320), (270,320)),((270, 300), (300, 300)),((246, 200), (300, 200))]

# Create the display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CodeDiffuse")

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
dropzone_rect1 = pygame.Rect(500, 250, 70, 70)
dropzone_rect2 = pygame.Rect(300, 250, 70, 70)
dropzone_rect3 = pygame.Rect(300, 400, 70, 70)
dropzone_rect4 = pygame.Rect(300, 100, 70, 70)
dropzone_rect5 = pygame.Rect(150, 200, 70, 70)
dropzone_rect6 = pygame.Rect(150, 300, 70, 70)

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

clock = pygame.time.Clock()
blink_interval = 500  # milliseconds
blink_timer = 0
visible = True
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
    screen.fill((128, 28, 128))


    current_time = pygame.time.get_ticks()
    if current_time - blink_timer >= blink_interval:
        visible = not visible
        blink_timer = current_time

    if visible:
        # Draw the circle if it's currently visible
        pygame.draw.circle(screen, CIRCLE_COLOR, (750, 300), 10)

    # for start, end in connections:
    #     pygame.draw.line(screen, (255, 0, 0), start, end, 5)
    pygame.draw.line(screen, (254, 20, 50), (200,220), (250,220), 5)
    pygame.draw.line(screen, (254, 20, 50), (250, 420), (250, 120), 5)
    pygame.draw.line(screen, (254, 20, 50), (248, 120), (300, 120), 5)
    pygame.draw.line(screen, (254, 20, 50), (248, 270), (300, 270), 5)
    pygame.draw.line(screen, (254, 20, 50), (248, 420), (300, 420), 5)
    pygame.draw.line(screen, (0, 0, 0), (270, 450), (270, 150), 5)
    pygame.draw.line(screen, (0, 0, 0), (200,320), (270,320), 5)
    pygame.draw.line(screen, (0, 0, 0), (270, 300), (300, 300), 5)
    pygame.draw.line(screen, (0, 0, 0), (268, 150), (300, 150), 5)
    pygame.draw.line(screen, (0, 0, 0), (268, 450), (300, 450), 5)
    pygame.draw.line(screen, (0, 34, 45), (350, 285), (500, 285), 5)
    pygame.draw.line(screen, (0, 34, 45), (350, 130), (530, 130), 5)
    pygame.draw.line(screen, (0, 34, 45), (350, 430), (530, 430), 5)
    pygame.draw.line(screen, (0, 34, 45), (530, 129), (530, 300), 5)
    pygame.draw.line(screen, (0, 34, 45), (530, 430), (530, 310), 5)

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

    clock.tick(60)
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()