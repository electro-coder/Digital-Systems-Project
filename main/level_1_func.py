import pygame
import sys
import random
from logic_gates import ANDGate, ORGate, NOTGate, NANDGate, NORGate, XORGate, XNORGate

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

    def click(self,gates,seq):
        if self.action:
            self.action()

        if self.level_1_inst:
            return self.level_1_inst.functional_output(gates,seq)

class level_1:
    def __init__(self,screen):

        #initialize Pygame
        pygame.init()

        # Display Surface
        self.screen=screen
        pygame.display.set_caption("CodeDiffuse Level 1")

        path_background="../Resources/background1.png"

        try:
            self.background=pygame.image.load(path_background)
        except(FileNotFoundError):
            self.background=pygame.image.load(path_background.replace("..","."))

        self.background = pygame.transform.scale(self.background, (800, 600))

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

    def var(self,x,y,order):
        if order[0]=="x\'" or order[1]=="x\'": x=not x
        if order[1]=="y\'" or order[1]=="y\'": y=not y
        return (x,y)

    #overloaded function for testing purposes of output
    def functional_output(self,gates,seq):

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

        inputs=[]
        
        for a,b in states:
            out_and=None
            out_or=None
            out_not=None
            out_nand=None
            out_nor=None
            out_xor=None
            out_xnor=None

            for zone in sorted(gates,reverse=True):
                    x,y=self.var(a,b,seq[zone])
                    if zone==1:
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

        return inputs
    
    def canonical_function_generation(self,dict_gates,gates):
        func1=''
        func2=''
        func3=''
        function=''
        flag1=False
        flag2=False
        flag3=False
        flag=False
        for zone,variables in dict_gates.items():
            if zone == 1:
                flag1=True
                if gates[zone]=='and':
                    func1+=variables[0]+'.'+variables[1]
                elif gates[zone]=='or':
                    func1+=variables[0]+'+'+variables[1]
                elif gates[zone]=='nand':
                    func1+='('+variables[0]+'.'+variables[1]+')\''
                elif gates[zone]=='nor':
                    func1+='('+variables[0]+'+'+variables[1]+')\''
                elif gates[zone]=='xor':
                    func1+=variables[0]+'^'+variables[1]
                elif gates[zone]=='xnor':
                    func1+='('+variables[0]+'^'+variables[1]+')\''
                
        return func1

    def run_level(self):

        WHITE = (255, 255, 255)
        DROPZONE_COLOR = (0, 255, 0)
        ZONE_COLOR = (200,200,100)
        IMAGE_SIZE = (50, 50)
        CIRCLE_COLOR_ON = (255, 255, 0)
        CIRCLE_COLOR_OFF=(255,255,255)
        CIRCLE_RADIUS=30
        USER_CIRCLE_COLOR_ON = (255, 0, 0)
        USER_CIRCLE_COLOR_OFF=(255,255,255)
        USER_CIRCLE_RADIUS=20
        num_leds=4
        DOT_RADIUS=10
        DOT_COLOR=(255,0,0)
        SELECTED_DOT_COLOR=(255,255,0)
        LINE_COLOR=(0,0,255)
        LINE_WIDTH=2
        lines=[]
        selected_dot=None
        dots_coord=[(220,135),(220,235),(220,335),(220,435),(450,280),(450,310)]
        dynamic_connections=[]
        # dynamic_verification={41:(300,173),42:(300,197),21:(300,273),22:(300,297),31:(300,373),32:(300,397),43:(370,185),23:(370,285),33:(370,385),11:(500,267),12:(500,285),13:(500,303)}
        dynamic_verification={11:(450,280),12:(450,310)}

        variables={'x':(220,135),'x\'':(220,235),'y':(220,335),'y\'':(220,435),'11':(450,280),'12':(450,310)}
    
        path_or="../Resources/or.png"
        path_and="../Resources/and.png"
        path_nor="../Resources/nor.png"
        path_xor="../Resources/xor.png"
        path_nand="../Resources/nand.png"
        path_xnor="../Resources/xnor.png"
        path_not="../Resources/not.png"
    
        try:
            image1 = pygame.image.load(path_or)  # Replace with your image file
            image1_1 = pygame.image.load(path_or)  # Replace with your image file
            image1_2 = pygame.image.load(path_or)  # Replace with your image file
            image1_3 = pygame.image.load(path_or)  # Replace with your image file
            image2 = pygame.image.load(path_and)  # Replace with your image file
            image2_1 = pygame.image.load(path_and)  # Replace with your image file
            image2_2 = pygame.image.load(path_and)  # Replace with your image file
            image2_3 = pygame.image.load(path_and)  # Replace with your image file
            image3 = pygame.image.load(path_nor)  # Replace with your image file
            image3_1 = pygame.image.load(path_nor)  # Replace with your image file
            image3_2 = pygame.image.load(path_nor)  # Replace with your image file
            image3_3 = pygame.image.load(path_nor)  # Replace with your image file
            image4 = pygame.image.load(path_xor)  # Replace with your image file
            image4_1 = pygame.image.load(path_xor)  # Replace with your image file
            image4_2 = pygame.image.load(path_xor)  # Replace with your image file
            image4_3 = pygame.image.load(path_xor)  # Replace with your image file
            image5 = pygame.image.load(path_nand)  # Replace with your image file
            image5_1 = pygame.image.load(path_nand)  # Replace with your image file
            image5_2 = pygame.image.load(path_nand)  # Replace with your image file
            image5_3 = pygame.image.load(path_nand)  # Replace with your image file
            image6 = pygame.image.load(path_xnor)  # Replace with your image file
            image6_1 = pygame.image.load(path_xnor)  # Replace with your image file
            image6_2 = pygame.image.load(path_xnor)  # Replace with your image file
            image6_3 = pygame.image.load(path_xnor)  # Replace with your image file
            image7 = pygame.image.load(path_not)
            image7_1 = pygame.image.load(path_not)
            image7_2 = pygame.image.load(path_not)
            image7_3 = pygame.image.load(path_not)

        except(FileNotFoundError):
            image1 = pygame.image.load(path_or.replace("..", "."))  # Replace with your image file
            image1_1 = pygame.image.load(path_or.replace("..", "."))  # Replace with your image file
            image1_2 = pygame.image.load(path_or.replace("..", "."))  # Replace with your image file
            image1_3 = pygame.image.load(path_or.replace("..", "."))  # Replace with your image file
            image2 = pygame.image.load(path_and.replace("..", "."))  # Replace with your image file
            image2_1 = pygame.image.load(path_and.replace("..", "."))  # Replace with your image file
            image2_2 = pygame.image.load(path_and.replace("..", "."))  # Replace with your image file
            image2_3 = pygame.image.load(path_and.replace("..", "."))  # Replace with your image file
            image3 = pygame.image.load(path_nor.replace("..", "."))  # Replace with your image file
            image3_1 = pygame.image.load(path_nor.replace("..", "."))  # Replace with your image file
            image3_2 = pygame.image.load(path_nor.replace("..", "."))  # Replace with your image file
            image3_3 = pygame.image.load(path_nor.replace("..", "."))  # Replace with your image file
            image4 = pygame.image.load(path_xor.replace("..", "."))  # Replace with your image file
            image4_1 = pygame.image.load(path_xor.replace("..", "."))  # Replace with your image file
            image4_2 = pygame.image.load(path_xor.replace("..", "."))  # Replace with your image file
            image4_3 = pygame.image.load(path_xor.replace("..", "."))  # Replace with your image file
            image5 = pygame.image.load(path_nand.replace("..", "."))  # Replace with your image file
            image5_1 = pygame.image.load(path_nand.replace("..", "."))  # Replace with your image file
            image5_2 = pygame.image.load(path_nand.replace("..", "."))  # Replace with your image file
            image5_3 = pygame.image.load(path_nand.replace("..", "."))  # Replace with your image file
            image6 = pygame.image.load(path_xnor.replace("..", "."))  # Replace with your image file
            image6_1 = pygame.image.load(path_xnor.replace("..", "."))  # Replace with your image file
            image6_2 = pygame.image.load(path_xnor.replace("..", "."))  # Replace with your image file
            image6_3 = pygame.image.load(path_xnor.replace("..", "."))  # Replace with your image file
            image7 = pygame.image.load(path_not.replace("..", "."))
            image7_1 = pygame.image.load(path_not.replace("..", "."))
            image7_2 = pygame.image.load(path_not.replace("..", "."))
            image7_3 = pygame.image.load(path_not.replace("..", "."))

        # Initial positions of images
        image1_rect = image1.get_rect(topleft=(20, 20))
        image1_1_rect = image1.get_rect(topleft=(20, 20))
        image1_2_rect = image1.get_rect(topleft=(20, 20))
        image1_3_rect = image1.get_rect(topleft=(20, 20))

        image2_rect = image2.get_rect(topleft=(125, 20))
        image2_1_rect = image2.get_rect(topleft=(125, 20))
        image2_2_rect = image2.get_rect(topleft=(125, 20))
        image2_3_rect = image2.get_rect(topleft=(125, 20))

        image3_rect = image3.get_rect(topleft=(220, 20))
        image3_1_rect = image3.get_rect(topleft=(220, 20))
        image3_2_rect = image3.get_rect(topleft=(220, 20))
        image3_3_rect = image3.get_rect(topleft=(220, 20))

        image4_rect = image4.get_rect(topleft=(330, 20))
        image4_1_rect = image4.get_rect(topleft=(330, 20))
        image4_2_rect = image4.get_rect(topleft=(330, 20))
        image4_3_rect = image4.get_rect(topleft=(330, 20))

        image5_rect = image5.get_rect(topleft=(450, 20))
        image5_1_rect = image5.get_rect(topleft=(450, 20))
        image5_2_rect = image5.get_rect(topleft=(450, 20))
        image5_3_rect = image5.get_rect(topleft=(450, 20))

        image6_rect = image6.get_rect(topleft=(570, 20))
        image6_1_rect = image6.get_rect(topleft=(570, 20))
        image6_2_rect = image6.get_rect(topleft=(570, 20))
        image6_3_rect = image6.get_rect(topleft=(570, 20))

        image7_rect = image7.get_rect(topleft=(680, 20))
        image7_1_rect = image7.get_rect(topleft=(680, 20))
        image7_2_rect = image7.get_rect(topleft=(680, 20))
        image7_3_rect = image7.get_rect(topleft=(680, 20))

        # Original positions of images
        # image1_original_rect = image1_rect.copy()
        # image2_original_rect = image2_rect.copy()
        # image3_original_rect = image3_rect.copy()
        # image4_original_rect = image4_rect.copy()
        # image5_original_rect = image5_rect.copy()
        # image6_original_rect = image6_rect.copy()
        # image7_original_rect = image7_rect.copy()

        image_original_rect = [image1_rect.copy(), image2_rect.copy(), image3_rect.copy(), image4_rect.copy(),
                               image5_rect.copy(), image6_rect.copy()]
        # Create drop zones
        #dropzone_rect2 = pygame.Rect(300, 150, 70, 70)
        #dropzone_rect3 = pygame.Rect(300, 350, 70, 70)
        dropzone_rect1 = pygame.Rect(450, 250, 100, 90)
        dropzone_rect4 = pygame.Rect(150, 100, 70, 70)
        zone_rect5 = pygame.Rect(150, 200, 70, 70)
        zone_rect6 = pygame.Rect(150, 300, 70, 70)
        dropzone_rect7 = pygame.Rect(150, 400, 70, 70)

        dropzone = [pygame.Rect(500, 250, 70, 70), pygame.Rect(300, 250, 70, 70), pygame.Rect(300, 400, 70, 70),
                    pygame.Rect(300, 100, 70, 70)]

        # List of images, their original positions, and flags for indicating if they are in a drop zone
        images = [(image1, image1_rect, False,"or","1"),(image1_1, image1_1_rect, False,"or",'1'),
                  (image1_2, image1_2_rect, False,"or",'1'),(image1_3, image1_3_rect, False,"or",'1'),
                (image2, image2_rect, False,"and",'2'),(image2_1, image2_1_rect, False,"and",'2'),
                  (image2_2, image2_2_rect, False, "and",'2'),(image2_3, image2_3_rect, False,"and",'2'),
                (image3, image3_rect, False,"nor",'3'),(image3_1, image3_1_rect, False,"nor",'3'),
                  (image3_2, image3_2_rect, False, "nor",'3'),(image3_3, image3_3_rect, False,"nor",'3'),
                (image4, image4_rect, False, "xor",'4'),(image4_1, image4_1_rect, False, "xor",'4'),
                  (image4_2, image4_2_rect, False, "xor",'4'),(image4_3, image4_3_rect, False, "xor",'4'),
                (image5, image5_rect, False,"nor",'5'),(image5_1, image5_1_rect, False,"nor",'5'),
                  (image5_2, image5_2_rect, False, "nor", '5'),(image5_3, image5_3_rect, False,"nor",'5'),
                (image6, image6_rect, False,"nor",'6'),(image6_1, image6_1_rect, False,"nor",'6'),
                  (image6_2, image6_2_rect, False, "nor", '6'),(image6_3, image6_3_rect, False,"nor",'6'),
                (image7, image7_rect, False,"not",'7'),(image7_1, image7_1_rect, False,"not",'7'),
                  (image7_2, image7_2_rect, False,"not",'7'),(image7_3, image7_3_rect, False,"not",'7')]
        
        # Dictionary to keep track of which image is in which drop zone
        dropzone_contents = {tuple(dropzone_rect1.topleft): None,
                            tuple(dropzone_rect4.topleft): None,
                            tuple(dropzone_rect7.topleft): None}
        
        clock = pygame.time.Clock()
        blink_interval = 0  # milliseconds
        blink_timer = 0
        visible = True
        dragging = None
        led_coord=[(750,150),(750,250),(750,350),(750,450)]
        user_led_coord=[(600,215),(600,265),(600,315),(600,365)]
        led_states=[]
        user_led_states=[0,0,0,0]
        zones_op = {}
        seq={}
        i_out=''

        #Main game loop
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
                random_number=random.randint(0,3)
                led_states = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]][random_number]
                # for i in led_states:
                #     print(int(i),end=' ')
                print(led_states)
                visible=False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if submit_button.rect.collidepoint(event.pos):
                        final_output=[int(i) for i in submit_button.click(zones_op,seq)]
                        print(final_output)
                        if(final_output==led_states):
                            return True
                        else:
                            counter+=1

                        if counter==5:
                            return False
                        
                    # if check_button.rect.collidepoint(event.pos):
                    #     dynamic_output=[int(i) for i in check_button.click(zones_op)]
                    #     print(dynamic_output)
                    #     for i,state in enumerate(dynamic_output):
                    #         CIRCLE_COLOR=USER_CIRCLE_COLOR_ON if state else USER_CIRCLE_COLOR_OFF
                    #         pygame.draw.circle(self.screen, CIRCLE_COLOR, user_led_coord[i] , USER_CIRCLE_RADIUS,0)
                            
                    if event.button == 1:
                        for img, img_rect, in_dropzone, img_id, img_code in images:
                            if img_rect.collidepoint(event.pos) and not in_dropzone:
                                dragging = img, img_rect, in_dropzone, img_id, img_code
                                #images.remove((img, img_rect, in_dropzone))

                    if event.button == 1:
                        x,y=event.pos
                        for dot in dots_coord:
                            distance = ((dot[0] - x) ** 2 + (dot[1] - y) ** 2) ** 0.5
                            if distance<DOT_RADIUS:
                                if selected_dot is None:
                                    selected_dot=dot
                                else:
                                    if selected_dot!=dot:
                                        x1,y1=selected_dot
                                        x2,y2=dot
                                        path_choice=random.choice([True,False])
                                        if path_choice:
                                            path1=(selected_dot,(x2,y1))
                                            path2=((x2,y1),dot)
                                        else:
                                            path1=(selected_dot,(x1,y2))
                                            path2=((x1,y2),dot)
                                        lines.extend(path1)
                                        lines.extend(path2)

                                        if selected_dot in dynamic_verification.values():
                                            z=selected_dot
                                            zb=dot
                                        else:
                                            z=dot
                                            zb=selected_dot

                                        for var in variables:
                                            if zb==variables[var]:
                                                variable=var

                                        # if (z in [43,33,23] and zb in [11,12,13]) or (z in [11,12,13] and zb in [43,33,23]):
                                        #     i_out+=1
                                        #     dynamic_connections.extend((i_out,0))
                                        for gate_input in dynamic_verification:
                                            if(z==dynamic_verification[gate_input]):
                                                dynamic_connections.extend((gate_input,variable))
                                    selected_dot=None

                if event.type == pygame.MOUSEMOTION:
                    if dragging is not None:
                        _, img_rect, _, _, _ = dragging
                        img_rect.topleft = event.pos

                if event.type == pygame.MOUSEBUTTONUP:
                    if dragging is not None:
                        img, img_rect, in_dropzone, img_id, img_code = dragging
                        drop_zones = [dropzone_rect1]

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
                                if dropzone_contents[tuple(dropzone_rect.topleft)] :
                                    img_rect.topleft = dropzone_rect.topleft
                                    in_dropzone = True
                                    pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone[i])
                                    dropzone_contents[tuple(dropzone_rect.topleft)] = img
                                    zones_op[i + 1] = dragging[3]
                                    print(f"{dragging[3]} was dropped in Zone {i + 1}")
                                    break
                        else:
                            # Return the image to its original position if no drop zone is available
                            img_rect.topleft = image_original_rect[int(img_code)-1].topleft
                        images.append((img, img_rect, in_dropzone, img_id, img_code))
                        dragging = None

            # Clear the screen
            #self.screen.fill((155, 0, 255))
            self.screen.blit(self.background, (0, 0))

            #print(dynamic_connections)
            present_gates=[i for i in zones_op.keys()]
            #print(present_gates)
            i=j=k=0
            for i in present_gates:
                i_out=''
                for j in dynamic_connections:
                    # if i==1:
                    #     if(j==11 or j==12):
                    #         i_out+=dynamic_connections[dynamic_connections.index(j)+1]
                    #     seq[i]=(i_out,0)
                    
                    #else:
                        if(j==(i*10+1)):
                            flag_check=False
                            for k in dynamic_connections:
                                if(k==(i*10+2)):
                                    flag_check=True
                                    break
                            if flag_check:
                                seq[i]=(dynamic_connections[dynamic_connections.index(i*10+1)+1],dynamic_connections[dynamic_connections.index(i*10+2)+1])

            #print(seq)
            generated_function=self.canonical_function_generation(seq,zones_op)
            dynamic_output=self.functional_output(zones_op,seq)
            j=0
            for i in dynamic_output:
                if i:
                    CIRCLE_COLOR=USER_CIRCLE_COLOR_ON
                else:
                    CIRCLE_COLOR=USER_CIRCLE_COLOR_OFF
                pygame.draw.circle(self.screen, CIRCLE_COLOR, user_led_coord[j] , USER_CIRCLE_RADIUS,0)
                j+=1

            for i,state in enumerate(led_states):
                    CIRCLE_COLOR=CIRCLE_COLOR_ON if state else CIRCLE_COLOR_OFF
                    pygame.draw.circle(self.screen, CIRCLE_COLOR, led_coord[i] , CIRCLE_RADIUS,0)

            for i in range(0,len(lines),2):
                pygame.draw.line(self.screen,LINE_COLOR,lines[i],lines[i+1],LINE_WIDTH)
            for dot in dots_coord:
                if dot==selected_dot:
                    pygame.draw.circle(self.screen,SELECTED_DOT_COLOR,dot,DOT_RADIUS)
                else:
                    pygame.draw.circle(self.screen,DOT_COLOR,dot,DOT_RADIUS)
            #drawing the wires connecting the gates
            # pygame.draw.lines(self.screen, (254, 20, 50), False, ((200,120), (335,120), (335,185)), 5)
            # pygame.draw.lines(self.screen, (254, 20, 50), False, ((200,450), (335,450), (335,380)), 5)
            # pygame.draw.lines(self.screen, (254, 20, 50), False, ((200,250), (335,250), (335,185)), 5)
            # pygame.draw.lines(self.screen, (254, 20, 50), False, ((200,320), (335,320), (335,380)), 5)
            # pygame.draw.lines(self.screen, (254, 20, 50), False, (dropzone_rect2.center, (485,185), dropzone_rect1.center), 5)
            # pygame.draw.lines(self.screen, (254, 20, 50), False, (dropzone_rect3.center, (485,385), dropzone_rect1.center), 5)

            #drawing the rectangles
            pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect1)
            #pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect2)
            #pygame.draw.rect(self.screen, DROPZONE_COLOR, dropzone_rect3)
            pygame.draw.rect(self.screen, ZONE_COLOR, dropzone_rect4)
            pygame.draw.rect(self.screen, ZONE_COLOR, zone_rect5)
            pygame.draw.rect(self.screen, ZONE_COLOR, zone_rect6)
            pygame.draw.rect(self.screen, ZONE_COLOR, dropzone_rect7)


            font_="../Resources/text/Chakra_Petch/ChakraPetch-Medium.ttf"

            try:
            #text of X, X' and Y, Y'
                font=pygame.font.Font(font_,40)
            except(FileNotFoundError):
                font=pygame.font.Font(font_.replace("..","."),40)

            font_small=pygame.font.Font('freesansbold.ttf',15)
            self.screen.blit(font.render("X",True,(0,0,0)),(170,110))
            self.screen.blit(font.render("Y",True,(0,0,0)),(170,310))
            self.screen.blit(font.render("X'",True,(0,0,0)),(170,210))
            self.screen.blit(font.render("Y'",True,(0,0,0)),(170,410))
            self.screen.blit(font_small.render("Function Generated:",True,(0,0,0)),(470,400))
            self.screen.blit(font_small.render(generated_function,True,(0,0,0)),(470,420))


            for img, img_rect, in_dropzone, img_id, img_code in images:
                self.screen.blit(img, img_rect)
                if in_dropzone:
                   pygame.draw.rect(self.screen, DROPZONE_COLOR, img_rect, 2)  # Add a border to indicate in the drop zone

            submit_button.update(pygame.mouse.get_pos())
            submit_button.draw(self.screen)
            # check_button.update(pygame.mouse.get_pos())
            # check_button.draw((self.screen))
            clock.tick(60)
            # Update the display
            pygame.display.flip()

            # Remaining thing to be added is a functional output match so that it returns true or false
            #return True//

        # Quit Pygame
        print(zones_op)
        output=self.functional_output(zones_op,seq)
        for i in output:
            print(int(i),end=' ')
        pygame.quit()
        sys.exit()

        

if __name__=="__main__":
    pygame.init()
    screen=pygame.display.set_mode((800,600))
    level1=level_1(screen)
    level1.run_level()



        

    
    