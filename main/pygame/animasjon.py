
from typing import Sequence
import pygame
from pygame.sprite import Sprite

class SimpleAnimation(Sprite):

    def __init__(self, frames):
        Sprite.__init__(self)
        self.frames = frames
        self.current = 0
        self.image = frames[0]
        self.rect = self.image.get_rect()
        self.playing = 0 

    def update(self, *args):
        if self.playing:
            self.current += 1
            if self.current == len(self.frames):
                self.current = 0
            self.image = self.frames[self.current]
            self.rect = self.image.get_rect(center=self.rect.center)
            
    def start(self):
        self.current = 0
        self.playing = True
    
    def stop(self):
        self.playing = False
    
    def pause(self):
        self.playing = False

    def resume(self):
        self.playing = True


cache = {}

def get_sequence(frames_names, sequence, optimize = True):
    frames = []
    global cache 
    for name in frames_names:
        if not cache.has_key(name):
            image = pygame.image.load(name)
            if optimize:
                if image.get_alpha() is not None:
                    image = image.convert_alpha()
                else:
                    image = image.convert()
                
            cache[name] = image 

        frames.append(cache[name])
    frames2 = []
    for idx in sequence:
        frames2.append(frames[idx])
    return frames2

def get_names_list(basename, ext, num, num_digits = 1, offset = 0):
    names = []
    format = "%s%0"+str(num_digits)+"d.%s"
    for i in range(offset, num+1):
        names.append(format % (basename, i, ext))
    return names

image_names = get_names_list("pic", 'png', 4)
sequence = [0,1,2,3,2,1]
frames = get_sequence(image_names, sequence) 


    














