import pygame

class Entity:
    def __init__(self, pos, path):
        self.pos = pos
        self.path = "main/game/media/" + path
        self.img = pygame.image.load(self.path)
        self.rect = self.img.get_rect()

    def say_something(self):
        print("HELLO")

        


