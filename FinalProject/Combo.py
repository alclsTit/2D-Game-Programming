import PCharacter
import RES
import Button

class Combo:
    def __init__(self):
        self.x , self.y = 0 , 0
        self.combo_count = 0

        self.select_combo_num  = 0


    def Update(self):
        self.x = PCharacter.Player.move_x
        self.y = PCharacter.Player.move_y + PCharacter.Player.half_height + 50
        self.combo_count = Button.Button_beat.button_combo_cnt
        self.frame_y = 0

        #콤보 카운트 0(miss) -> select_combo_num = 1
        #콤보 카운트 1이상(combo) -> select_combo_num = 3
        #콤보 카운트 10배수(cool) -> select_combo_num = 2
        #콤보 카운트 30배수(hit hit) -> select_combo_num = 0

        #cool
        if((self.combo_count % 10 == 0) and self.combo_count != 0 and (self.combo_count % 30 != 0)):
            self.select_combo_num = 2

        #miss
        if(self.combo_count == 0):
            self.select_combo_num = 1

        #combo
        if(self.combo_count >= 1 and (self.combo_count % 10) != 0):
            self.select_combo_num = 3

        #hit hit
        if((self.combo_count % 30 ) == 0 and self.combo_count != 0):
            self.select_combo_num = 0

        Button.Button_beat.size = 0
        for Button.Button_beat.size in range(Button.Button_beat.Get_total_ButtonNum):
            if (Button.Button_beat.Button_List[Button.Button_beat.size][11] == True) and (Button.Button_beat.Button_List[Button.Button_beat.size][12] >= 0):
                Button.Button_beat.Button_List[Button.Button_beat.size][12] -= 1


    def Draw(self):
        for Button.Button_beat.size in range(Button.Button_beat.Get_total_ButtonNum):
            if (Button.Button_beat.Button_List[Button.Button_beat.size][11] == True) and (Button.Button_beat.Button_List[Button.Button_beat.size][12] >= 0):
                if self.select_combo_num == 0:
                    RES.res.Combo.clip_draw(0, 0, 200, 100, self.x, self.y)
                elif self.select_combo_num == 1:
                    RES.res.Combo.clip_draw(0, 100, 200, 100, self.x, self.y)
                elif self.select_combo_num == 2:
                    RES.res.Combo.clip_draw(0, 200, 200, 100, self.x, self.y)
                elif self.select_combo_num == 3:
                    RES.res.Combo.clip_draw(0, 300, 200, 100, self.x, self.y)