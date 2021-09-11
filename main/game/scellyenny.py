from pygame.sprite import spritecollide
from entity import Entity
import pygame
import math


class Scellyenny(Entity):
    def __init__(self, start_pos, path, scale, speed, screen_pos):
        super().__init__(start_pos, path, scale)
        self.speed = speed
        self.start_pos = start_pos
        self.center = screen_pos
        self.pos = start_pos

    
    def move_towards_player(self, playerpos):

        dx, dy = playerpos[0] - self.center[0], playerpos[1] - self.center[1]
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist  
        x = self.pos[0]
        y = self.pos[1]

        x += (dx * self.speed)
        y += (dy * self.speed)

        self.pos = [x, y]
        return self.pos
        
class Enemy():
    def __init__(self, img, pos) -> None:
        pass
        
    


    






    


        
        



    


        

    

        

 
