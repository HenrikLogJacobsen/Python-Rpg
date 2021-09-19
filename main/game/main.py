from entity import Enemy
import sys, pygame
from pygame.math import Vector2
from player import Player
import math
from ingameGui import text_box
#from scellyenny import Scellyenny
from map import Map
import time
import numpy as np




# ___________INIT___________

# Class? + update monitor on resize
monitor = width, height = 720, 480
camera = [0, 0]
ground = 8, 138, 10
vel = 2
running = True
paused = False

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(monitor, pygame.RESIZABLE)
pygame.display.set_caption("Pukman")

#Flytt disse
map_box = text_box("map1", 30, 15, 20)

#Entities (trenger lettere måte for når vi får mange)
player = Player(monitor)
#step_count = [0, 0, 0, 0]
#enemy = Scellyenny((200,200), 'kuk2.png', 1, 2, player.pos)
#player_health = HealthBar("main/game/media/kuk2.png", [0,0], screen)
map1 = Map("map1", screen)

# _________FUNCTIONS____________
def raycasting(playerpos, entities):
    startpos = [monitor[0] / 2 , monitor[1] / 2]
    dist = 100
    ents = [map1.test_rects]
    print(ents)
    rays = []
    
    if player.action == 'left':

        for i in range(0, 480, 100):

            ray = pygame.draw.line(screen, 'blue', startpos, (0, i), 5)
    
            if len(rays) < 480/5:
                rays.append(ray)
            

    if player.action == 'right':

        for i in range(0, 480, 5):

            ray = pygame.draw.line(screen, 'blue', startpos, (width, i), 5)
    
            if len(rays) < 480/5:
                rays.append(ray)

    if player.action == 'up':

        for i in range(120, 600, 5):

            ray = pygame.draw.line(screen, 'blue', startpos, (i, 0), 5)
    
            if len(rays) < 480/5:
                rays.append(ray)

    if player.action == 'down':

        for i in range(120, 600, 5):

            ray = pygame.draw.line(screen, 'blue', startpos, (i, height), 5)
    
            if len(rays) < 480/5:
                rays.append(ray)

        


    #for e in entities:

        #ents.append(e[0].get_rect())


    #print(pygame.Rect.collidelist(ray, ents))

            




        
        
    


def redrawGameWindow():
    screen.fill(ground)
    #enemy_pos = enemy.move_towards_player(step_count)
    #screen.blit(enemy.img, enemy_pos)
    player.draw(screen)
    map1.draw(camera)
    screen.blit(map_box[0], map_box[1])
    
# player.pos = sentrert på skjermen, midten av camera boks
# camera = firkantens posisjon på map, det du ser 

def keyhandle(ATTACK, LEFT, RIGHT, DOWN, UP):
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        player.pos[0] -= vel
        camera[0] -= vel
        player.action = "left"
        LEFT = True

    if keys[pygame.K_RIGHT]:
        player.pos[0] += vel
        camera[0] += vel
        player.action = "right"
        RIGHT = True
    
    if keys[pygame.K_UP]:
        player.pos[1] -= vel
        camera[1] -= vel
        player.action = "up"
        UP = True

    if keys[pygame.K_DOWN]:
        player.pos[1] += vel
        camera[1] += vel
        player.action = "down"
        DOWN = True  

    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        player.action = "left-up"
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        player.action = "right-up"
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        player.action = "left-down"
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        player.action = "right-down"
    


    if keys[pygame.K_SPACE]:
        player.action = "attacking"
        ATTACK = True
    
    return ATTACK, RIGHT, LEFT, UP, DOWN
    


# ___________GAMELOOP_____________
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()

    if not paused:
        ATTACK = False
        LEFT = False
        RIGHT = False
        DOWN = False
        UP = False
        keyhandle(ATTACK, LEFT, RIGHT, DOWN, UP)
        redrawGameWindow()
        map1.update(player.pos)
        #raycasting(player.pos, map1.entities)
        player.update()
     
        
    if keys[pygame.K_ESCAPE]: paused = not paused

    if player.is_touching(map1.enemies): 
        paused = True

        alertText = "Å nei du ble truffet!"
        alert = text_box(alertText, 350, 200, 40)
        screen.blit(alert[0], alert[1])

    
    mainClock.tick(60)
    pygame.display.flip()

        



