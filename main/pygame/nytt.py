import pygame, sys
from pygame.locals import *
import random, time


def main(): 
    pygame.init()

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    SPEED = 5 
    SCORE = 0


    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.fill('white')
    pygame.display.set_caption('Game')

    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('main/kuk2.png')
            self.surf = pygame.Surface((50, 80))
            self.rect = self.surf.get_rect(center = (random.randint(40, SCREEN_WIDTH-40), 0))

        def move(self):
            self.rect.move_ip(0, SPEED)
            if (self.rect.bottom > 600):
                self.rect.top = 0
                self.rect.center = (random.randint(30, 370), 0)
        

    
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load('main/kuk1.png')
            self.surf = pygame.Surface((50, 100))
            self.rect = self.surf.get_rect(center = (150, 500))

        def move(self):
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 5)

            if self.rect.left > 0: 
                if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5, 0)
            
            if self.rect.right < 400:
                if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5,0)
            
        

    P1 = Player()
    E1 = Enemy()

    enemies = pygame.sprite.Group()
    enemies.add(E1)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)
    all_sprites.add(E1)

    INC_SPEED = pygame.USEREVENT + 1 
    pygame.time.set_timer(INC_SPEED, 1000)



    #fps styring 
    FPS = 60
    FramePerSec = pygame.time.Clock()
 


    while True:
        
        for event in pygame.event.get():
            if event.type == INC_SPEED:
                SPEED += 2 

            if event.type == QUIT:
                pygame.quit()
        
        screen.fill('white')

        #beveger og tegner sprites på nytt 
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)
            entity.move()
        
        #denne løkken kjører dersom player og enemy kolliderer
        if pygame.sprite.spritecollideany(P1, enemies):
            screen.fill('red')
            pygame.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            pygame.quit()


        pygame.display.update()
        FramePerSec.tick(FPS)


main()
