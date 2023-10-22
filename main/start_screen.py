import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("CodeDiffuse")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('player2.png')
playerX = 100;
playerY = 150;

def player(x,y):
    screen.blit(playerimg,(x,y))

x = playerX;
y = playerY;
running = True
change = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("Right")
                change = 0.1
            if event.key == pygame.K_LEFT:
                print("Left")
                change = -0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT  or event.key == pygame.K_LEFT:
                print("Released")
                change = 0
    screen.fill((0, 0, 0))
    x += change
    if x<0:
        x = 0
    if x>736:
        x = 736
    player(x, y)


    pygame.display.update()
