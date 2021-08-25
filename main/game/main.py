import sys, pygame
from entity import Entity

mainClock = pygame.time.Clock()
pygame.init()

# Class? + update monitor on resize
monitor = width, height = 720, 480
speed = [0, 0]
white = 255, 255, 255
vel = 2
running = True
player = Entity([0, 0], "intro_ball.gif")
player.center_coord(width / 2, height / 2)
screen = pygame.display.set_mode(monitor, pygame.RESIZABLE)
print(player.rect[2])

pygame.display.set_caption("Pukman")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player.pos[0] -= vel

    if keys[pygame.K_RIGHT]:
        player.pos[0] += vel

    if keys[pygame.K_UP]:
        player.pos[1] -= vel

    if keys[pygame.K_DOWN]:
        player.pos[1] += vel

    screen.fill(white)
    screen.blit(player.img, player.pos)
    pygame.display.flip()
    mainClock.tick(60)



