from pico2d import *

class User_UI:
    User_point = 0
    User_combo = 0
    User_miss = 0
    User_coolcombo = 0
    User_hitcombo = 0
    User_HP = 100
    def __init__(self):
        self.Max_height = 900
        self.font_size = 20
        self.HP_font_size = 50
        self.digit_pos = 400
        self.word_pos = 200

        User_point = 0
        User_combo = 0
        User_miss = 0
        User_coolcombo = 0
        User_hitcombo = 0

    def Update(self):
        pass

    def Draw(self):
        global font
        font = load_font('ENCR10B.TTF', self.font_size)

        font.draw(self.word_pos, self.Max_height - self.font_size, "**[Point]** ", (255, 0, 0))
        font.draw(self.digit_pos, self.Max_height - self.font_size, "%d Point" %(User_UI.User_point))

        font.draw(self.word_pos, self.Max_height - 2 * self.font_size, "**[Combo]** ", (255, 0, 0))
        font.draw(self.digit_pos, self.Max_height - 2 * self.font_size, "%d Combo" % (User_UI.User_combo))

        font.draw(self.word_pos, self.Max_height - 3 * self.font_size, "**[CoolCombo]** ", (255, 0, 0))
        font.draw(self.digit_pos, self.Max_height - 3 * self.font_size, "%d Cool Combo" % (User_UI.User_coolcombo))

        font.draw(self.word_pos, self.Max_height - 4 * self.font_size, "**[HitCombo]** ", (255, 0, 0))
        font.draw(self.digit_pos, self.Max_height - 4 * self.font_size, "%d Hit Combo" %(User_UI.User_hitcombo))

        font.draw(self.word_pos, self.Max_height - 5 * self.font_size, "**[Miss]** ", (255, 0, 0))
        font.draw(self.digit_pos, self.Max_height - 5 * self.font_size, "%d Miss" %(User_UI.User_miss))

    def Draw_HP(self):
        global font
        font = load_font('ENCR10B.TTF', self.HP_font_size)
        
        #임시
        font.draw(400, 700, "H P",(0,255,0))
        font.draw(600, 700 ,"%d HP" %(User_UI.User_HP))