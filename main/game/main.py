import sys, pygame
from player import Player
import math
from ingameGui import GameGui
#from scellyenny import Scellyenny
from map import Map

#dette e den siste versjonen min 


# ___________INIT___________

# Class? + update monitor on resize
monitor = width, height = 720, 480
camera = [0, 0]
ground = 8, 138, 10
vel = 2
running = True
paused = False
time = 0
mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode(monitor, pygame.RESIZABLE)
pygame.display.set_caption("Pukman")

#Flytt disse

#Entities (trenger lettere måte for når vi får mange)
player = Player(monitor)
#step_count = [0, 0, 0, 0]
#enemy = Scellyenny((200,200), 'kuk2.png', 1, 2, player.pos)
#player_health = HealthBar("main/game/media/kuk2.png", [0,0], screen)
map1 = Map("map1", screen)
#map1.forest(-1000, -1000, 100, map1.imgs[0])
gui = GameGui(screen)

# _________FUNCTIONS____________


def redrawGameWindow():
    screen.fill(ground)
    #enemy_pos = enemy.move_towards_player(step_count)
    #screen.blit(enemy.img, enemy_pos)
    player.draw(screen)
    map1.draw(camera)
    gui.draw()

    
# player.pos = 

# ENDRE PLAYERACTION TIL BOOL ARRAY
def keyhandle():
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        if not player.is_touching([-vel, 0], map1.entities):
            player.pos[0] -= vel
            camera[0] -= vel
        player.action = "left"
        
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
        if not player.is_touching([vel, 0], map1.entities):
            player.pos[0] += vel
            camera[0] += vel
        player.action = "right"

    if keys[pygame.K_UP] or keys[pygame.K_w]: 
        if not player.is_touching([0, -vel], map1.entities):
            player.pos[1] -= vel
            camera[1] -= vel
        player.action = "idle"

    if keys[pygame.K_DOWN] or keys[pygame.K_s]: 
        if not player.is_touching([0, vel], map1.entities):
            player.pos[1] += vel
            camera[1] += vel
        player.action = "idle"
    

    # ----- Må oppdateres -----
    #if keys[pygame.K_SPACE]:
    #    player.action = "attacking"


# ___________GAMELOOP_____________
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    if not paused:
        keyhandle()
        redrawGameWindow()
        map1.update(player.pos)
        player.update()
        gui.update(int(time))
        
    if keys[pygame.K_ESCAPE]: paused = not paused

    #if player.is_touching(map1.enemies): 
    #    paused = True
    #    alertText = "Å nei du ble truffet av en ginger"
    #    alert = text_box(alertText, 350, 200, 40)
    #    screen.blit(alert[0], alert[1])

    time = round(pygame.time.get_ticks() / 1000, 2)
    mainClock.tick(60)
    pygame.display.flip()

        



