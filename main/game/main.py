import sys, pygame
from map import Map
from player import Player
import math
from ingameGui import text_box



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

#char sprites
char_anim_sprite = Spritesheet('main/game/media/char_anim.png')
player_running_anim = [char_anim_sprite.parse_sprite("adventurer-run-00.png"), char_anim_sprite.parse_sprite("adventurer-run-01.png"), char_anim_sprite.parse_sprite("adventurer-run-02.png"), char_anim_sprite.parse_sprite("adventurer-run-03.png"), char_anim_sprite.parse_sprite("adventurer-run-04.png"), char_anim_sprite.parse_sprite("adventurer-run-05.png")]
player_idle = [char_anim_sprite.parse_sprite("adventurer-idle-2-00.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-03.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png")]
player_attack = [char_anim_sprite.parse_sprite("adventurer-attack2-00.png"), char_anim_sprite.parse_sprite("adventurer-attack2-01.png"), char_anim_sprite.parse_sprite("adventurer-attack2-02.png"), char_anim_sprite.parse_sprite("adventurer-attack2-03.png"), char_anim_sprite.parse_sprite("adventurer-attack2-04.png"), char_anim_sprite.parse_sprite("adventurer-attack2-05.png"), ]




#sprite groups 
all_sprites = pygame.sprite.Group()
#all_sprites.add(player_running_anim)


#Entities (trenger lettere måte for når vi får mange)
player = Player(screen_pos)
print(player.pos)

tree_pos = [[-200, 200], [600, 200], [-100, -100], [200, -100]]
map1 = Map("tree.jpg", tree_pos, screen)


def redrawGameWindow():

    screen.fill('white')
    player.draw(screen)
    map1.draw(player.pos)
    screen.blit(totalText[0], totalText[1])
    

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
        



