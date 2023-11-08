import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
DROPZONE_COLOR = (0, 255, 0)

# Create the display surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Image Drag and Drop")

# Load images (replace with your image files)
image1 = pygame.image.load("../Resources/and.png")
image2 = pygame.image.load("../Resources/and.png")
image3 = pygame.image.load("../Resources/and.png")

# Initial positions of images
image1_rect = image1.get_rect(topleft=(100, 100))
image2_rect = image2.get_rect(topleft=(200, 100))
image3_rect = image3.get_rect(topleft=(300, 100))

# Create drop zones (as tuples of (left, top, width, height))
dropzone_rect1 = (100, 400, 100, 100)
dropzone_rect2 = (250, 400, 100, 100)
dropzone_rect3 = (400, 400, 100, 100)

# List of images and their original positions
images = [
    (image1, image1_rect, False),
    (image2, image2_rect, False),
    (image3, image3_rect, False)
]

# Dictionary to keep track of which image is in which drop zone
dropzone_contents = {dropzone_rect1: None, dropzone_rect2: None, dropzone_rect3: None}

dragging = None

# Function to add a new instance of an image at its original position
def add_new_instance(image_info):
    img, img_rect, _ = image_info
    new_img = img.copy()  # Create a copy of the image
    new_img_rect = new_img.get_rect(topleft=img_rect.topleft)  # Set its position to the original position
    images.append((new_img, new_img_rect, False))  # Add the new image to the list

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for i, (img, img_rect, _) in enumerate(images):
                    if img_rect.collidepoint(event.pos):
                        dragging = i
                        offset_x, offset_y = img_rect.x - event.pos[0], img_rect.y - event.pos[1]
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging is not None:
                img, img_rect, in_dropzone = images[dragging]
                for dropzone_rect, content in dropzone_contents.items():
                    rect = pygame.Rect(*dropzone_rect)
                    if rect.collidepoint(event.pos) and content is None:
                        img_rect.topleft = rect.topleft
                        in_dropzone = True
                        dropzone_contents[dropzone_rect] = img
                    else:
                        img_rect.topleft = images[dragging][1].topleft  # Return to original position
                    break
                else:
                    img_rect.topleft = images[dragging][1].topleft  # Return to original position
                    if not in_dropzone:  # Add a new instance if the image was not dropped in a drop zone
                        add_new_instance(images[dragging])

                images[dragging] = (img, img_rect, in_dropzone)
                dragging = None

        elif event.type == pygame.MOUSEMOTION and dragging is not None:
            images[dragging][1].x = event.pos[0] + offset_x
            images[dragging][1].y = event.pos[1] + offset_y

    screen.fill(WHITE)

    for img, img_rect, in_dropzone in images:
        screen.blit(img, img_rect.topleft)

    for dropzone_rect in dropzone_contents:
        rect = pygame.Rect(*dropzone_rect)
        pygame.draw.rect(screen, DROPZONE_COLOR, rect, 2)

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
