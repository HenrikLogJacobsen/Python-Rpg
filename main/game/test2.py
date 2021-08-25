import pygame 
import sys
import buttons
from pygame.constants import QUIT

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDHT = 800
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDHT))
screen.fill((202, 228, 241))
start_img = pygame.image.load('/Users/jonasolsen/Documents/GitHub/start.png').convert_alpha()

start_button = buttons.Button(100, 200, start_img, 0.7)



run = True 
while run:
    
    screen.fill((202, 228, 241))

    #draw_button = buttons.Button.draw(screen)
    if start_button.draw(screen) == True:
        print('kuk')


    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            pygame.quit
    
    pygame.display.update()


        

       




        
