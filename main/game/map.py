from scellyenny import Enemy
import pygame 
import json

class Map:
    def __init__(self, path, screen):
        self.screen = screen
        self.entities = []
        self.enemies = []
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
                if type == "terrain":
                    for e in entity["entities"]:
                        self.entities.append([img, e])
                elif type == "enemy":
                    for e in entity["entities"]:
                        self.enemies.append(Enemy(img,e))

    def draw(self, playerpos):
        for e in self.entities:
            self.screen.blit(e[0],[e[1][0] + playerpos[0], e[1][1] + playerpos[1]])
        for e in self.enemies:
            e.draw()
