from entity import Enemy
import pygame 
import json
from random import randint
from entity import Entity

class Map:
    def __init__(self, path, screen):
        self.screen = screen
        self.entities = []
        self.enemies = []
        self.path = "main/game/map/" + path + ".json"
        self.imgs = []
        with open(self.path) as f:
            self.info = json.load(f)
        f.close()
        for type in self.info:
            for entity in self.info[type]:
                entity = self.info[type][entity]
                img = pygame.image.load("main/game/media/terrain/" + entity["path"])
                scale = entity["scale"]
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                self.imgs.append(img)
                if type == "terrain":
                    for e in entity["entities"]:
                        #DEFINER ENTITY OBJEKTER
                        self.entities.append([img, e])
                elif type == "enemy":
                    # Lagre annen info her (hp, dmg, movement type) og pass inn i enemy objekt
                    for e in entity["entities"]:
                        self.enemies.append(Enemy(img,e, screen))

    def draw(self, camera):
        for e in self.entities:
            self.screen.blit(e[0],[e[1][0] - camera[0], e[1][1] - camera[1]])
        for e in self.enemies:
            e.draw(camera)

    def update(self, playerpos):
        for e in self.enemies:
            e.update(playerpos)
        
    def forest(self, cornerX, cornerY, amount, img):
        size = 2000
        for _ in range(amount):
            x = randint(cornerX, cornerX+size)
            y = randint(cornerY, cornerY+size)
            self.entities.append([img, [x, y]])

