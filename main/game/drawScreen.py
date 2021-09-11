
import pygame

def redrawGameWindow():
    screen.fill('white')
    enemy_pos = enemy.move_towards_player(player.pos)
    screen.blit(enemy.img, enemy_pos)
    player.draw(screen)
    map1.draw(player.pos)