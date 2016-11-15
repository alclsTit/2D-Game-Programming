from pico2d import *

import random
import Collision
import PUpBar
import RES

class Button_beat:
    Hit_count = 0
    Button_List = []
    size = 0

    a_button = False
    s_button = False
    d_button = False
    f_button = False
    b_button = False

    def __init__(self):
        self.Button_data = []
        self.Button_total_num = 0
        self.x , self.y = 1550, 675
        self.fx ,self.fy = 0, 1
        self.toatal_fx = 0
        self.create_time = 0
        self.IsColled = False
        self.canremove = False
        self.disappear_cnt = 5
        self.button_num = 1
        self.point = 50
        self.move_size = 25

    def Update(self,stage_num):
        if stage_num == 1:
            if self.Button_total_num < 10:
                self.create_time = (self.create_time + 1) % 51
                if self.create_time == 50:
                    self.Button_total_num += 1
                    self.button_num = random.randint(1,5)
                    if self.button_num == 5:
                        self.point = 200
                        self.move_size = 25
                    else:
                        self.point = 50
                        self.move_size = 25

                    self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num, self.point,
                                        self.move_size, self.IsColled, self.canremove, self.disappear_cnt]
                    Button_beat.Button_List.append(self.Button_data)

            elif self.Button_total_num >= 10 and self.Button_total_num < 30:
                self.create_time = (self.create_time + 1) % 31
                if self.create_time == 30: #1 7 13 19
                    self.Button_total_num += 1
                    self.button_num = random.randint(1, 6)
                    if self.button_num == 5:
                        self.point = 200
                        self.move_size = 25
                    elif self.button_num == 6:
                        self.point = -200
                        self.move_size = 10
                    else:
                        self.point = 50
                        self.move_size = 25

                    self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num, self.point,
                                        self.move_size, self.IsColled, self.canremove, self.disappear_cnt]
                    Button_beat.Button_List.append(self.Button_data)

            elif self.Button_total_num >= 30 and self.Button_total_num < 40:
                self.create_time = (self.create_time + 1) % 51
                if self.create_time == 50:
                    self.Button_total_num += 1
                    self.button_num = random.randint(1, 6)
                    if self.button_num == 5:
                        self.point = 200
                        self.move_size = 20
                    elif self.button_num == 6:
                        self.point = -200
                        self.move_size = 25
                    else:
                        self.point = 50
                        self.move_size = 25

                    self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num, self.point,
                                    self.move_size, self.IsColled, self.canremove, self.disappear_cnt]
                    Button_beat.Button_List.append(self.Button_data)


            elif self.Button_total_num >= 40 and self.Button_total_num < 60:
                self.create_time = (self.create_time + 1) % 31
                if self.create_time == 30:
                    self.Button_total_num += 1
                    self.button_num = random.randint(1, 5)
                    if self.button_num == 5:
                        self.point = 200
                        self.move_size = 25
                    else:
                        self.point = 50
                        self.move_size = 25

                    self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num, self.point,
                                    self.move_size, self.IsColled, self.canremove, self.disappear_cnt]
                    Button_beat.Button_List.append(self.Button_data)

            elif  self.Button_total_num >= 60:
                self.create_time = (self.create_time + 1) % 41
                if self.create_time == 40:
                    self.Button_total_num += 1
                    self.button_num = random.randint(1, 6)
                    if self.button_num == 5:
                        self.point = 200
                        self.move_size = 15
                    elif self.button_num == 6:
                        self.point = -200
                        self.move_size = 25
                    else:
                        self.point = 50
                        self.move_size = 25

                    self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num, self.point,
                                        self.move_size, self.IsColled, self.canremove, self.disappear_cnt]
                    Button_beat.Button_List.append(self.Button_data)


        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            Button_beat.Button_List[Button_beat.size][0] -= 10

        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            Button_beat.Button_List[Button_beat.size][2] = (Button_beat.Button_List[Button_beat.size][2] + 1) % 4
            if Button_beat.Button_List[Button_beat.size][2] == 3:
                Button_beat.Button_List[Button_beat.size][4] = (Button_beat.Button_List[Button_beat.size][4] + 1) % 4

        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            if(PUpBar.Stop_station.coll_x - 50 < Button_beat.Button_List[Button_beat.size][0] and Button_beat.Button_List[Button_beat.size][0] < PUpBar.Stop_station.coll_x + 50 and PUpBar.Stop_station.coll_y - 50 < Button_beat.Button_List[Button_beat.size][1] and Button_beat.Button_List[Button_beat.size][1] < PUpBar.Stop_station.coll_y + 50):
                Button_beat.Button_List[Button_beat.size][8] = True
            else:
                Button_beat.Button_List[Button_beat.size][8] = False

        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            if Button_beat.Button_List[Button_beat.size][8] == True:
                if Button_beat.Button_List[Button_beat.size][5] == 1 and Button_beat.a_button == True : #a버튼이 눌러졌고 해당 버튼이 누르는지점에 닿았을 때
                    Button_beat.Button_List[Button_beat.size][9] = True
                elif Button_beat.Button_List[Button_beat.size][5] == 2 and Button_beat.s_button == True :
                    Button_beat.Button_List[Button_beat.size][9] = True
                elif Button_beat.Button_List[Button_beat.size][5] == 3 and Button_beat.d_button == True :
                    Button_beat.Button_List[Button_beat.size][9] = True
                elif Button_beat.Button_List[Button_beat.size][5] == 4 and Button_beat.f_button == True :
                    Button_beat.Button_List[Button_beat.size][9] = True
                elif Button_beat.Button_List[Button_beat.size][5] == 5 and Button_beat.b_button == True :
                    Button_beat.Button_List[Button_beat.size][9] = True
                elif Button_beat.Button_List[Button_beat.size][5] == 6 and (Button_beat.a_button == True or Button_beat.s_button == True or Button_beat.d_button == True or Button_beat.f_button == True or Button_beat.b_button == True) :
                    Button_beat.Button_List[Button_beat.size][9] = True

        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            if Button_beat.Button_List[Button_beat.size][9] == True:
                Button_beat.Button_List[Button_beat.size][3] = 0
                Button_beat.Button_List[Button_beat.size][10] -= 1

            if Button_beat.Button_List[Button_beat.size][10] < 0:
                Button_beat.Button_List.remove(Button_beat.Button_List[Button_beat.size])
                self.Button_total_num -=1
                Button_beat.size -= 1

    def Draw(self):
        for i in range(self.Button_total_num):
            if Button_beat.Button_List[i][5] == 1:
                RES.res.A_button.clip_draw(Button_beat.Button_List[i][4] * 100 ,Button_beat.Button_List[i][3] * 100 , 100,100, Button_beat.Button_List[i][0],Button_beat.Button_List[i][1])
            elif Button_beat.Button_List[i][5] == 2:
                RES.res.S_button.clip_draw(Button_beat.Button_List[i][4] * 100, Button_beat.Button_List[i][3] * 100,
                                           100, 100, Button_beat.Button_List[i][0], Button_beat.Button_List[i][1])
            elif Button_beat.Button_List[i][5] == 3:
                RES.res.D_button.clip_draw(Button_beat.Button_List[i][4] * 100, Button_beat.Button_List[i][3] * 100,
                                           100, 100, Button_beat.Button_List[i][0], Button_beat.Button_List[i][1])
            elif Button_beat.Button_List[i][5] == 4:
                RES.res.F_button.clip_draw(Button_beat.Button_List[i][4] * 100, Button_beat.Button_List[i][3] * 100,
                                           100, 100, Button_beat.Button_List[i][0], Button_beat.Button_List[i][1])
            elif Button_beat.Button_List[i][5] == 5:
                RES.res.B_button.clip_draw(Button_beat.Button_List[i][4] * 100, Button_beat.Button_List[i][3] * 100,
                                           100, 100, Button_beat.Button_List[i][0], Button_beat.Button_List[i][1])
            elif Button_beat.Button_List[i][5] == 6:
                RES.res.boom_button.clip_draw(Button_beat.Button_List[i][4] * 100, Button_beat.Button_List[i][3] * 100,
                                           100, 100, Button_beat.Button_List[i][0], Button_beat.Button_List[i][1])