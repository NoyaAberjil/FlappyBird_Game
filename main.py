import pygame
from pygame import mixer
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width, screen_hight = 564 , 536
running = True 

pipes = []
MAX_PIPES = 6
SCORE = 0

worte = True

ground_scroll = 0
scroll_speed = 3
flappy_vel = 0
start_game = False
jumping = False
game_over = False
touched_pipe = False
flip_pic = False
value_flappy = 0
x_flappy = 100
y_flappy = int(screen_hight / 2)
flappy_cooldown = 0
flappy_moving = 0
uper_bound = 10

x_pipe = 0
y_pipe = 0

font = pygame.font.SysFont("Bauhaus 93", 60)
white = (255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption('Flappy Bird - by Noya aberjil')

#backgrund sound
mixer.music.load("Sounds\\CARNIVAL_bg.mp3")
mixer.music.play(-1)

backgrund= pygame.image.load("Game_pictrues\\bg.png")
ground_scroll_pic = pygame.image.load("Game_pictrues\\ground_scorll.png")
ground_pic = pygame.image.load("Game_pictrues\\ground_pic.png")
button_img = pygame.image.load("Game_pictrues\\restart.png")
button = pygame.Rect(( screen_width // 2 - 50), (screen_hight // 2 - 100 ), button_img.get_size()[0], button_img.get_size()[1])


image_sprite_flappy = [pygame.image.load("Game_pictrues\\bird1.png"),
                pygame.image.load("Game_pictrues\\bird2.png"),
                pygame.image.load("Game_pictrues\\bird3.png")]
pipe = pygame.image.load("Game_pictrues\\pipe.png")
pipe2 = pygame.image.load("Game_pictrues\\pipe_2.png")
pipe3 = pygame.image.load("Game_pictrues\\pipe_3.png")
pipe4 = pygame.image.load("Game_pictrues\\pipe_4.png")
pipe_list = [pipe, pipe2, pipe3, pipe4]

def check_pipes():
    '''
    The function returns True if the pipes list is empty or if the 
    y-coordinate of the last pipe is less than 350, and False otherwise.
    '''
    if len(pipes)==0:
        return True
    elif pipes[-1][1] < 350:
        return True
    else:
        return False
    
def generate_pipes():
    '''
    The function selects a pipe image randomly from pipe_list, 
    potentially flips it based on the flip_pic flag, and appends it to the global pipes list with specific coordinates, 
    toggling the flip_pic flag after each addition if check_players returns true.
    '''
    global pipes
    global flip_pic
    if check_pipes():
        pipe = pipe_list[random.randint(0, len(pipe_list) - 1)]
        if flip_pic:
            # pygame.transform.flip() will flip the image 
            pipe = pygame.transform.flip(pipe, True, False)
            pipe = pygame.transform.flip(pipe, False, True)
            pipes.append([pipe, 564 ,flip_pic ])   
            flip_pic = False
        else: 
            pipes.append([pipe, 564 ,flip_pic ])   
            flip_pic = True
    
def move_pipes():
    '''
    The function updates the horizontal position of each pipe in 
    the global pipes list by decreasing their x-coordinates by the value of scroll_speed.
    '''
    global pipes
    for pipe in pipes:
        pipe[1] -= scroll_speed

def show_pipes():
    '''
    The function iterates over a list of pipes and displays each pipe 
    on the screen, positioning it either at the top or the bottom based on a boolean value.
    '''
    for pipe in pipes:
        if pipe[2]:
            screen.blit(pipe[0], (pipe[1], 0))
        else:
            screen.blit(pipe[0], (pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1]))
        
def remove_pipes():
    '''
    This function removes any pipe from the global list pipes whose x-coordinates is less than -50.
    '''
    global pipes
    
    for pipe in pipes:
        if pipe[1] < -50:
            pipes.remove(pipe)

def check_touch_pipe():
    '''
    This function checks if the Flappy Bird sprite collides with any of the pipes 
    on the screen, returning True if a collision is detected and False otherwise.
    '''
    for pipe in pipes:
        # Get the coordinates of Flappy Bird's bounding box
        flappy_rect = pygame.Rect(x_flappy, y_flappy, image_sprite_flappy[0].get_width(), image_sprite_flappy[0].get_height())

        # Get the coordinates of the pipe's bounding box
        if pipe[2]: 
            pipe_rect = pygame.Rect(pipe[1], 0, pipe[0].get_width(), pipe[0].get_height())
        else:
            pipe_rect = pygame.Rect(pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1], pipe[0].get_width(), pipe[0].get_height())
        # Check for collision between Flappy Bird and the pipe
        if flappy_rect.colliderect(pipe_rect):
            return True  # Collision detected
    return False  # No collision detected

def update_score():
    '''
    The function increments the global SCORE variable each time the Flappy Bird passes a pipe on the screen.
    '''
    global SCORE
    flappy_rect = pygame.Rect(x_flappy, y_flappy, image_sprite_flappy[0].get_width(), image_sprite_flappy[0].get_height())
    for pipe in pipes:
        pipe_rect = pygame.Rect(pipe[1], backgrund.get_size()[1] - pipe[0].get_size()[1], pipe[0].get_width(), pipe[0].get_height())
        if flappy_rect.right > pipe_rect.right and pipe_rect.right + scroll_speed > flappy_rect.right:
            # If Flappy Bird passes the right side of the pipe
            SCORE += 1

def draw_text(text, font, text_col, x, y):
    '''
    This function renders a given text with a specified font and color at the specified (x, y) position on the screen.
    '''
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_button():
    '''
    The draw_button function displays a button image on the screen and returns True if the button is clicked by the user.
    '''
    click_restart = False

    pos = pygame.mouse.get_pos()
    #check if mouse is over the button
    if button.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            click_restart = True
    screen.blit(button_img, button)
    return click_restart

def check_bound():
    '''
    This function checks if the variable y_flappy is less than 10 and returns True if it is, otherwise False.
    '''
    if y_flappy < uper_bound:
        return True
    return False


def write_highScore():
    '''
    This function writes the current high score to a file if it exceeds the previously stored high score.
    '''
    with open("HighScore.txt", "w+") as score_file:
        highscore = score_file.read()

        if len(highscore) > 0:
            highscore = int(highscore)
            if highscore < SCORE:
                score_file.write(str(SCORE))  # Write the new high score
        else:
            score_file.write(str(SCORE))  # Write the new high score

# Run until the user asks to quit
while running:

    clock.tick(fps)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and start_game and jumping and not(check_bound()):
            flappy_vel = -50
            #jump music
            jump_sound = mixer.Sound("Sounds\jumpSuond.wav")
            jump_sound.play()
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
        flappy_vel = 2.7
    else:
        flappy_vel = 0

    screen.blit(bird_image, (x_flappy, y_flappy))
    generate_pipes()
    show_pipes()
    remove_pipes()
    if check_touch_pipe() or y_flappy > 392 :
        game_over = True
        start_game = False
        jumping = False

    if game_over == False and start_game:
        move_pipes()
        update_score()
        ground_scroll -= scroll_speed

        if abs(ground_scroll) > 25:
            ground_scroll = 0

    if game_over:
        if worte:
            write_highScore()
            worte = False
        if draw_button() == True:
            SCORE = 0
            pipes = []
            y_flappy = int(screen_hight / 2)
            game_over = False
            worte = True
            
       
    
    
    flappy_cooldown +=1
    if flappy_cooldown > 5:
       value_flappy += 1
       flappy_cooldown = 0

    draw_text(str(SCORE),font, white,int(screen_width / 2),20)

    pygame.display.update()

pygame.quit()