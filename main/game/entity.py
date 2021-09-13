from math import sqrt      
import pygame

class Entity():
    def __init__(self, img, pos, screen):
        self.screen = screen
        self.img = img
        self.pos = pos
        rect = self.img.get_rect()
        self.rect = rect[2], rect[3]

    def draw(self, camera):
        self.screen.blit(self.img, [self.pos[0] - camera[0], self.pos[1] - camera[1]])
        

class Enemy(Entity):
    def __init__(self, img, pos, screen):
        super().__init__(img, pos, screen)
        self.speed = .5

    def update(self, playerpos):
        dx, dy = playerpos[0] - self.pos[0], playerpos[1] - self.pos[1]
        d = sqrt(dx**2 + dy**2)
        vx, vy = self.speed * dx / d, self.speed * dy / d
        self.pos = [self.pos[0] + vx, self.pos[1] + vy]

class HealthBar(Entity):
    def __init__(self, img, pos, screen):
        super().__init__(img, pos, screen)
        self.img = pygame.load.image(img)

    def draw(self, camera):
        self.screen.blit(self.img, [self.pos[0] - camera[0], self.pos[1] - camera[1]])



        


