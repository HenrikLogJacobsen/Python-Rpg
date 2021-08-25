import pygame 
pygame.init() 
screen = pygame.display.set_mode((1200,600)) 
myfont = 'timesnewromanbold'
mytext = myfont.render('Hello world', 1, (255, 100, 100)) 
running = True
while running: 
  for event in pygame.event.get(): 
    if event.type==pygame.QUIT: 
      running=False

  screen.fill((255, 255, 255)) 
  screen.blit(mytext, (600, 300)) 
  pygame.display.flip()

pygame.quit()