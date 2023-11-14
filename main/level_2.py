import pygame
import sys
import random

class level_2:
    def __init__(self,screen):

        #initialize Pygame
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse Level 2")

    def run_level(self):

        # Game Logic to be added here
        WHITE = (255, 255, 255)
        DROPZONE_COLOR = (0, 255, 0)
        IMAGE_SIZE = (50, 50)
        CIRCLE_COLOR_ON = (255, 255, 0)
        CIRCLE_COLOR_OFF = (255, 255, 255)
        CIRCLE_RADIUS = 30
        num_leds = 4
        total_time = 110
        # paths for image files
        path_or = "../Resources/or.png"
        path_and = "../Resources/and.png"
        # path_not="../Resources/not.png"
        path_nand = "../Resources/nand.png"
        path_xor = "../Resources/xor.png"
        path_nor = "../Resources/nor.png"


        try:
            image1 = pygame.image.load(path_or)  # Replace with your image file
            image1_1 = pygame.image.load(path_or)  # Replace with your image file
            image1_2 = pygame.image.load(path_or)  # Replace with your image file
            image1_3 = pygame.image.load(path_or)  # Replace with your image file
            image2 = pygame.image.load(path_and)  # Replace with your image file
            image2_1 = pygame.image.load(path_and)  # Replace with your image file
            image2_2 = pygame.image.load(path_and)  # Replace with your image file
            image2_3 = pygame.image.load(path_and)  # Replace with your image file
            # image3 = pygame.image.load(path_not)  # Replace with your image file
            # image3_1 = pygame.image.load(path_not)  # Replace with your image file
            # image3_2 = pygame.image.load(path_not)  # Replace with your image file
            # image3_3 = pygame.image.load(path_not)  # Replace with your image file
            image4 = pygame.image.load(path_nand)  # Replace with your image file
            image4_1 = pygame.image.load(path_nand)  # Replace with your image file
            image4_2 = pygame.image.load(path_nand)  # Replace with your image file
            image4_3 = pygame.image.load(path_nand)  # Replace with your image file
            image5 = pygame.image.load(path_xor)  # Replace with your image file
            image5_1 = pygame.image.load(path_xor)  # Replace with your image file
            image5_2 = pygame.image.load(path_xor)  # Replace with your image file
            image5_3 = pygame.image.load(path_xor)  # Replace with your image file
            image6 = pygame.image.load(path_nor)  # Replace with your image file
            image6_1 = pygame.image.load(path_nor)  # Replace with your image file
            image6_2 = pygame.image.load(path_nor)  # Replace with your image file
            image6_3 = pygame.image.load(path_nor)  # Replace with your image file

        except(FileNotFoundError):
            image1 = pygame.image.load(path_or.replace("..","."))  # Replace with your image file
            image1_1 = pygame.image.load(path_or.replace("..","."))  # Replace with your image file
            image1_2 = pygame.image.load(path_or.replace("..","."))  # Replace with your image file
            image1_3 = pygame.image.load(path_or.replace("..","."))  # Replace with your image file
            image2 = pygame.image.load(path_and.replace("..","."))  # Replace with your image file
            image2_1 = pygame.image.load(path_and.replace("..","."))  # Replace with your image file
            image2_2 = pygame.image.load(path_and.replace("..","."))  # Replace with your image file
            image2_3 = pygame.image.load(path_and.replace("..","."))  # Replace with your image file
            # image3 = pygame.image.load(path_not.replace("..","."))  # Replace with your image file
            # image3_1 = pygame.image.load(path_not.replace("..","."))  # Replace with your image file
            # image3_2 = pygame.image.load(path_not.replace("..","."))  # Replace with your image file
            # image3_3 = pygame.image.load(path_not.replace("..","."))  # Replace with your image file
            image4 = pygame.image.load(path_nand.replace("..","."))  # Replace with your image file
            image4_1 = pygame.image.load(path_nand.replace("..","."))  # Replace with your image file
            image4_2 = pygame.image.load(path_nand.replace("..","."))  # Replace with your image file
            image4_3 = pygame.image.load(path_nand.replace("..","."))  # Replace with your image file
            image5 = pygame.image.load(path_xor.replace("..","."))  # Replace with your image file
            image5_1 = pygame.image.load(path_xor.replace("..","."))  # Replace with your image file
            image5_2 = pygame.image.load(path_xor.replace("..","."))  # Replace with your image file
            image5_3 = pygame.image.load(path_xor.replace("..","."))  # Replace with your image file
            image6 = pygame.image.load(path_nor.replace("..","."))  # Replace with your image file
            image6_1 = pygame.image.load(path_nor.replace("..","."))  # Replace with your image file
            image6_2 = pygame.image.load(path_nor.replace("..","."))  # Replace with your image file
            image6_3 = pygame.image.load(path_nor.replace("..","."))  # Replace with your image file


        # Initial positions of images
        image1_rect = image1.get_rect(topleft=(120, 10))
        image1_1_rect = image1.get_rect(topleft=(120, 10))
        image1_2_rect = image1.get_rect(topleft=(120, 10))
        image1_3_rect = image1.get_rect(topleft=(120, 10))

        image2_rect = image2.get_rect(topleft=(235, 10))
        image2_1_rect = image2.get_rect(topleft=(235, 10))
        image2_2_rect = image2.get_rect(topleft=(235, 10))
        image2_3_rect = image2.get_rect(topleft=(235, 10))

        # image3_rect = image3.get_rect(topleft=(260, 10))
        # image3_1_rect = image3.get_rect(topleft=(260, 10))
        # image3_2_rect = image3.get_rect(topleft=(260, 10))
        # image3_3_rect = image3.get_rect(topleft=(260, 10))

        image4_rect = image4.get_rect(topleft=(350, 10))
        image4_1_rect = image4.get_rect(topleft=(350, 10))
        image4_2_rect = image4.get_rect(topleft=(350, 10))
        image4_3_rect = image4.get_rect(topleft=(350, 10))

        image5_rect = image5.get_rect(topleft=(480, 10))
        image5_1_rect = image5.get_rect(topleft=(480, 10))
        image5_2_rect = image5.get_rect(topleft=(480, 10))
        image5_3_rect = image5.get_rect(topleft=(480, 10))

        image6_rect = image6.get_rect(topleft=(620, 10))
        image6_1_rect = image6.get_rect(topleft=(620, 10))
        image6_2_rect = image6.get_rect(topleft=(620, 10))
        image6_3_rect = image6.get_rect(topleft=(620, 10))


        image_original_rect = [image1_rect.copy(), image2_rect.copy(), image4_rect.copy(), image5_rect.copy(),
                               image6_rect.copy()]

        # Original positions of images
        image1_original_rect = image1_rect.copy()
        image2_original_rect = image2_rect.copy()
        # image3_original_rect = image3_rect.copy()
        image4_original_rect = image4_rect.copy()
        image5_original_rect = image5_rect.copy()
        image6_original_rect = image6_rect.copy()

        # Create drop zones
        dropzone_rect2 = pygame.Rect(350, 250, 70, 70)
        dropzone_rect3 = pygame.Rect(350, 400, 70, 70)
        dropzone_rect4 = pygame.Rect(350, 100, 70, 70)
        dropzone_rect1 = pygame.Rect(150, 250, 70, 70)
        dropzone_rect5 = pygame.Rect(150, 120, 70, 70)
        dropzone_rect6 = pygame.Rect(150, 380, 70, 70)


        dropzone = [pygame.Rect(350, 250, 70, 70), pygame.Rect(350, 400, 70, 70), pygame.Rect(350, 100, 70, 70),pygame.Rect(150, 250, 70, 70),pygame.Rect(150, 120, 70, 70),pygame.Rect(150, 380, 70, 70) ]

        # List of images, their original positions, and flags for indicating if they are in a drop zone
        images = [(image1, image1_rect, False,"or","1"),(image1_1, image1_1_rect, False,"or",'1'),
                  (image1_2, image1_2_rect, False,"or",'1'),(image1_3, image1_3_rect, False,"or",'1'),
                (image2, image2_rect, False,"and",'2'),(image2_1, image2_1_rect, False,"and",'2'),
                  (image2_2, image2_2_rect, False, "and",'2'),(image2_3, image2_3_rect, False,"and",'2'),
                # (image3, image3_rect, False,"not",'3'),(image3_1, image3_1_rect, False,"not",'3'),
                #   (image3_2, image3_2_rect, False, "not",'3'),(image3_3, image3_3_rect, False,"not",'3'),
                (image4, image4_rect, False, "nand",'3'),(image4_1, image4_1_rect, False, "nand",'3'),
                  (image4_2, image4_2_rect, False, "nand",'3'),(image4_3, image4_3_rect, False, "nand",'3'),
                (image5, image5_rect, False,"xor",'4'),(image5_1, image5_1_rect, False,"xor",'4'),
                  (image5_2, image5_2_rect, False,"xor",'4'),(image5_3, image5_3_rect, False,"xor",'4'),
                (image6, image6_rect, False,"nor",'5'),(image6_1, image6_1_rect, False,"nor",'5'),
                  (image6_2, image6_2_rect, False,"nor",'5'),(image6_3, image6_3_rect, False,"nor",'5')]

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
        led_coord=[(750,150),(750,250),(750,350),(750,450)]
        led_states = []
        zones_op = {}
        # Main game loop
        running = True
        last_update_time = pygame.time.get_ticks()
        update_interval = 1000
        flag = True
        TIMER_FONT = pygame.font.Font(None, 36)
        # timer_running = True
        start_time = pygame.time.get_ticks()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for img, img_rect, in_dropzone, img_id, img_code in images:
                            if img_rect.collidepoint(event.pos) and not in_dropzone:
                                dragging = img, img_rect, in_dropzone, img_id, img_code
                                #images.remove((img, img_rect, in_dropzone))
                if event.type == pygame.MOUSEMOTION:
                    if dragging is not None:
                        _, img_rect, _, _, _ = dragging
                        img_rect.topleft = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    if dragging is not None:
                        img, img_rect, in_dropzone, img_id, img_code = dragging
                        drop_zones = [dropzone_rect1, dropzone_rect2, dropzone_rect3, dropzone_rect4, dropzone_rect5, dropzone_rect6]

                        # Check if any of the drop zones is empty, and drop the image if one is
                        for i, dropzone_rect in enumerate(drop_zones):
                            if dropzone_rect.colliderect(img_rect):
                                if dropzone_contents[tuple(dropzone_rect.topleft)] is None:
                                    img_rect.topleft = dropzone_rect.topleft
                                    in_dropzone = True
                                    dropzone_contents[tuple(dropzone_rect.topleft)] = img
                                    zones_op[i + 1] = dragging[3]
                                    print(f"{dragging[3]} was dropped in Zone {i + 1}")
                                    break
                            else:
                                # Return the image to its original position if no drop zone is available
                                img_rect.topleft = image_original_rect[int(img_code) - 1].topleft

                        images.append((img, img_rect, in_dropzone, img_id, img_code))
                        dragging = None
            #timer (time remaining)/

            elapsed_time = (pygame.time.get_ticks())
            seconds = elapsed_time // 1000  # Convert milliseconds to seconds
            seconds_remaining = total_time - (elapsed_time // 1000)
            # Clear the screen
            self.screen.fill((255, 0, 255))
            # pygame.draw.rect(self.screen,(128,128,128) ,((290,90),(200,400)))
            #timer text
            timer_text = TIMER_FONT.render(f"Remaining Time : {seconds_remaining} seconds", True, (0,0,0))
            self.screen.blit(timer_text, (250, 550))
            current_time = pygame.time.get_ticks()

            if seconds_remaining <= 0:
                return False

            if visible:
                led_states = [random.choice([True, False]) for _ in range(num_leds)]
                for i in led_states:
                    print(int(i),end=' ')
                print()
                visible=False
            for i,state in enumerate(led_states):
                    CIRCLE_COLOR=CIRCLE_COLOR_ON if state else CIRCLE_COLOR_OFF
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, led_coord[i] , CIRCLE_RADIUS,0)

            #pygame.draw.circle(screen, CIRCLE_COLOR, tuple(led_coord) , CIRCLE_RADIUS,0)
            # for start, end in connections:
            #     pygame.draw.line(screen, (255, 0, 0), start, end, 5)
            # pygame.draw.line(self.screen, (254, 20, 50), (200,220), (250,220), 5)
            # pygame.draw.line(self.screen, (254, 20, 50), (250, 420), (250, 120), 5)
            # pygame.draw.line(self.screen, (254, 20, 50), (248, 120), (300, 120), 5)
            # pygame.draw.line(self.screen, (254, 20, 50), (248, 270), (300, 270), 5)
            # pygame.draw.line(self.screen, (254, 20, 50), (248, 420), (300, 420), 5)
            # pygame.draw.line(self.screen, (0, 0, 0), (270, 450), (270, 150), 5)
            # pygame.draw.line(self.screen, (0, 0, 0), (200,320), (270,320), 5)
            # pygame.draw.line(self.screen, (0, 0, 0), (270, 300), (300, 300), 5)
            # pygame.draw.line(self.screen, (0, 0, 0), (268, 150), (300, 150), 5)
            # pygame.draw.line(self.screen, (0, 0, 0), (268, 450), (300, 450), 5)
            # pygame.draw.line(self.screen, (0, 34, 45), (350, 285), (500, 285), 5)
            # pygame.draw.line(self.screen, (0, 34, 45), (350, 130), (530, 130), 5)
            # pygame.draw.line(self.screen, (0, 34, 45), (350, 430), (530, 430), 5)
            # pygame.draw.line(self.screen, (0, 34, 45), (530, 129), (530, 300), 5)
            # pygame.draw.line(self.screen, (0, 34, 45), (530, 430), (530, 310), 5)
            # pygame.draw.line(self.screen, (0, 34, 45), (560, 285), (620, 285), 5)

            # Draw drop zones
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect1)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect2)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect3)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect4)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect5)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect6)

            #text of X and Y
            font=pygame.font.Font('freesansbold.ttf',30)
            self.screen.blit(font.render("X",True,(0,0,0)),(170,135))
            self.screen.blit(font.render("Y",True,(0,0,0)),(170,265))
            self.screen.blit(font.render("Z", True, (0, 0, 0)), (170, 395))
            self.screen.blit(font.render("OUTPUT", True, (0, 0, 0)), (500, 280))

            # Draw the images
            for img, img_rect, in_dropzone, img_id , img_code in images:
                self.screen.blit(img, img_rect)
                if in_dropzone:
                    pygame.draw.rect(self.screen, DROPZONE_COLOR, img_rect, 2)  # Add a border to indicate in the drop zone

            clock.tick(60)
            # Update the display
            pygame.display.flip()

           # Remaining thing to be added is a functional output match so that it returns true or false
            # return True

        # Quit Pygame
        pygame.quit()
        sys.exit()




#Testing of Level-2
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    level2=level_2(screen)
    level2.run_level()
    pygame.quit()