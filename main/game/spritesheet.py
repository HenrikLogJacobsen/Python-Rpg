import pygame

class Spritesheet:
    def __init__(self, path):
        self.path = path
        self.sprite_sheet = pygame.image.load(path).convert()

    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))
        return sprite
        
