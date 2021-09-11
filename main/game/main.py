import sys, pygame
from player import Player
import math
from ingameGui import text_box
from scellyenny import Scellyenny
from map import Map

# Class? + update monitor on resize
monitor = width, height = 720, 480
screen_pos = [width / 2, height / 2]
white = 255, 255, 255
vel = 2
running = True

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(monitor, pygame.RESIZABLE)
pygame.display.set_caption("Pukman")

#Entities (trenger lettere måte for når vi får mange)
player = Player(screen_pos)

enemy = Scellyenny((200,200), 'kuk2.png', 1, 2, screen_pos)

map1 = Map("map1", screen)

def redrawGameWindow():
    screen.fill('white')
    enemy_pos = enemy.move_towards_player(player.pos)
    screen.blit(enemy.img, enemy_pos)
    player.draw(screen)
    map1.draw(player.pos)

    

#GAMELOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player.pos[0] += vel
        player.action = "left"

    if keys[pygame.K_RIGHT]:
        player.pos[0] -= vel
        player.action = "right"

    if keys[pygame.K_UP]:
        player.pos[1] += vel
        player.action = "idle"

    if keys[pygame.K_DOWN]:
        player.pos[1] -= vel
        player.action = "idle"
    
    # ----- Må oppdateres -----
    #if keys[pygame.K_SPACE]:
    #    player.action = "attacking"

    
    mainClock.tick(60)
    redrawGameWindow()
    player.update()
    
    pygame.display.flip()
        



