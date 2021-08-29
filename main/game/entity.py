import pygame

class Entity:
    def __init__(self, start_pos, path):
        self.start_pos = start_pos
        self.pos = [0,0]
        self.path = "main/game/media/" + path
        self.img = pygame.image.load(self.path)
        self.img = pygame.transform.scale(self.img, (50,50))
        self.rect = self.img.get_rect()

    def center_coord(self, x, y):
        self.pos = [x - (self.rect[2] / 2), y - (self.rect[2] / 2)]






        


