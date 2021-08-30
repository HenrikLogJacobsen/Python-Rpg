import sys, pygame
from map import Map
from player import Player
import math
from ingameGui import text_box
from scellyenny import Scellyenny

print('henrik kan sje kode')
print("heehee")

print('tissefant')



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

enemy = Scellyenny((200,200), 'kuk2.png', 1, 0.5)


tree_pos = [[-200, 200], [600, 200], [-100, -100], [200, -100]]
map1 = Map("tree.jpg", tree_pos, screen)


def redrawGameWindow():
    screen.fill('white')
    screen.blit(enemy.img, enemy.pos)
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
    enemy.move_towards_player(player.pos)
    pygame.display.flip()
        



