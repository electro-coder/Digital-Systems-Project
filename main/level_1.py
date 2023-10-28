import pygame
import sys
import random

class level_1:
    def __init__(self,screen):

        #initialize Pygame
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse Level 1")

    def run_level(self):

        WHITE = (255, 255, 255)
        DROPZONE_COLOR = (0, 255, 0)
        IMAGE_SIZE = (50, 50)
        CIRCLE_COLOR_ON = (255, 255, 0)
        CIRCLE_COLOR_OFF=(255,255,255)
        CIRCLE_RADIUS=30
        num_leds=4

        #paths for image files
        path1="../Resources/or.png"
        path2="../Resources/and.png"
        path3="../Resources/nor.png"
        path4="../Resources/xor.png"
        path5="../Resources/nor.png"
        path6="../Resources/nor.png"

        try:
            image1 = pygame.image.load(path1)  # Replace with your image file
            image2 = pygame.image.load(path2)  # Replace with your image file
            image3 = pygame.image.load(path3)  # Replace with your image file
            image4 = pygame.image.load(path4)  # Replace with your image file
            image5 = pygame.image.load(path5)  # Replace with your image file
            image6 = pygame.image.load(path6)  # Replace with your image file
        except(FileNotFoundError):
            image1 = pygame.image.load(path1.replace("..","."))  # Replace with your image file
            image2 = pygame.image.load(path2.replace("..","."))  # Replace with your image file
            image3 = pygame.image.load(path3.replace("..","."))  # Replace with your image file
            image4 = pygame.image.load(path4.replace("..","."))  # Replace with your image file
            image5 = pygame.image.load(path5.replace("..","."))  # Replace with your image file
            image6 = pygame.image.load(path6.replace("..","."))  # Replace with your image file


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
        blink_interval = 0  # milliseconds
        blink_timer = 0
        visible = True
        dragging = None
        led_coord=[750,150]
        led_states=[]
        # Main game loop
        running = True
        last_update_time=pygame.time.get_ticks()
        update_interval=1000
        flag=True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for img, img_rect, in_dropzone in images:
                            if img_rect.collidepoint(event.pos) and not in_dropzone:
                                dragging = img, img_rect, in_dropzone
                                #images.remove((img, img_rect, in_dropzone))
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
            screen.fill((255, 255, 255))


            current_time = pygame.time.get_ticks()
            '''if current_time - blink_timer >= blink_interval:
                visible = not visible
                blink_timer = current_time'''

            '''if current_time-last_update_time>=update_interval:
                led_states = [random.choice([True, False]) for _ in range(num_leds)]
                last_update_time=current_time'''
            if visible:
                led_states = [random.choice([True, False]) for _ in range(num_leds)]
                for i in led_states:
                    print(int(i),end=' ')
                print()
                visible=False
            for i in led_states:
                    CIRCLE_COLOR=CIRCLE_COLOR_ON if int(i) else CIRCLE_COLOR_OFF
                    if int(i)==1:
                        pygame.draw.circle(screen, CIRCLE_COLOR, tuple(led_coord) , CIRCLE_RADIUS,0)
                    else:
                        pygame.draw.circle(screen, CIRCLE_COLOR, tuple(led_coord) , CIRCLE_RADIUS,0)
                    led_coord[1]+=100

            #pygame.draw.circle(screen, CIRCLE_COLOR, tuple(led_coord) , CIRCLE_RADIUS,0)
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
            pygame.draw.line(screen, (0, 34, 45), (560, 285), (620, 285), 5)

            # Draw drop zones
            pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect1)
            pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect2)
            pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect3)
            pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect4)
            pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect5)
            pygame.draw.rect(screen, DROPZONE_COLOR, dropzone_rect6)

            #text of X and Y
            font=pygame.font.Font('freesansbold.ttf',40)
            screen.blit(font.render("X",True,(0,0,0)),(170,215))
            screen.blit(font.render("Y",True,(0,0,0)),(170,310))

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


# Testing of Level-1
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    level1=level_1(screen)
    level1.run_level()
    pygame.quit()