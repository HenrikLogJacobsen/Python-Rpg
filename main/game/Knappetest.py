
import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

start_img = pygame.image.load('/Users/jonasolsen/Documents/GitHub/start.png')

class Button():
    #lager selve knappen
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False


    #tegner den på screen
    def draw(self):

        action = False

        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 1: 
            self.clicked = False
        
        
        


        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

start_button = Button(100, 200, start_img, 0.7)






run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw() == True: 
        print('start')



    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update()










    





