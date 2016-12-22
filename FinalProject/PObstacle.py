from pico2d import *
import PTile
import PCharacter
import random
import Collision
import RES
import Player_UI



character = PCharacter.Player()
#tile = PTile.Brick()

class Obstacle:

    Obstacle_List = []
    total_Obstacle_num = 0

    def __init__(self):
        self.num = 0
        self.height = 40

        self.half_height = 50
        self.half_width  = 50

        self.mid_x , self.mid_y = 0 , 0
        self.die_cnt , self.die_flag = 7 , False
        self.frame_x , self.frame_y = 0, 0
        self.total_frame_x = 0
        self.show_once = False

        self.Obstacle_data = []

        for i in range(PTile.Brick.number):
         if (PTile.Brick.List_tile[i][7] % 4 == 0):
            self.num = random.randint(1, 2)  # 장애물의 종류선택

            #if (self.num == 1 or self.num == 2):
            #    self.height = 50
            #    self.die_cnt = 7
            #    self.die_flag = False

            self.mid_x = PTile.Brick.List_tile[i][0] + random.randint(0, PTile.Brick.List_tile[i][4] / 2)
            self.mid_y = PTile.Brick.List_tile[i][1] + PTile.Brick.List_tile[i][5] + self.height

            self.frame_x = 0
            self.frame_y = random.randint(1, 2)

            #9
            self.Obstacle_data = [self.mid_x, self.mid_y, self.frame_x, self.frame_y, self.total_frame_x, self.num, Obstacle.total_Obstacle_num, self.die_flag, self.die_cnt,self.show_once]

            Obstacle.Obstacle_List.append(self.Obstacle_data)

            Obstacle.total_Obstacle_num += 1

    def collide_obstacle(self,Obstacle_num):
        #if (self.Obstacle_num == 1 or self.Obstacle_num == 2):
            return Obstacle.Obstacle_List[Obstacle_num][0] - self.half_width, Obstacle.Obstacle_List[Obstacle_num][1] - self.half_height, Obstacle.Obstacle_List[Obstacle_num][0] + self.half_width, Obstacle.Obstacle_List[Obstacle_num][1] + self.half_height

    def Update(self):

        #장애물 이미지프레임변화
        for i in range(Obstacle.total_Obstacle_num):

            if(Obstacle.Obstacle_List[i][7] == True):
                Obstacle.Obstacle_List[i][2] = (Obstacle.Obstacle_List[i][2] + 1) % 5
                if Obstacle.Obstacle_List[i][2] == 4    :
                    Obstacle.Obstacle_List[i][4] = (Obstacle.Obstacle_List[i][4] + 1) % 7
                    Obstacle.Obstacle_List[i][8] -= 1
            else:
                Obstacle.Obstacle_List[i][2] = (Obstacle.Obstacle_List[i][2] + 1) % 6
                if (Obstacle.Obstacle_List[i][2] == 5):
                    Obstacle.Obstacle_List[i][4] = (Obstacle.Obstacle_List[i][4] + 1) % 7

            if (Obstacle.Obstacle_List[i][8] <= 0):
                Obstacle.Obstacle_List.remove(Obstacle.Obstacle_List[i])
                Obstacle.total_Obstacle_num -= 1
                break

        #캐릭터 이동에 따른 장애물 이동
        if(character.move_x >= 500):
            for i in range(Obstacle.total_Obstacle_num):
                Obstacle.Obstacle_List[i][0] -= character.move_size

                if (Obstacle.Obstacle_List[i][0] <= - 1000):
                    Obstacle.Obstacle_List[i][0] = -1000

        #장애물 충돌체크
        for i  in range(Obstacle.total_Obstacle_num):
            if (Collision.collide_for_obstacle(character, self,i)):
                #print("Collision  ", self.Obstacle_num)
                if Obstacle.Obstacle_List[i][9] == False:
                     #장애물 죽는 모션 이미지 프레임 = 0

                    Player_UI.User_UI.User_point -= 1000
                    Player_UI.User_UI.User_HP -= 10

                    Obstacle.Obstacle_List[i][3] = 0
                    Obstacle.Obstacle_List[i][4] = 0
                    Obstacle.Obstacle_List[i][7] = True
                    Obstacle.Obstacle_List[i][9] = True

    def Draw(self):
        for i in range(Obstacle.total_Obstacle_num):
            if(Obstacle.Obstacle_List[i][5] == 1):
                RES.res.First_Obstacle.clip_draw(Obstacle.Obstacle_List[i][4] * 100, Obstacle.Obstacle_List[i][3] * 100,
                                                 100 ,100,
                                                 Obstacle.Obstacle_List[i][0], Obstacle.Obstacle_List[i][1])

            if(Obstacle.Obstacle_List[i][5] == 2):
                RES.res.Second_Obstacle.clip_draw(Obstacle.Obstacle_List[i][4] * 100, Obstacle.Obstacle_List[i][3] * 100,
                                                  100 ,100,
                                                  Obstacle.Obstacle_List[i][0], Obstacle.Obstacle_List[i][1])


#temp = [Obstacle() for i in range(30)]