
import pygame

class redrawGameWindow(self, screen,

    self.screen.fill('white')
    self.map1.draw(self.screen_pos)


    if LEFT:
        screen.blit(player_left_walk[clock_count],(player.pos))

    elif RIGHT:
        screen.blit(player_right_walk[clock_count],(player.pos))
    
    else: 
        screen.blit(player_idle[idle_count],(player.pos))