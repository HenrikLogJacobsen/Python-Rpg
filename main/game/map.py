from entity import Entity
import pygame 

class Map:
    def __init__(self, path, positions, screen):
        self.path = path
        self.positions = positions
        self.screen = screen
        self.entities = []
        
     

        for pos in self.positions:
            self.entities.append(Entity(pos, self.path, .2))
        

   ## def biome(self, playerpos): 


    def draw(self, screen_pos):
        for e in self.entities:
            e.pos[0] = e.start_pos[0] + screen_pos[0]
            e.pos[1] = e.start_pos[1] + screen_pos[1]
            self.screen.blit(e.img,e.pos)


