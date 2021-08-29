import pygame
from pygame.constants import K_LEFT
from spritesheet import Spritesheet



class Player():
    def __init__(self, start_pos):
        self.pos = start_pos

        #self.pos = [start_pos[0] - (self.rect[2] / 2), y - (self.rect[2] / 2)]
        
    def draw(): 
        
        char_anim_sprite = Spritesheet('main/game/media/char_anim.png')
        player_running_anim = [char_anim_sprite.parse_sprite("adventurer-run-00.png"), char_anim_sprite.parse_sprite("adventurer-run-01.png"), char_anim_sprite.parse_sprite("adventurer-run-02.png"), char_anim_sprite.parse_sprite("adventurer-run-03.png"), char_anim_sprite.parse_sprite("adventurer-run-04.png"), char_anim_sprite.parse_sprite("adventurer-run-05.png")]
        player_idle = [char_anim_sprite.parse_sprite("adventurer-idle-2-00.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-03.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-02.png"), char_anim_sprite.parse_sprite("adventurer-idle-2-01.png")]
        player_attack = [char_anim_sprite.parse_sprite("adventurer-attack2-00.png"), char_anim_sprite.parse_sprite("adventurer-attack2-01.png"), char_anim_sprite.parse_sprite("adventurer-attack2-02.png"), char_anim_sprite.parse_sprite("adventurer-attack2-03.png"), char_anim_sprite.parse_sprite("adventurer-attack2-04.png"), char_anim_sprite.parse_sprite("adventurer-attack2-05.png"), ]
        keys = pygame.key.get.pressed()



        if action == True:

            if keys = [K_LEFT]:

                if keys[pygame.K_LEFT]:
                    screen_pos[0] += vel
                    screen.blit(pygame.transform.flip(player_running_anim[math.floor(index)], True, False),(player.pos))

                    index = (index + 0.1) % len(player_running_anim)

