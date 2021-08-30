from entity import Entity
import pygame
import math
from spritesheet import Spritesheet



class Scellyenny(Entity):
    def __init__(self, start_pos, path, scale, speed):
        super().__init__(start_pos, path, scale)
        self.speed = speed


        


    
    def move_towards_player(self, playerpos):
        dx, dy = self.start_pos[0] - self.pos[0], self.start_pos[1] - self.pos[1]
        
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist , dy/dist

        self.pos[0] += dx * self.speed
        self.pos[1] += dy * self.speed

        

    

        

 
