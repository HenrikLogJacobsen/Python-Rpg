from entity import Entity



class Scellyenny(Entity):
    def __init__(self, start_pos, path, scale, speed, screen_pos):
        super().__init__(start_pos, path, scale)
        self.speed = speed
        self.start_pos = start_pos
        self.center = screen_pos
        self.pos = start_pos

    
    def move_towards_player(self, step_count):

        x, y = self.start_pos

        y += step_count[1]
        y += step_count[0]
        x += step_count[2]
        x += step_count[3]


        self.pos = [x, y]
        return self.pos
        


    






    


        
        



    


        

    

        

 
