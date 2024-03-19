import pygame
import time



pygame.init()

w, h = 1200 , 600
screen = pygame.display.set_mode([w, h])
pygame.display.set_caption('Flappy Bird - by Noya aberjil')
backgrund= pygame.image.load("background_pic.png")
backgrund = pygame.transform.scale(backgrund, (w, h))

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

    # Fill the background with white
    screen.blit(backgrund, (0,0))
    # write text in screen
    txtsurf = font.render("Score:"+str(), True, black)
    screen.blit(txtsurf,(380,10))
    pygame.display.flip()

# Done! Time to quit.

pygame.quit()