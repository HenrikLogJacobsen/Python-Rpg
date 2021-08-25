import sys, pygame
from entity import Entity
from map import Map

# Class? + update monitor on resize
monitor = width, height = 720, 480
screen_pos = [0, 0]
white = 255, 255, 255
vel = 2
running = True

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

#GAMELOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        screen_pos[0] += vel
    if keys[pygame.K_RIGHT]:
        screen_pos[0] -= vel
    if keys[pygame.K_UP]:
        screen_pos[1] += vel
    if keys[pygame.K_DOWN]:
        screen_pos[1] -= vel

    # DRAW
    screen.fill(white)
    screen.blit(player.img, player.pos)
    map1.draw(screen_pos)
    pygame.display.flip()
    mainClock.tick(60)
    



