import pygame
from spritesheet import Spritesheet
import math

class Player():
    def __init__(self, center):

        self.action = "idle"
        self.index = 0
        #char sprites
        char_anim_sprite = Spritesheet('main/game/media/char_anim.png')
        self.player_running_anim = [char_anim_sprite.parse_sprite("adventurer-run-00.png"), char_anim_sprite.parse_sprite("adventurer-run-01.png"), char_anim_sprite.parse_sprite("adventurer-run-02.png"), char_anim_sprite.parse_sprite("adventurer-run-03.png"), char_anim_sprite.parse_sprite("adventurer-run-04.png"), char_anim_sprite.parse_sprite("adventurer-run-05.png")]
        self.player_idle = [char_anim_sprite.parse_sprite("adventurer-idle-2-00.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-03.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png")]
        self.player_attack = [char_anim_sprite.parse_sprite("adventurer-attack2-00.png"), char_anim_sprite.parse_sprite("adventurer-attack2-01.png"), char_anim_sprite.parse_sprite("adventurer-attack2-02.png"), char_anim_sprite.parse_sprite("adventurer-attack2-03.png"), char_anim_sprite.parse_sprite("adventurer-attack2-04.png"), char_anim_sprite.parse_sprite("adventurer-attack2-05.png"), ]


        self.char_anim_sprite = Spritesheet('main/game/media/char_anim.png')

        self.rect = self.char_anim_sprite.parse_sprite("adventurer-idle-2-00.png").get_rect()
        self.hitbox = (self.rect[2], self.rect[3])
        self.start_pos = [center[0] - (self.hitbox[0] / 2), center[1] - (self.hitbox[1] / 2)]
        self.pos = [center[0] - (self.hitbox[0] / 2), center[1] - (self.hitbox[1] / 2)]
        
        #sprite groups 
        #all_sprites = pygame.sprite.Group()
        #all_sprites.add(self.player_running_anim)

    def draw(self, screen):
        
        if self.action == "left":
            screen.blit(pygame.transform.flip(self.player_running_anim[math.floor(self.index)], True, False),(self.start_pos))

        if self.action == "right":
            screen.blit(self.player_running_anim[math.floor(self.index)],(self.start_pos))
        
        if self.action == "idle": 
            screen.blit(self.player_idle[math.floor(self.index)],(self.start_pos))

        if self.action == "attacking": 
            if self.LEFT == True:
                screen.blit(pygame.transform.flip(self.player_attack[math.floor(self.index)], True, False), (self.start_pos))
            else:
                screen.blit(self.player_attack[math.floor(self.index)], self.start_pos)

    def update(self):
        if self.action == "left" or self.action == "right":
            self.index = (self.index + 0.1) % len(self.player_running_anim)

        # DRAW
        self.index = self.index + 0.1 % len(self.player_idle)
        if self.index >= 6:
            self.index = 0

        self.pos = self.pos
        
        self.action = "idle"
        