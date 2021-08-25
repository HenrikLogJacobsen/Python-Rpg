import pygame 
import sys
from buttons import Button
from pygame.constants import QUIT

pygame.init()

SCREEN_HEIGHT = 500
SCREEN_WIDHT = 800
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDHT))
screen.fill((202, 228, 241))
start_img = pygame.image.load('/Users/jonasolsen/Documents/GitHub/start.png').convert_alpha()
class cutton:
    
    def __init__(self, x, y, image):
        
        self.image = image
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


start_button = cutton(100, 200, start_img)



running = True 
while running:
    
    screen.fill((202, 228, 241))



    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit
        

       




        
