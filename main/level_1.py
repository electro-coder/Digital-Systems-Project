import pygame
import sys
import random
from logic_gates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate, XNORGate


# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
class level_1:
    def __init__(self,screen):

        #initialize Pygame
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse Level 1")

    def functional_output(self,gates,led_states,dropzone_rect):
        and_gate=None
        or_gate=None
        not_gate=None
        nand_gate=None
        nor_gate=None
        xor_gate=None
        xnor_gate=None

        for gate in gates:
            if gate.rect.colliderect(dropzone_rect[0]):
                if isinstance(gate, ANDGate):
                    and_gate=gate
                elif isinstance(gate,ORGate):
                    or_gate=gate
                elif isinstance(gate,ORGate):
                    or_gate=gate
                elif isinstance(gate,NOTGate):
                    not_gate=gate
                elif isinstance(gate,NANDGate):
                    nand_gate=gate
                elif isinstance(gate,NORGate):
                    nor_gate=gate
                elif isinstance(gate,XORGate):
                    xor_gate=gate
                elif isinstance(gate,XNORGate):
                    xnor_gate=gate

            if gate.rect.colliderect(dropzone_rect[1]):
                if isinstance(gate, ANDGate):
                    and_gate=gate
                elif isinstance(gate,ORGate):
                    or_gate=gate
                elif isinstance(gate,ORGate):
                    or_gate=gate
                elif isinstance(gate,NOTGate):
                    not_gate=gate
                elif isinstance(gate,NANDGate):
                    nand_gate=gate
                elif isinstance(gate,NORGate):
                    nor_gate=gate
                elif isinstance(gate,XORGate):
                    xor_gate=gate
                elif isinstance(gate,XNORGate):
                    xnor_gate=gate

            if gate.rect.colliderect(dropzone_rect[2]):
                if isinstance(gate, ANDGate):
                    and_gate=gate
                elif isinstance(gate,ORGate):
                    or_gate=gate
                elif isinstance(gate,ORGate):
                    or_gate=gate
                elif isinstance(gate,NOTGate):
                    not_gate=gate
                elif isinstance(gate,NANDGate):
                    nand_gate=gate
                elif isinstance(gate,NORGate):
                    nor_gate=gate
                elif isinstance(gate,XORGate):
                    xor_gate=gate
                elif isinstance(gate,XNORGate):
                    xnor_gate=gate

        if and_gate:
            and_gate.set_input(led_states[0],led_states[1])
        if or_gate:
            or_gate.set_input(led_states[0],led_states[1])
        if not_gate:
            not_gate.set_input(led_states[0],led_states[1])
        if nand_gate:
            nand_gate.set_input(led_states[0],led_states[1])
        if nor_gate:
            nor_gate.set_input(led_states[0],led_states[1])
        if xor_gate:
            xor_gate.set_input(led_states[0],led_states[1])
        if xnor_gate:
            xnor_gate.set_input(led_states[0],led_states[1])


    #overloaded function for testing purposes of output
    def functional_output(self,led_states):
        and_gate=ANDGate()
        or_gate=ORGate()
        not_gate=NOTGate()
        nand_gate=NANDGate()
        nor_gate=NORGate()
        xor_gate=XORGate()
        xnor_gate=XNORGate()

        out_and=None
        out_or=None
        out_not=None
        out_nand=None
        out_nor=None
        out_xor=None
        out_xnor=None

        
        out_and=and_gate.set_input(led_states[0],led_states[1])
        out_or=or_gate.set_input(led_states[0],led_states[1])
        out_not=not_gate.set_input(led_states[0],led_states[1])
        out_nand=nand_gate.set_input(led_states[0],led_states[1])
        out_nor=nor_gate.set_input(led_states[0],led_states[1])
        out_xor=xor_gate.set_input(led_states[0],led_states[1])
        out_xnor=xnor_gate.set_input(led_states[0],led_states[1])
       
        output=[out_and,out_or,out_not,out_nand,out_nor,out_xor,out_xnor]
        print(output)


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
        led_coord=[(750,150),(750,250),(750,350),(750,450)]
        led_states=[]
        # Main game loop
        running = True
        last_update_time=pygame.time.get_ticks()
        update_interval=1000
        flag=True
        dropzone_rect=[False,False,False,False]

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
            self.screen.fill((255, 0, 255))


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
            for i,state in enumerate(led_states):
                    CIRCLE_COLOR=CIRCLE_COLOR_ON if state else CIRCLE_COLOR_OFF
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, led_coord[i] , CIRCLE_RADIUS,0)

            #pygame.draw.circle(screen, CIRCLE_COLOR, tuple(led_coord) , CIRCLE_RADIUS,0)
            # for start, end in connections:
            #     pygame.draw.line(screen, (255, 0, 0), start, end, 5)
            pygame.draw.line(self.screen, (254, 20, 50), (200,220), (250,220), 5)
            pygame.draw.line(self.screen, (254, 20, 50), (250, 420), (250, 120), 5)
            pygame.draw.line(self.screen, (254, 20, 50), (248, 120), (300, 120), 5)
            pygame.draw.line(self.screen, (254, 20, 50), (248, 270), (300, 270), 5)
            pygame.draw.line(self.screen, (254, 20, 50), (248, 420), (300, 420), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (270, 450), (270, 150), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (200,320), (270,320), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (270, 300), (300, 300), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (268, 150), (300, 150), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (268, 450), (300, 450), 5)
            pygame.draw.line(self.screen, (0, 34, 45), (350, 285), (500, 285), 5)
            pygame.draw.line(self.screen, (0, 34, 45), (350, 130), (530, 130), 5)
            pygame.draw.line(self.screen, (0, 34, 45), (350, 430), (530, 430), 5)
            pygame.draw.line(self.screen, (0, 34, 45), (530, 129), (530, 300), 5)
            pygame.draw.line(self.screen, (0, 34, 45), (530, 430), (530, 310), 5)
            pygame.draw.line(self.screen, (0, 34, 45), (560, 285), (620, 285), 5)

            # Draw drop zones
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect1)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect2)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect3)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect4)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect5)
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect6)

            #text of X and Y
            font=pygame.font.Font('freesansbold.ttf',40)
            self.screen.blit(font.render("X",True,(0,0,0)),(170,215))
            self.screen.blit(font.render("Y",True,(0,0,0)),(170,310))

            # Draw the images
            for img, img_rect, in_dropzone in images:
                self.screen.blit(img, img_rect)
                if in_dropzone:
                    pygame.draw.rect(self.screen, DROPZONE_COLOR, img_rect, 2)  # Add a border to indicate in the drop zone

            clock.tick(60)
            # Update the display
            pygame.display.flip()

            # Remaining thing to be added is a functional output match so that it returns true or false
            #return True

        # Quit Pygam
        pygame.quit()
        sys.exit()


# Testing of Level-1
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    level1=level_1(screen)
    # level1.run_level()
    pygame.quit()
    for i in range(5):
        led_states = [random.choice([True, False]) for _ in range(4)]
        print(led_states)
        level1.functional_output(led_states)
    
