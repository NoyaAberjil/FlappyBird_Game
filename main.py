import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width, screen_hight = 564 , 536
running = True 

font = pygame.font.SysFont("Bauhaus 93", 60)
white = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption('Flappy Bird - by Noya aberjil')


backgrund= pygame.image.load("bg.png")
ground_scroll_pic = pygame.image.load("ground_scorll.png")
ground_pic = pygame.image.load("ground_pic.png")
button_img = pygame.image.load("restart.png")
button = pygame.Rect(( screen_width // 2 - 50), (screen_hight // 2 - 100 ), button_img.get_size()[0], button_img.get_size()[1])


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
scroll_speed = 1


flappy_vel = 0
start_game = False
jumping = False
game_over = False
touched_pipe = False
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

def check_touch_pipe():
    for pipe in pipes:
        # Get the coordinates of Flappy Bird's bounding box
        flappy_rect = pygame.Rect(x_flappy, y_flappy, image_sprite_flappy[0].get_width(), image_sprite_flappy[0].get_height())

        # Get the coordinates of the pipe's bounding box
        pipe_rect = pygame.Rect(pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1], pipe[0].get_width(), pipe[0].get_height())
        # Check for collision between Flappy Bird and the pipe
        if flappy_rect.colliderect(pipe_rect):
            return True  # Collision detected
    return False  # No collision detected


def check_score():
    global SCORE
    pass_pipe = False
    flappy_rect = pygame.Rect(x_flappy, y_flappy, image_sprite_flappy[0].get_width(), image_sprite_flappy[0].get_height())
    if len(pipes) > 0:
        for pipe in pipes:
            pipe_rect = pygame.Rect(pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1], pipe[0].get_width(), pipe[0].get_height())
            if (flappy_rect.left > pipe_rect.left) and (flappy_rect.right < pipe_rect.right + 3) and pass_pipe == False:
                pass_pipe = True
            if pass_pipe:
                if flappy_rect.left > pipe_rect.left:
                    SCORE += 1
                    pass_pipe = False

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_button():
    click_restart = False

    pos = pygame.mouse.get_pos()
    #check if mouse is over the button
    if button.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            click_restart = True
    screen.blit(button_img, button)
    return click_restart

def reset_game():
    global pipes
    pipes = []

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
    if check_touch_pipe() or y_flappy > 392 :
        game_over = True
        start_game = False
        jumping = False

    if game_over == False and start_game:
        move_pipes()
        check_score()
        ground_scroll -= scroll_speed

        if abs(ground_scroll) > 25:
            ground_scroll = 0

    if game_over:
        if draw_button() == True:
            SCORE = 0
            pipes = []
            y_flappy = int(screen_hight / 2)
            game_over = False
            
       
    
    
    flappy_cooldown +=1
    if flappy_cooldown > 5:
       value_flappy += 1
       flappy_cooldown = 0

    draw_text(str(SCORE),font, white,int(screen_width / 2),20)

    pygame.display.update()

pygame.quit()