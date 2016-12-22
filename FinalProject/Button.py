from pico2d import *

import random
import Collision
import PUpBar
import RES
import Player_UI
import PObject
import PTile

class Button_beat:
    Hit_count = 0
    Button_List = []
    size = 0

    a_button = False
    s_button = False
    d_button = False
    f_button = False
    b_button = False

    button_combo_cnt = 0

    Get_total_ButtonNum = 0

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

        self.half_width = 50
        self.half_height = 50

        self.jump_time = 0
        self.jump_time_buttonNum = 0

        self.jump_button_flag = False
        #버튼 클릭 이미지가 보여진다 or 안보여진다
        self.show_flag = False

        #버튼 클릭 이미지가 보여지는 시간
        self.show_time = 6

    def Update(self,stage_num):
        if stage_num == 1:
            # 1550 시작 -> 25씩 46프레임뒤 / 블록은 10씩
            #for i in range(PTile.Brick.number):
            #    if i >= 1:
            #        if PTile.Brick.List_tile[i][0] + PTile.Brick.List_tile[i][4] - 500 >= 460 and  PTile.Brick.List_tile[i][0] + PTile.Brick.List_tile[i][4] - 500 <= 560:
            #            if self.jump_time == 0:
            #                self.point = 200
            #                self.move_size = 10

            #                self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num,
            #                                    self.point,
            #                                    self.move_size, self.IsColled, self.canremove, self.disappear_cnt,
            #                                    self.show_flag, self.show_time, self.move_size]
            #                Button_beat.Button_List.append(self.Button_data)

            #            self.jump_time = (self.jump_time + 1) % 11

            #            if self.jump_time == 10:
            #                self.Button_total_num += 1

            #            self.jump_button_flag = True
            #        else:
            #            self.jump_button_flag = False

            #if self.jump_button_flag == False:

                if self.Button_total_num < 10:
                    self.create_time = (self.create_time + 1) % 51
                    if self.create_time == 50:
                        self.Button_total_num += 1
                        self.button_num = random.randint(1, 6)
                        if self.button_num == 5:
                            self.point = 200
                            self.move_size = 10
                        elif self.button_num == 6:
                            self.point = -1000
                            self.move_size = 10
                        else:
                            self.point = 50
                            self.move_size = 10

                        self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num,
                                            self.point,
                                            self.move_size, self.IsColled, self.canremove, self.disappear_cnt,
                                            self.show_flag, self.show_time, self.move_size]
                        Button_beat.Button_List.append(self.Button_data)

                elif self.Button_total_num >= 10 and self.Button_total_num < 30:
                    self.create_time = (self.create_time + 1) % 31
                    if self.create_time == 30:  # 1 7 13 19
                        self.Button_total_num += 1
                        self.button_num = random.randint(1, 6)
                        if self.button_num == 5:
                            self.point = 200
                            self.move_size = 10
                        elif self.button_num == 6:
                            self.point = -1000
                            self.move_size = 10
                        else:
                            self.point = 50
                            self.move_size = 10

                        self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num,
                                            self.point,
                                            self.move_size, self.IsColled, self.canremove, self.disappear_cnt,
                                            self.show_flag, self.show_time, self.move_size]
                        Button_beat.Button_List.append(self.Button_data)

                elif self.Button_total_num >= 30 and self.Button_total_num < 40:
                    self.create_time = (self.create_time + 1) % 51
                    if self.create_time == 50:
                        self.Button_total_num += 1
                        self.button_num = random.randint(1, 6)
                        if self.button_num == 5:
                            self.point = 200
                            self.move_size = 10
                        elif self.button_num == 6:
                            self.point = -1000
                            self.move_size = 10
                        else:
                            self.point = 50
                            self.move_size = 10

                        self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num,
                                            self.point,
                                            self.move_size, self.IsColled, self.canremove, self.disappear_cnt,
                                            self.show_flag, self.show_time, self.move_size]
                        Button_beat.Button_List.append(self.Button_data)


                elif self.Button_total_num >= 40 and self.Button_total_num < 60:
                    self.create_time = (self.create_time + 1) % 31
                    if self.create_time == 30:
                        self.Button_total_num += 1
                        self.button_num = random.randint(1, 5)
                        if self.button_num == 5:
                            self.point = 200
                            self.move_size = 10
                        else:
                            self.point = 50
                            self.move_size = 10

                        self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num,
                                            self.point,
                                            self.move_size, self.IsColled, self.canremove, self.disappear_cnt,
                                            self.show_flag, self.show_time, self.move_size]
                        Button_beat.Button_List.append(self.Button_data)

                elif self.Button_total_num >= 60:
                    self.create_time = (self.create_time + 1) % 41
                    if self.create_time == 40:
                        self.Button_total_num += 1
                        self.button_num = random.randint(1, 6)
                        if self.button_num == 5:
                            self.point = 200
                            self.move_size = 10
                        elif self.button_num == 6:
                            self.point = -1000
                            self.move_size = 10
                        else:
                            self.point = 50
                            self.move_size = 10

                        self.Button_data = [self.x, self.y, self.fx, self.fy, self.toatal_fx, self.button_num,
                                            self.point,
                                            self.move_size, self.IsColled, self.canremove, self.disappear_cnt,
                                            self.show_flag, self.show_time , self.move_size]
                        Button_beat.Button_List.append(self.Button_data)



        #생성된 버튼은 왼쪽으로 이동한다
        Button_beat.size = 0
        for Button_beat.size in range(len(Button_beat.Button_List)):
            if Player_UI.User_UI.User_HP > 0 and PObject.Exit_door.Exit_flag == False:
                    Button_beat.Button_List[Button_beat.size][0] -= Button_beat.Button_List[Button_beat.size][13]

        #버튼의 이미지변화(x프레임 변화)
        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            Button_beat.Button_List[Button_beat.size][2] = (Button_beat.Button_List[Button_beat.size][2] + 1) % 4
            if Button_beat.Button_List[Button_beat.size][2] == 3:
                Button_beat.Button_List[Button_beat.size][4] = (Button_beat.Button_List[Button_beat.size][4] + 1) % 4

        #버튼이 버튼 클릭 지점에 들어왔는지 확인
        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            if(PUpBar.Stop_station.coll_x - 50 < Button_beat.Button_List[Button_beat.size][0] and Button_beat.Button_List[Button_beat.size][0] < PUpBar.Stop_station.coll_x + 50 and PUpBar.Stop_station.coll_y - 50 < Button_beat.Button_List[Button_beat.size][1] and Button_beat.Button_List[Button_beat.size][1] < PUpBar.Stop_station.coll_y + 50):
                Button_beat.Button_List[Button_beat.size][8] = True
            else:
                Button_beat.Button_List[Button_beat.size][8] = False

        #버튼이 버튼 클릭 지점에 들어왔고 해당 버튼을 키보드로 클릭 했을시
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

        #버튼을 눌르고 버튼이 사라질 지점에 존재할때
        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            if Button_beat.Button_List[Button_beat.size][9] == True:
                Button_beat.Button_List[Button_beat.size][3] = 0
                Button_beat.Button_List[Button_beat.size][10] -= 1

                #버튼을 알맞게 눌렀을시 콤보 카운트는 1만 증가하도록
                if Button_beat.Button_List[Button_beat.size][5] != 6:
                    if Button_beat.Button_List[Button_beat.size][11] == False:
                        Button_beat.Button_List[Button_beat.size][11] = True

                        if Button_beat.Button_List[Button_beat.size][5] == 5:
                            Player_UI.User_UI.User_HP += 20
                            if Player_UI.User_UI.User_HP >= 200:
                                Player_UI.User_UI.User_HP = 200

                        Button_beat.button_combo_cnt += 1
                        Player_UI.User_UI.User_combo += 1
                        if Player_UI.User_UI.User_combo % 10 == 0 and Player_UI.User_UI.User_combo != 0 and Player_UI.User_UI.User_combo % 30 != 0:
                            Player_UI.User_UI.User_coolcombo += 1
                        if Player_UI.User_UI.User_combo % 30 == 0 and Player_UI.User_UI.User_combo != 0:
                            Player_UI.User_UI.User_hitcombo += 1

        #눌려진 버튼 삭제
        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            if Button_beat.Button_List[Button_beat.size][10] < 0:
                Player_UI.User_UI.User_point += Button_beat.Button_List[Button_beat.size][6]
                #추가 부분
                Button_beat.Button_List.remove(Button_beat.Button_List[Button_beat.size])
                self.Button_total_num -=1
                break


        #버튼을 누르지 못하고 화면을 넘어갔을경우
        #1.버튼 삭제
        #2.콤보 포인트 초기화
        Button_beat.size = 0
        for Button_beat.size in range(self.Button_total_num):
            if Button_beat.Button_List[Button_beat.size][0] < 0:
                #생명력 깍기 추가
                Button_beat.Button_List.remove(Button_beat.Button_List[Button_beat.size])
                self.Button_total_num -=1
                break

            #버튼이 바로 클릭지점을 벗어났을 때
            if(Button_beat.Button_List[Button_beat.size][0] + self.half_width < PUpBar.Stop_station.coll_x - PUpBar.Stop_station.half_width):
                if Button_beat.Button_List[Button_beat.size][5] != 6:
                    if Button_beat.Button_List[Button_beat.size][11] == False:
                        Button_beat.Button_List[Button_beat.size][11] = True
                        Button_beat.button_combo_cnt = 0
                        Player_UI.User_UI.User_miss += 1
                        Player_UI.User_UI.User_HP -= 5

        Button_beat.Get_total_ButtonNum = self.Button_total_num

    def Draw(self):#
        for i in range(self.Button_total_num):
            if Button_beat.Button_List[i][5] == 1:
                RES.res.A_button.clip_draw(Button_beat.Button_List[i][4] * 100 ,Button_beat.Button_List[i][3] * 100,
                                           100,100, Button_beat.Button_List[i][0],Button_beat.Button_List[i][1])
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