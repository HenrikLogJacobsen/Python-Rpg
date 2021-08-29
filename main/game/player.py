import pygame
from spritesheet import Spritesheet

class Player():
    def __init__(self, start_pos):
        self.pos = start_pos

        self.char_anim_sprite = Spritesheet('main/game/media/char_anim.png')

        rect = self.char_anim_sprite.parse_sprite("adventurer-idle-2-00.png").get_rect()
        self.hitbox = (rect[2], rect[3])
        
        self.pos = [start_pos[0] - (self.hitbox[0] / 2), start_pos[1] - (self.hitbox[1] / 2)]

        