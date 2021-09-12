from entity import Entity



class Scellyenny(Entity):
    def __init__(self, start_pos, path, scale, speed, screen_pos):
        super().__init__(start_pos, path, scale)
        self.speed = speed
        self.start_pos = start_pos
        self.center = screen_pos
        self.pos = start_pos

    
    def move_towards_player(self, step_count, playerpos):
        self.playerpos = playerpos
        x, y = self.start_pos
        self.pos = [x, y]   
        self.pos = ([self.pos[1] + playerpos[0], self.pos[1] + playerpos[1]])


        return self.pos
        
class Enemy():
    def __init__(self, img, pos) -> None:
        pass
        
    
## legg til en move method som oppdaterer posisjonen til enemy 


    






    


        
        



    


        

    

        

 
