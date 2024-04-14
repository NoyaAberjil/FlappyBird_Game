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
start_game = False
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

def check_touch_pipe(flappy_y, flappy_x):
    for pipe in pipes:
        # Get the coordinates of Flappy Bird's bounding box
        flappy_rect = pygame.Rect(flappy_x, flappy_y, image_sprite_flappy[0].get_width(), image_sprite_flappy[0].get_height())
        # Get the coordinates of the pipe's bounding box
        pipe_rect = pygame.Rect(pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1], pipe[0].get_width(), pipe[0].get_height())
        # Check for collision between Flappy Bird and the pipe
        if flappy_rect.colliderect(pipe_rect):
            return True  # Collision detected
    return False  # No collision detected

# def check_score():
#     global SCORE
#     pass_pipe = False
    
#     if len(pipes) > 0:
#         if flappy_rect.left() >
# Run until the user asks to quit
while running:

    clock.tick(fps)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start_game and jumping:
            flappy_vel = -40
        if event.type == pygame.MOUSEBUTTONDOWN and start_game == False:
            start_game = True
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
        start_game = False
        jumping = False
    if start_game:
        flappy_vel = 2
    else:
        flappy_vel = 0

    screen.blit(bird_image, (x_flappy, y_flappy))
    generatePalyers()
    show_players()
    remove_players()
    if game_over == False and start_game and not check_touch_pipe(y_flappy, x_flappy):
        move_pipes()
        ground_scroll -= scroll_speed

        if abs(ground_scroll) > 25:
            ground_scroll = 0
    else:
        jumping = False
    
    
    flappy_cooldown +=1
    if flappy_cooldown > 5:
       value_flappy += 1
       flappy_cooldown = 0


    pygame.display.update()

pygame.quit()