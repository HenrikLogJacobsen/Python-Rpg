#from main.game.player import Player
import pygame
import json


class Spritesheet:
    def __init__(self, path):
        self.path = path
        self.sprite_sheet = pygame.image.load(path).convert()
        self.meta_data = self.path.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
        


    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet, (0,0), (x,y,w,h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite['x'], sprite['y'], sprite['w'], sprite['h']
        image = self.get_sprite(x, y, w, h)
        return image

class MapInfo:
    def __init__(self, path, screen):
        self.screen = screen
        self.entities = []
        self.path = "main/game/map/" + path + ".json"
        with open(self.path) as f:
            self.info = json.load(f)
        f.close()
        for type in self.info:
            for entity in self.info[type]:
                entity = self.info[type][entity]
                img = pygame.image.load("main/game/media/" + entity["path"])
                scale = entity["scale"]
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                for e in entity["entities"]:
                    self.entities.append([img, e])

    def draw(self, playerpos):
        for e in self.entities:
            self.screen.blit(e[0],[e[1][0] + playerpos[0], e[1][1] + playerpos[1]])

        
            


