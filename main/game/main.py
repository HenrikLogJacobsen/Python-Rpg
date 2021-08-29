import sys, pygame
from pygame.constants import KMOD_NONE, TIMER_RESOLUTION
from entity import Entity
from map import Map
from spritesheet import Spritesheet



# Class? + update monitor on resize
monitor = width, height = 720, 480
screen_pos = [0, 0]
white = 255, 255, 255
vel = 2
running = True

mainClock = pygame.time.Clock()
clock_count = 0 
idle_count = 0
attack_count = 0
pygame.init()
screen = pygame.display.set_mode(monitor, pygame.RESIZABLE)
pygame.display.set_caption("Pukman")

#char sprites
char_anim = Spritesheet('main/game/media/char_anim.png')
#running_anim = 

player_right_walk = [pygame.image.load('main/game/media/run1.png').convert_alpha(), pygame.image.load('main/game/media/run2.png'), pygame.image.load('main/game/media/run3.png'), pygame.image.load('main/game/media/run4.png'), pygame.image.load('main/game/media/run5.png'), pygame.image.load('main/game/media/run6.png').convert_alpha()]
player_left_walk = []
player_idle = [pygame.image.load('main/game/media/idle1.png').convert_alpha(), pygame.image.load('main/game/media/idle2.png').convert_alpha(), pygame.image.load('main/game/media/idle3.png').convert_alpha(), pygame.image.load('main/game/media/idle4.png').convert_alpha()]
for i in range(0, len(player_right_walk)):
    player_left_walk.append(pygame.transform.flip(player_right_walk[i], True, False))

player_attack = [pygame.image.load('main/game/media/attack1.png').convert_alpha(), pygame.image.load('main/game/media/attack2.png').convert_alpha(), pygame.image.load('main/game/media/attack3.png').convert_alpha(), pygame.image.load('main/game/media/attack4.png').convert_alpha(), pygame.image.load('main/game/media/attack5.png').convert_alpha()]


#Entities (trenger lettere måte for når vi får mange)
player = Entity([0, 0], "intro_ball.gif")
player.center_coord(width / 2, height / 2)


tree_pos = [[-200, 200], [300, 200], [-100, -100], [200, -100]]
map1 = Map("tree.jpg", tree_pos, screen)

def redrawGameWindow():

    screen.fill('white')
    map1.draw(screen_pos)

    player_hitbox = player_left_walk[1].get_rect()


    if LEFT:
        screen.blit(char_anim.get_sprite(1, 313, 50, 37),(player.pos))

    if RIGHT:
        screen.blit(player_right_walk[clock_count],(player.pos))
    
    if MOVING == False: 
        screen.blit(player_idle[idle_count],(player.pos))

    if ATTACK: 
        screen.blit(player_attack[attack_count], player.pos)



ATTACK = False
MOVING = False
RIGHT = False
LEFT = False

#GAMELOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        screen_pos[0] += vel
        RIGHT = False
        LEFT = True
        MOVING = True

    if keys[pygame.K_RIGHT]:
        screen_pos[0] -= vel
        RIGHT = True
        LEFT = False
        MOVING = True

    if keys[pygame.K_UP]:
        screen_pos[1] += vel
    if keys[pygame.K_DOWN]:
        screen_pos[1] -= vel
    
    if keys[pygame.K_SPACE]:
        ATTACK = True
        RIGHT = False
        LEFT = False
        MOVING = False

    



    # DRAW
    mainClock.tick(12)
    clock_count += 1
    idle_count += 1
    attack_count += 1 
    redrawGameWindow()
    pygame.display.flip()

    if clock_count == 5:
        clock_count = 0

    if idle_count == 3:
        idle_count = 0 
    
    if attack_count == 4:
        attack_count = 0

    MOVING = False
    RIGHT = False
    LEFT = False
    ATTACK = False

        



