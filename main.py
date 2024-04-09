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
MAX_PIPES = 6


ground_scroll = 0
scroll_speed = 4


flappy_vel = 0
jumping = False
game_over = False

SCORE = 0

def check_players():
    if len(pipes)==0:
        return True
    elif pipes[-1][1] < 450:     
        return True
    else:
        return False
        
def generatePalyers():
    global pipes
    
    if check_players():
        pipe = pipe_list[random.randint(0, len(pipe_list) - 1)]
        pipes.append([pipe, 564])

def move_pipes():
    global pipes
    for pipe in pipes:
        pipe[1] -= scroll_speed

def show_players():
    for pipe in pipes:
        screen.blit(pipe[0], (pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1]))
        
def remove_players():
    global pipes
    
    for pipe in pipes:
        if pipe[1] < -50:
            pipes.remove(pipe)

def check_game_over(flappy_y, flappy_x,):
    end_game = False
    size_of_pipe = 50
    for pipe in pipes:
        if backgrund.get_size()[1] - pipe[0].get_size()[1] > flappy_y and pipe[1] < flappy_x < pipe[1] + size_of_pipe:
            end_game = True
            break
    
    return end_game

# Run until the user asks to quit
while running:

    clock.tick(fps)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key== pygame.K_SPACE and jumping:
            # print(event)
            flappy_vel = -40
            print(flappy_vel)
        if event.type == pygame.MOUSEBUTTONDOWN and jumping == False:
            jumping = True


        if value_flappy >= len(image_sprite_flappy):
            value_flappy = 0
        bird_image = image_sprite_flappy[value_flappy]

    screen.blit(backgrund, (0,0)) #draw background
    screen.blit(ground_pic, (0,428))
    screen.blit(ground_scroll_pic, (ground_scroll,428))

    y_flappy += flappy_vel
    if y_flappy > 392 :
        flappy_vel = 0
        game_over = True
        jumping = False
    if jumping:
        flappy_vel = 2
    else:
        flappy_vel = 0

    screen.blit(bird_image, (x_flappy, y_flappy))
    generatePalyers()
    show_players()
    remove_players()
    if game_over == False and jumping:
        move_pipes()
        ground_scroll -= scroll_speed

        if abs(ground_scroll) > 25:
            ground_scroll = 0
    
    flappy_cooldown +=1
    if flappy_cooldown > 5:
       value_flappy += 1
       flappy_cooldown = 0


    pygame.display.update()

pygame.quit()