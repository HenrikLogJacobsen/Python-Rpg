import pygame
from pygame import time
from pygame.sprite import Sprite
r = pygame.Rect

#legger til bevegelse til smiley
#må definere step lengde, hvor langt den beveger seg per frame. 
#definerer også plasseringen til smiley i variabler som oppdateres.


def main():
    pygame.init()

    xpos = 50
    ypos = 50

    step_x = 1
    step_y = 1

    screen_width = 1000
    screen_height = 700

    screen = pygame.display.set_mode((screen_width,screen_height))

    screen.fill(('pink')) #fyller skjermen med rødt. 

    image = pygame.image.load('main/kuk2.png')
    #screen.blit(image, (xpos,ypos)) #tallene representerer plassen på bildet på skjermen. må overlappe med screen du opretter
    image.set_colorkey((255,255,255)) #tar vekk alle pixler i bildet med fargekode (255, 0, 255)
    image.set_alpha(250) #transparancy, lavt tall veldig gjennomsiktig 

    screen.blit(image, (xpos,ypos)) #displayet bygger lag, altså for at bildet skal syntes må det bli printet på etter den er farget rød 
    
    #legger inn if setninger som oppdaterer posisjonen på smiley for hver gang main loopen kjøres. 
    if xpos > screen_width -64 or xpos< 0:
        step_x = -step_x
    if ypos > screen_height -64 or ypos < 0:
        step_y = -step_y
    #selve oppdatering: 
    xpos += step_x
    ypos += step_y
    screen.blit(image, (xpos, ypos))


    pygame.display.flip()
    
    clock = pygame.time.Clock()
    fps = 1
    pygame.key.set_repeat(500,30)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        if xpos > screen_width -64 or xpos< 0:
            step_x = -step_x
        if ypos > screen_height -64 or ypos < 0:
            step_y = -step_y
        #selve oppdatering: 
        xpos += step_x
        ypos += step_y
        screen.fill('pink') #denne linjen legger nytt lag med farge over alt annet slik at det skjuler forrige bilde og dermedfår det til å se ut som den beveger seg rundt 
        screen.blit(image, (xpos, ypos))
        pygame.display.flip()
        
        clock.tick(fps)


if __name__=="__main__":
    main()
