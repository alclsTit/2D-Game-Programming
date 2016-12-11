import PCharacter
import RES


class Point_Effect:
    def __init__(self):
        self.x , self.y = 0 , 0
        self.half_width , self.half_height = 25 , 25

        pass

    def Update(self):
        self.x = PCharacter.Player.move_x
        self.y = PCharacter.Player.move_y + self.half_height + 30

        pass

    def Draw(self):

        pass