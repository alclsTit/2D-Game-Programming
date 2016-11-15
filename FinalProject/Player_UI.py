from pico2d import *

class User_UI:
    User_point = 0
    User_combo = 0
    User_miss = 0
    User_TotalHit = 0

    def Update(self):
        pass

    def Draw(self):
        global font
        font = load_font('ENCR10B.TTF', 20)
        font.draw(200, 880, "[User Point] :", (255, 0, 0))
        font.draw(400, 880, "%d Point" %(User_UI.User_point))
