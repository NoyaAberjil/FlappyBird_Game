import pygame
import time



pygame.init()

width, hight = 1200 , 600
bird_size = 100
bird_x = 10
bird_y = 380
vel = 20
jumping = False
Y_GRAVITY = 1
JUMP_HIGHT = 20
Y_VELCITY = JUMP_HIGHT
screen = pygame.display.set_mode([width, hight])
pygame.display.set_caption('Flappy Bird - by Noya aberjil')
backgrund= pygame.image.load("background_pic.png")
backgrund = pygame.transform.scale(backgrund, (width, hight))
bird_pic = pygame.image.load("pngegg.png")
bird_pic = pygame.transform.scale(bird_pic, (bird_size, bird_size))




# Run until the user asks to quit
running = True
black=(0,0,0)
white=(255,255,255)
font = pygame.font.SysFont("Arial", 26)
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()  

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_SPACE]:
        jumping = True

    screen.blit(backgrund, (0,0))

    if jumping:
        bird_y -= Y_VELCITY
        Y_VELCITY -= Y_GRAVITY
        if Y_VELCITY < -JUMP_HIGHT:
            jumping = False
            Y_VELCITY = JUMP_HIGHT 
        screen.blit(bird_pic,(bird_x,bird_y))
    else:
        screen.blit(bird_pic,(bird_x,bird_y))


    # write text in screen
    txtsurf = font.render("Score:"+str(), True, black)
    screen.blit(txtsurf,(20,20))
    pygame.display.flip()

# Done! Time to quit.

pygame.quit()