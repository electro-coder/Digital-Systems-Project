import pygame
import sys
import random
from logic_gates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate, XNORGate


# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))




class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, font,level_1_inst, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.level_1_inst=level_1_inst
        self.action = action
        self.hovered = False

    def draw(self, screen):
        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
        else:
            self.hovered = False

    def click(self,gates):
        if self.action:
            self.action()

        if self.level_1_inst:
            return self.level_1_inst.functional_output(gates)




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
    
    #overloaded function for testing purposes of output
    def functional_output(self,gates):

        states=[[False,False],
                [False,True],
                [True,False],
                [True,True]]
        
        and_gate=None
        or_gate=None
        not_gate=None
        nand_gate=None
        nor_gate=None
        xor_gate=None
        xnor_gate=None

        output=[]
        
        for x,y in states:
            out_and=None
            out_or=None
            out_not=None
            out_nand=None
            out_nor=None
            out_xor=None
            out_xnor=None

            inputs=[]

            for zone in sorted(gates,reverse=True):
                if zone in [2,3,4]:
                    if gates[zone]=='and':
                        and_gate=ANDGate(x,y)
                        out_and=and_gate.set_input()
                        inputs.append(out_and)
                    elif gates[zone]=='or':
                        or_gate=ORGate(x,y)
                        out_or=or_gate.set_input()
                        inputs.append(out_or)
                    elif gates[zone]=='not':
                        not_gate=NOTGate(x)
                        out_not=not_gate.set_input()
                        inputs.append(out_not)
                    elif gates[zone]=='nand':
                        nand_gate=NANDGate(x,y)
                        out_nand=nand_gate.set_input()
                        inputs.append(out_nand)
                    elif gates[zone]=='nor':
                        nor_gate=NORGate(x,y)
                        out_nor=nor_gate.set_input()
                        inputs.append(out_nor)
                    elif gates[zone]=='xor':
                        xor_gate=XORGate(x,y)
                        out_xor=xor_gate.set_input()
                        inputs.append(out_xor)
                    elif gates[zone]=='xnor':
                        xnor_gate=XNORGate(x,y)
                        out_xnor=xnor_gate.set_input()
                        inputs.append(out_xnor)

                #print(inputs)
                if zone==1:
                    if len(inputs)==3:
                        if gates[zone]=='and':
                            and_gate=ANDGate(inputs[0],inputs[1],inputs[2])
                            output.append(and_gate.set_input())
                        elif gates[zone]=='or':
                            or_gate=ORGate(inputs[0],inputs[1],inputs[2])
                            output.append(or_gate.set_input())
                        elif gates[zone]=='not':
                            not_gate=NOTGate(inputs[0],inputs[1],inputs[2])
                            output.append(not_gate.set_input(inputs))
                        elif gates[zone]=='nand':
                            nand_gate=NANDGate(inputs[0],inputs[1],inputs[2])
                            output.append(nand_gate.set_input())
                        elif gates[zone]=='nor':
                            nor_gate=NORGate(inputs[0],inputs[1],inputs[2])
                            output.append(nor_gate.set_input())
                        elif gates[zone]=='xor':
                            xor_gate=XORGate(inputs[0],inputs[1],inputs[2])
                            output.append(xor_gate.set_input())
                        elif gates[zone]=='xnor':
                            xnor_gate=XNORGate(inputs[0],inputs[1],inputs[2])
                            output.append(xnor_gate.set_input())

                    elif len(inputs)==2:
                        if gates[zone]=='and':
                            and_gate=ANDGate(inputs[0],inputs[1])
                            output.append(and_gate.set_input())
                        elif gates[zone]=='or':
                            or_gate=ORGate(inputs[0],inputs[1])
                            output.append(or_gate.set_input())
                        elif gates[zone]=='not':
                            not_gate=NOTGate(inputs[0],inputs[1])
                            output.append(not_gate.set_input(inputs))
                        elif gates[zone]=='nand':
                            nand_gate=NANDGate(inputs[0],inputs[1])
                            output.append(nand_gate.set_input())
                        elif gates[zone]=='nor':
                            nor_gate=NORGate(inputs[0],inputs[1])
                            output.append(nor_gate.set_input())
                        elif gates[zone]=='xor':
                            xor_gate=XORGate(inputs[0],inputs[1])
                            output.append(xor_gate.set_input())
                        elif gates[zone]=='xnor':
                            xnor_gate=XNORGate(inputs[0],inputs[1])
                            output.append(xnor_gate.set_input())

        return output



    def run_level(self):

        WHITE = (255, 255, 255)
        DROPZONE_COLOR = (0, 255, 0)
        IMAGE_SIZE = (50, 50)
        CIRCLE_COLOR_ON = (255, 255, 0)
        CIRCLE_COLOR_OFF=(255,255,255)
        CIRCLE_RADIUS=30
        USER_CIRCLE_COLOR_ON = (255, 0, 0)
        USER_CIRCLE_COLOR_OFF=(255,255,255)
        USER_CIRCLE_RADIUS=20
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
        # image1_original_rect = image1_rect.copy()
        # image2_original_rect = image2_rect.copy()
        # image3_original_rect = image3_rect.copy()
        # image4_original_rect = image4_rect.copy()
        # image5_original_rect = image5_rect.copy()
        # image6_original_rect = image6_rect.copy()

        image_original_rect = [image1_rect.copy(),image2_rect.copy(),image3_rect.copy(),image4_rect.copy(),image5_rect.copy(),image6_rect.copy()]

        # Create drop zones
        dropzone_rect1 = pygame.Rect(500, 250, 70, 70)
        dropzone_rect2 = pygame.Rect(300, 250, 70, 70)
        dropzone_rect3 = pygame.Rect(300, 400, 70, 70)
        dropzone_rect4 = pygame.Rect(300, 100, 70, 70)
        dropzone_rect5 = pygame.Rect(150, 200, 70, 70)
        dropzone_rect6 = pygame.Rect(150, 300, 70, 70)

        # List of images, their original positions, and flags for indicating if they are in a drop zone
        images = [(image1, image1_rect, False,"or"),
                (image2, image2_rect, False,"and"),
                (image3, image3_rect, False,"nor"),
                (image4, image4_rect, False, "xor"),
                (image5, image5_rect, False,"nor"),
                (image6, image6_rect, False,"nor")]

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
        user_led_coord=[(650,215),(650,265),(650,315),(650,365)]
        led_states=[]
        user_led_states=[0,0,0,0]
        zones_op = {}
        org_image_count = 0

        # Main game loop
        running = True
        last_update_time=pygame.time.get_ticks()
        update_interval=1000
        flag=True
        dropzone_rect=[False,False,False,False]
        font1 = pygame.font.Font('freesansbold.ttf', 20)
        submit_button = Button(400, 500, 100, 50, "SUBMIT", (0, 150, 200), (0, 200, 255), (255, 255, 255), font1,self)
        check_button = Button(250, 500, 100, 50, "CHECK", (0, 150, 200), (0, 200, 255), (255, 255, 255), font1,self)
        counter=0 #Level_1 will have a limit of 5 submits
        while running:
            # Randomized LED states
            if visible:
                led_states = [random.choice([True, False]) for _ in range(num_leds)]
                for i in led_states:
                    print(int(i),end=' ')
                print()
                visible=False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if submit_button.rect.collidepoint(event.pos):
                        final_output=[int(i) for i in submit_button.click(zones_op)]
                        print(final_output)
                        if(final_output==led_states):
                            return True
                        else:
                            counter+=1

                        if counter==5:
                            return False
                        
                    if check_button.rect.collidepoint(event.pos):
                        user_led_states=[int(i) for i in check_button.click(zones_op)]
                        print(user_led_states)
                        
                    if event.button == 1:
                        for img, img_rect, in_dropzone, img_id in images:
                            if img_rect.collidepoint(event.pos) and not in_dropzone:
                                dragging = img, img_rect, in_dropzone, img_id
                                #images.remove((img, img_rect, in_dropzone))
                if event.type == pygame.MOUSEMOTION:
                    if dragging is not None:
                        _, img_rect, _, _ = dragging
                        img_rect.topleft = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    if dragging is not None:
                        img, img_rect, in_dropzone, img_id = dragging
                        drop_zones = [dropzone_rect1, dropzone_rect2, dropzone_rect3, dropzone_rect4, dropzone_rect5, dropzone_rect6]

                        # Check if any of the drop zones is empty, and drop the image if one is
                        for i, dropzone_rect in enumerate(drop_zones):
                            if dropzone_rect.colliderect(img_rect):
                                if dropzone_contents[tuple(dropzone_rect.topleft)] is None:
                                    img_rect.topleft = dropzone_rect.topleft
                                    in_dropzone = True
                                    dropzone_contents[tuple(dropzone_rect.topleft)] = img
                                    zones_op[i+1] = dragging[3]
                                    print(f"{dragging[3]} was dropped in Zone {i + 1}")
                                    break
                        else:
                            # Return the image to its original position if no drop zone is available
                            img_rect.topleft = image_original_rect[org_image_count].topleft
                            org_image_count = (org_image_count+1)%7

                        images.append((img, img_rect, in_dropzone, img_id))
                        dragging = None

            # Clear the screen
            self.screen.fill((155, 25, 255))
            for i in range(4):
                if i in zones_op.keys():
                    CIRCLE_COLOR=USER_CIRCLE_COLOR_ON
                else:
                    CIRCLE_COLOR=USER_CIRCLE_COLOR_OFF
                pygame.draw.circle(self.screen, CIRCLE_COLOR, user_led_coord[i] , USER_CIRCLE_RADIUS,0)
            # for i,state in enumerate(zones_op):
            #         CIRCLE_COLOR=USER_CIRCLE_COLOR_ON if state else USER_CIRCLE_COLOR_OFF
            #         pygame.draw.circle(self.screen, CIRCLE_COLOR, user_led_coord[i] , USER_CIRCLE_RADIUS,0)


            current_time = pygame.time.get_ticks()
            '''if current_time - blink_timer >= blink_interval:
                visible = not visible
                blink_timer = current_time'''

            '''if current_time-last_update_time>=update_interval:
                led_states = [random.choice([True, False]) for _ in range(num_leds)]
                last_update_time=current_time'''
            # if visible:
            #     led_states = [random.choice([True, False]) for _ in range(num_leds)]
            #     for i in led_states:
            #         print(int(i),end=' ')
            #     print()
            #     visible=False
            # for i,state in enumerate(user_led_states):
            #         CIRCLE_COLOR=CIRCLE_COLOR_ON if state else CIRCLE_COLOR_OFF
            #         pygame.draw.circle(self.screen, CIRCLE_COLOR, user_led_coord[i] , CIRCLE_RADIUS,0)

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

            # Draw drop zones/
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
            for img, img_rect, in_dropzone, img_id in images:
                self.screen.blit(img, img_rect)
                if in_dropzone:
                    pygame.draw.rect(self.screen, DROPZONE_COLOR, img_rect, 2)  # Add a border to indicate in the drop zone

            submit_button.update(pygame.mouse.get_pos())
            submit_button.draw(self.screen)
            check_button.update(pygame.mouse.get_pos())
            check_button.draw((self.screen))
            clock.tick(60)
            # Update the display
            pygame.display.flip()

            # Remaining thing to be added is a functional output match so that it returns true or false
            #return True

        # Quit Pygame
        print(zones_op)
        output=self.functional_output(zones_op)
        for i in output:
            print(int(i),end=' ')
        pygame.quit()
        sys.exit()


# Testing of Level-1
if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    level1=level_1(screen)
    level1.run_level()
    #output=level1.functional_output({4: 'or', 1: 'or', 2: 'and', 3: 'or'})
    pygame.quit()
    # for i in range(5):
    #     led_states = [random.choice([True, False]) for _ in range(4)]
    #     print(led_states)
    #     level1.functional_output(led_states)
    
