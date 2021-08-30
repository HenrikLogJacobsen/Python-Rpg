import pygame
from spritesheet import Spritesheet



class scellyenny(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        
        enemy_scelleton = Spritesheet.parse_sprite('')
        self.img = pygame.image.load

 
