import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width, screen_hight = 564 , 536
running = True 

screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption('Flappy Bird - by Noya aberjil')

backgrund= pygame.image.load("bg.png")
ground_scroll_pic = pygame.image.load("ground_scorll.png")
ground_pic = pygame.image.load("ground_pic.png")

image_sprite_flappy = [pygame.image.load("bird1.png"),
                pygame.image.load("bird2.png"),
                pygame.image.load("bird3.png")]
value_flappy = 0
x_flappy = 100
y_flappy = int(screen_hight / 2)
flappy_cooldown = 0
flappy_moving = 0

x_pipe = 0
y_pipe = 0
image_pipe = pygame.image.load("pipe.png")


ground_scroll = 0
scroll_speed = 3


flappy_vel = 2
jumping = False

# Run until the user asks to quit
while running:

    clock.tick(fps)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()  
    
    keys = pygame.key.get_pressed()  
    
    if keys[pygame.K_SPACE]:
        flappy_vel = -10

    else:
        if value_flappy >= len(image_sprite_flappy):
            value_flappy = 0
        bird_image = image_sprite_flappy[value_flappy]

        if y_flappy > 392 :
            flappy_vel = 0
        else:
            flappy_vel = 2
    y_flappy += flappy_vel

    screen.blit(backgrund, (0,0)) #draw background
    screen.blit(ground_pic, (0,428))
    screen.blit(ground_scroll_pic, (ground_scroll,428))
    screen.blit(bird_image, (x_flappy, y_flappy + flappy_vel))
    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 25:
        ground_scroll = 0
    
    flappy_cooldown +=1
    if flappy_cooldown > 5:
       value_flappy += 1
       flappy_cooldown = 0


    pygame.display.update()

pygame.quit()