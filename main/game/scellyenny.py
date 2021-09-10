from entity import Entity
import pygame
import math
from spritesheet import Spritesheet
from player import Player


class Scellyenny(Entity, Player):
    def __init__(self, start_pos, path, scale, speed):
        super().__init__(start_pos, path, scale)
        self.speed = speed
        self.playerpos = Player.pos



        


    
    def move_towards_player(self, playerpos):
        dx, dy = self.start_pos[0] - self.playerpos, self.start_pos[1] - self.playerpos
        
        dist = math.hypot(dx, dy)
        dx, dy = dx/dist , dy/dist

        self.pos[0] += dx * self.speed
        self.pos[1] += dy * self.speed

        print(self.pos)


    


        

    

        

 
