import pygame

class Label:
    def __init__(self,string, coordx, coordy, fontSize):
        self.font = pygame.font.Font('freesansbold.ttf', fontSize) 
        #(0, 0, 0) is black, to make black text
        self.text = self.font.render(string, True, (0, 0, 0)) 
        self.textRect = self.text.get_rect()
        self.textRect.center = (coordx, coordy)
    
    def update(self, new):
        self.text = self.font.render(new, True, (0,0,0))

class GameGui:
    def __init__(self, screen):
        self.screen = screen
        self.timebox = Label("00:00", 30, 15, 20)
    
    def draw(self):
        self.screen.blit(self.timebox.text, self.timebox.textRect)

    def update(self, time):
        gametime = time // 30
        minutes = gametime*10 % 60
        hour = ((gametime // 6) + 12) % 24
        gametime = str(hour).zfill(2) + ":" + str(minutes).zfill(2)
        self.timebox.update(gametime)