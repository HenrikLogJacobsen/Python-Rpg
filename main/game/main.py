import sys, pygame
from pygame.constants import KMOD_NONE, TIMER_RESOLUTION
from entity import Entity
from map import Map
from spritesheet import Spritesheet
from player import Player
import math



# Class? + update monitor on resize
monitor = width, height = 720, 480
screen_pos = [width / 2, height / 2]
white = 255, 255, 255
vel = 1.5
running = True

mainClock = pygame.time.Clock()
clock_count = 0 
idle_count = 0
attack_count = 0
pygame.init()
screen = pygame.display.set_mode(monitor, pygame.RESIZABLE)
pygame.display.set_caption("Pukman")

#char sprites
char_anim_sprite = Spritesheet('main/game/media/char_anim.png')
player_running_anim = [char_anim_sprite.parse_sprite("adventurer-run-00.png"), char_anim_sprite.parse_sprite("adventurer-run-01.png"), char_anim_sprite.parse_sprite("adventurer-run-02.png"), char_anim_sprite.parse_sprite("adventurer-run-03.png"), char_anim_sprite.parse_sprite("adventurer-run-04.png"), char_anim_sprite.parse_sprite("adventurer-run-05.png")]
player_idle = [char_anim_sprite.parse_sprite("adventurer-idle-2-00.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-03.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png")]
player_attack = [char_anim_sprite.parse_sprite("adventurer-attack2-00.png"), char_anim_sprite.parse_sprite("adventurer-attack2-01.png"), char_anim_sprite.parse_sprite("adventurer-attack2-02.png"), char_anim_sprite.parse_sprite("adventurer-attack2-03.png"), char_anim_sprite.parse_sprite("adventurer-attack2-04.png"), char_anim_sprite.parse_sprite("adventurer-attack2-05.png"), ]

#sprite groups 
all_sprites = pygame.sprite.Group()
#all_sprites.add(player_running_anim)


#Entities (trenger lettere måte for når vi får mange)
player = Entity([0, 0], "intro_ball.gif", 1)
player.center_coord(width / 2, height / 2)
p1 = Player(screen_pos)
print(p1.pos)

tree_pos = [[-200, 200], [600, 200], [-100, -100], [200, -100]]
map1 = Map("tree.jpg", tree_pos, screen)


def redrawGameWindow(index):

    screen.fill('white')
    map1.draw(screen_pos)

    if LEFT:
        screen.blit(pygame.transform.flip(player_running_anim[math.floor(index)], True, False),(player.pos))

    if RIGHT:
        screen.blit(player_running_anim[math.floor(index)],(player.pos))
    
    if MOVING == False: 
        screen.blit(player_idle[math.floor(index)],(player.pos))

    if ATTACK: 
        if LEFT == True:
            screen.blit(pygame.transform.flip(player_attack[math.floor(index)], True, False), (player.pos))
        else:
            screen.blit(player_attack[math.floor(index)], player.pos)

action = False
index = 0
ATTACK = False
MOVING = False
RIGHT = False
LEFT = False

#GAMELOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
<<<<<<< HEAD
=======



>>>>>>> 93995a0b440a63d15d06256ecfdbcb769d303b3f
    if keys[pygame.K_LEFT]:
        screen_pos[0] += vel
        RIGHT = False
        LEFT = True
        MOVING = True
        index = (index + 0.1) % len(player_running_anim)

    if keys[pygame.K_RIGHT]:
        screen_pos[0] -= vel
        RIGHT = True
        LEFT = False
        MOVING = True
        index = (index + 0.1) % len(player_running_anim)

    if keys[pygame.K_UP]:
        screen_pos[1] += vel
    if keys[pygame.K_DOWN]:
        screen_pos[1] -= vel
    
    if keys[pygame.K_SPACE]:
        ATTACK = True


    



    # DRAW
    index = index+0.1 % len(player_idle)
    if index >= 6:
        index = 0
    
    mainClock.tick(60)
    redrawGameWindow(index)
    pygame.display.flip()

    action = False
    LEFT = False
    RIGHT = False
    ATTACK = False
    MOVING  = False
        



