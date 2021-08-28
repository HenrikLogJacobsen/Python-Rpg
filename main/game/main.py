import sys, pygame
from pygame.constants import TIMER_RESOLUTION
from entity import Entity
from map import Map

# Class? + update monitor on resize
monitor = width, height = 720, 480
screen_pos = [0, 0]
white = 255, 255, 255
vel = 2
running = True

#char gåing sprite (bare venstre t nå)
player_left_walk = [pygame.image.load('main/game/media/L1.png'), pygame.image.load('main/game/media/L2.png' ), pygame.image.load('main/game/media/L3.png'), pygame.image.load('main/game/media/L4.png'), pygame.image.load('main/game/media/L5.png')]
player_idle = pygame.image.load('main/game/media/idle1')


#SETUP
mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(monitor, pygame.RESIZABLE)
pygame.display.set_caption("Pukman")

#Entities (trenger lettere måte for når vi får mange)
player = Entity([0, 0], "intro_ball.gif")
player.center_coord(width / 2, height / 2)

tree_pos = [[-200, 200], [300, 200], [-100, -100], [200, -100]]
map1 = Map("tree.jpg", tree_pos, screen)

def redrawGameWindow():

    screen.blit(player_idle)

    if LEFT:
        screen.blit(player_left_walk//3,(width / 2, height / 2))

    elif RIGHT:
        screen.blit(player_left_walk//3,(width / 2, height / 2))
    
    else: 
        screen.blit(player_idle,(width / 2, height / 2))




RIGHT = False
LEFT = True

#GAMELOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        screen_pos[0] += vel
        RIGHT = False
        LEFT = True

    elif keys[pygame.K_RIGHT]:
        screen_pos[0] -= vel
        RIGHT = True
        LEFT = False

    elif keys[pygame.K_UP]:
        screen_pos[1] += vel
    elif keys[pygame.K_DOWN]:
        screen_pos[1] -= vel

    else:
        RIGHT = False
        LEFT = False

    # DRAW
    screen.fill(white)
    screen.blit(player.img, player.pos)
    map1.draw(screen_pos)
    pygame.display.flip()
    mainClock.tick(18)
        



