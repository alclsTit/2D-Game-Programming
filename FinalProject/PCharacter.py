from pico2d import *
import math
import RES
import GameFramework
import ranking_state

name = "PCharacter"

#var_steps = [PTile.Brick() for i in range(20)]
Player_number = 0

#캐릭터 현재위치, 동작 변화, 이미지 로드, 스테이터스
class Player:
    Player_Die = False
    #PIXEL_PER_METER = (10.0 / 0.3)  # 10픽셀 1m로 가정
    #RUN_SPEED_KMPH = 20.0  # km/h
    #RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    #RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    #RUN_SPEED_PPS = (RUN_SPEED_MPS + PIXEL_PER_METER)  # m/s단위 속도 + 픽셀미터

    #100미터를 5초안에
    PIXEL_PER_METER = (10.0 / 0.5)  # 10 pixel 50 cm = >100 pixel 5m
    RUN_SPEED_KMPH = 72
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)    #20m/s
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # 10 * 20 = 200

    TIME_PER_ACTION = 0.125
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION     #동작 2번 - 1초
    FRAMES_PER_ACTION = 4  #한걸음 2초


    #jump_cnt = 0
    move_x = 0
    move_y = 200
    move_size = 10

    jump_state = False
    #total_jump_cnt = 0

    point = 0
    time = 0
    Player_num = 0

    CollwithTile = False

    def __init__(self):
        self.x , self.y = 0 , 200
        self.frame_x = 0
        self.frame_y = 9
        self.hp = 100
        self.total_frames = 0.0
        self.jump_cnt = 0
        self.total_jump_cnt = 0

    def Update(self,frame_time):
        distance = Player.RUN_SPEED_PPS  * frame_time #객체의 이동거리 -> 등속운동가정
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame_x = int(self.total_frames) % 4
        self.x += distance
        Player.time = self.total_frames

        Player.move_x = self.x

        if Player.move_x >= 500:
            Player.move_x = 500

        if(Player.jump_state):
            Player.CollwithTile = False
            if (self.jump_cnt == 6):
                self.total_jump_cnt = (self.total_jump_cnt + 1) % 10
                self.jump_cnt = 0
            self.jump_cnt = (self.jump_cnt + 1) % 7

            if(self.total_jump_cnt == 1):
                Player.move_y += 25 #Player.RUN_SPEED_MPS * 2
            elif(self.total_jump_cnt == 2):
                Player.move_y += 15 #Player.RUN_SPEED_MPS * 2
            elif (self.total_jump_cnt == 3):
                Player.move_y += 10 #Player.RUN_SPEED_MPS * 2;
            elif(self.total_jump_cnt == 4):
                Player.move_y += 5 #Player.RUN_SPEED_MPS * 2
            elif(self.total_jump_cnt == 5):
                Player.move_y -= 5
            elif(self.total_jump_cnt == 6):
                Player.move_y -= 10
            elif(self.total_jump_cnt == 7):
                Player.move_y -= 15
            elif(self.total_jump_cnt == 8):
                Player.move_y -= 25
            elif(self.total_jump_cnt >= 9):
                Player.jump_state = False
                self.total_jump_cnt = 0
        else:
            Player.move_y -= 10   #점프를 공중에서도 할 수 있다? ->수정


        if(Player.move_y <= 0):
            GameFramework.change_state(ranking_state)
            Player.Player_Die = True
            #Player.Player_Die = True

        #Player.move_y = self.move_y

    def get_bb(self):
         return Player.move_x - 25, Player.move_y - 50, Player.move_x + 25, Player.move_y - 50

    def Draw(self):
        RES.res.Player_image.clip_draw(self.frame_x * 100, self.frame_y * 100, 100, 100, Player.move_x, Player.move_y)
        #print("frame_x : %d , frame_y : %d ,x : %f, y : %f, move_size: %f"  %(self.frame_x , self.frame_y, Player.move_x,Player.move_y,Player.move_size))

    def Draw_boundingbox(self):
        draw_rectangle(*self.get_bb())


