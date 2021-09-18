import pygame
from spritesheet import Spritesheet
import math

class Player():
    def __init__(self, monitor):

        self.action = "idle"
        self.index = 0
        #char sprites
        char_anim_sprite = Spritesheet('main/game/media/sprites/char_anim.png')
        self.player_running_anim = [char_anim_sprite.parse_sprite("adventurer-run-00.png"), char_anim_sprite.parse_sprite("adventurer-run-01.png"), char_anim_sprite.parse_sprite("adventurer-run-02.png"), char_anim_sprite.parse_sprite("adventurer-run-03.png"), char_anim_sprite.parse_sprite("adventurer-run-04.png"), char_anim_sprite.parse_sprite("adventurer-run-05.png")]
        self.player_idle = [char_anim_sprite.parse_sprite("adventurer-idle-2-00.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-03.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png")]
        self.player_attack = [char_anim_sprite.parse_sprite("adventurer-attack2-00.png"), char_anim_sprite.parse_sprite("adventurer-attack2-01.png"), char_anim_sprite.parse_sprite("adventurer-attack2-02.png"), char_anim_sprite.parse_sprite("adventurer-attack2-03.png"), char_anim_sprite.parse_sprite("adventurer-attack2-04.png"), char_anim_sprite.parse_sprite("adventurer-attack2-05.png"), ]


        self.char_anim_sprite = Spritesheet('main/game/media/sprites/char_anim.png')

        rect = self.char_anim_sprite.parse_sprite("adventurer-idle-2-00.png").get_rect()
        self.rect = rect[2], rect[3]
        self.draw_pos = [monitor[0] / 2 - (self.rect[0] / 2), monitor[1] / 2 - (self.rect[1] / 2)]
        self.pos = [monitor[0] / 2 - (self.rect[0] / 2), monitor[1] / 2 - (self.rect[1] / 2)]
        
        #sprite groups 
        #all_sprites = pygame.sprite.Group()
        #all_sprites.add(self.player_running_anim)

    def draw(self, screen):
        # ACTION OVERKJØRER MOVEMENT OVERKJØRER OPP OG NED
        if self.action == "left":
            screen.blit(pygame.transform.flip(self.player_running_anim[math.floor(self.index)], True, False),(self.draw_pos))

        if self.action == "right":
            screen.blit(self.player_running_anim[math.floor(self.index)],(self.draw_pos))
        
        if self.action == "idle": 
            screen.blit(self.player_idle[math.floor(self.index)],(self.draw_pos))

        if self.action == "attacking": 
            if self.LEFT == True:
                screen.blit(pygame.transform.flip(self.player_attack[math.floor(self.index)], True, False), (self.draw_pos))
            else:
                screen.blit(self.player_attack[math.floor(self.index)], self.draw_pos)

    def update(self):
        # 
        if self.action == "left" or self.action == "right":
            self.index = (self.index + 0.1) % len(self.player_running_anim)

        # DRAW
        self.index = self.index + 0.1 % len(self.player_idle)
        if self.index >= 6:
            self.index = 0

        self.pos = self.pos
        
        self.action = "idle"

    def is_touching(self, vel, entities):
        #self.pos self.rect, entity.pos entity.rect
        d = 9
        for e in entities:
            if (
                self.pos[0] + vel[0] + self.rect[0] - d >= e.pos[0] and
                e.pos[0] + e.rect[0] >= self.pos[0] + vel[0] + d and
                self.pos[1] + vel[1] + self.rect[1] - d >= e.pos[1] + e.dtop and
                e.pos[1] + e.rect[1] >= self.pos[1] + vel[1] + d
                ):
                return True

        return False

