import pygame
import time



pygame.init()

width, hight = 1200 , 600
bird_size = 100
bird_x = 10
bird_y = 380
vel = 20
screen = pygame.display.set_mode([width, hight])
pygame.display.set_caption('Flappy Bird - by Noya aberjil')
backgrund= pygame.image.load("background_pic.png")
backgrund = pygame.transform.scale(backgrund, (width, hight))
bird_pic = pygame.image.load("pngegg.png")
bird_pic = pygame.transform.scale(bird_pic, (bird_size, bird_size))


jump_height = 100
jump_speed = 5
gravity = 0.5
is_jumping = False
jump_count = jump_height
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True

    # Object movement
    if is_jumping:
        if jump_count >= -jump_height:
            neg = 1
            if jump_count < 0:
                neg = -1
            bird_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= jump_speed
        else:
            is_jumping = False
            jump_count = jump_height

    # Apply gravity
    if not is_jumping and bird_y < hight - bird_y:
        bird_y += gravity    
    # if keys[pygame.K_LEFT] and bird_x > 0: 
          
    #     bird_x -= vel 
          
    # if keys[pygame.K_RIGHT] and bird_x < width - bird_size: 
          
    #     bird_x += vel 
         
    # if keys[pygame.K_UP] and bird_y > 0: 
          
    #     bird_y -= vel 
          
    # if keys[pygame.K_DOWN] and bird_y < hight - bird_size: 
    #     bird_y += vel 
    screen.blit(backgrund, (0,0))
    screen.blit(bird_pic,(bird_x,bird_y))

    # write text in screen
    txtsurf = font.render("Score:"+str(), True, black)
    screen.blit(txtsurf,(20,20))
    pygame.display.flip()

# Done! Time to quit.

pygame.quit()