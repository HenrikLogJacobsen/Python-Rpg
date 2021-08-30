from entity import Entity
import pygame
import math
from spritesheet import Spritesheet



class Scellyenny(Entity):
    def __init__(self, start_pos, path, scale, speed):
        super().__init__(start_pos, path, scale)
        self.speed = speed 
        print(speed)


    
    def move_towards_player(self, player):
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist , dy/dist

        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    

        

 
