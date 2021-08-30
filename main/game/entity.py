import pygame

class Entity:
    def __init__(self, start_pos, path, scale, screen):
        self.screen = screen
        self.start_pos = start_pos
        self.pos = [0,0]
        self.path = "main/game/media/" + path
        self.img = pygame.image.load(self.path)
        self.img = pygame.transform.scale(self.img, (int(self.img.get_width() * scale), int(self.img.get_height() * scale)))
        self.rect = self.img.get_rect()

    def center_coord(self, x, y):
        self.pos = [x - (self.rect[2] / 2), y - (self.rect[2] / 2)]

    def draw(self):
        self.screen.blit(self.img, self.pos)
        






        


