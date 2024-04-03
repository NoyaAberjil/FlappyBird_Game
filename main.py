import pygame
from pygame.locals import *
import random

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
pipe = pygame.image.load("pipe.png")
pipe2 = pygame.image.load("pipe_2.png")
pipe3 = pygame.image.load("pipe_3.png")
pipe4 = pygame.image.load("pipe_4.png")
pipe_list = [pipe, pipe2, pipe3, pipe4]
pipes = []
MAX_PIPES = 4


ground_scroll = 0
scroll_speed = 1


flappy_vel = 2
jumping = False

def check_players():
    global pipes
    if len(pipes)==0:
        return True
    elif pipes[0][1] < 330:     
        return True
    else:
        return False
        
def generatePalyers():
    global pipes
    global pipe_list

    if check_players() and (len(pipes) < MAX_PIPES):
        pipe = pipe_list[random.randint(0, len(pipe_list) - 1)]
        pipes.append([pipe, 426])

def move_pipes():
    global pipes
    for pipe in pipes:
        pipe[1] -= scroll_speed

def show_players():
    global screen
    global pipes
    global backgrund

    print(pipes)
    for pipe in pipes:
        screen.blit(pipe[0], (pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1]))

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
    move_pipes()
    generatePalyers()
    show_players()

    ground_scroll -= scroll_speed

    if abs(ground_scroll) > 25:
        ground_scroll = 0
    
    flappy_cooldown +=1
    if flappy_cooldown > 5:
       value_flappy += 1
       flappy_cooldown = 0


    pygame.display.update()

pygame.quit()