from pico2d import *

#from array import *
import random
import PCharacter
import Collision
import RES

name = "PTile"

character = PCharacter.Player()

class Brick:
    # 클래스 변수 ->객체가 공유
    number = 0
    List_tile = []

    def __init__(self,Brick_num):
        self.mid_x , self.mid_y = 0 , 0
        self.Brick_width_range ,self.Brick_height_range = 0 , 0
        self.next_startx , self.next_starty = 0 , 0

        self.num = 0
        self.IsColled = False

        self.Brick_data = []

        for i in range(Brick_num):
            if  (i == 0):
                self.num = 3
                self.mid_x , self.mid_y = 500 , 75
                self.Brick_width_range ,self.Brick_height_range = 1000 , 150
            elif(i == Brick_num - 1):
                self.num = 3
                self.Brick_width_range, self.Brick_height_range = 1000, 150
                self.mid_x = Brick.List_tile[i - 1][2] + (self.Brick_width_range / 2)
                self.mid_y = 75

                if (self.mid_y >= 300):
                    self.mid_y = 300

                if (self.mid_y <= 75):
                    self.mid_y = 75
            else:
                self.num = random.randint(1, 8)

                if (self.num == 1):     #기본발판 1
                    self.Brick_width_range = 2000
                    self.Brick_height_range = 150
                elif (self.num == 2):   #기본발판 2
                    self.Brick_width_range = 1500
                    self.Brick_height_range = 150
                elif (self.num == 3):   #기본발판 3
                    self.Brick_width_range = 1000
                    self.Brick_height_range = 150
                elif (self.num == 4):   #기본발판 4
                    self.Brick_width_range = 500
                    self.Brick_height_range = 150
                elif (self.num == 5):   #부유물 1
                    self.Brick_width_range = 400
                    self.Brick_height_range = 120
                elif (self.num == 6):   #부유물 2
                    self.Brick_width_range = 200
                    self.Brick_height_range = 80
                elif (self.num == 7):   #구름 1
                    self.Brick_width_range = 300
                    self.Brick_height_range = 80
                elif (self.num == 8):   #구름 2
                    self.Brick_width_range = 600
                    self.Brick_height_range = 80

                self.mid_x = Brick.List_tile[i - 1][2] + (self.Brick_width_range / 2)
                self.mid_y = Brick.List_tile[i - 1][3]

                if(self.mid_y >= 300):
                    self.mid_y = 300

                if(self.mid_y <= 75):
                    self.mid_y = 75

            Brick.number += 1

            # 다음 발판의 시작 위치
            self.next_startx = self.mid_x + self.Brick_width_range / 2 + random.randint(50, 200)
            self.next_starty = self.mid_y + random.randint(-150, 150)

            self.Brick_data = [self.mid_x, self.mid_y,
                               self.next_startx, self.next_starty,
                               self.Brick_width_range / 2, self.Brick_height_range / 2,
                               self.num,
                               Brick.number,
                               self.IsColled]

            Brick.List_tile.append(self.Brick_data)

    #def get_bb(self):
    #    if(self.num == 1):
    #        return self.mid_x - 1000, self.mid_y - 75, self.mid_x + 1000, self.mid_y + 75
    #    elif(self.num == 2):
    #        return self.mid_x - 750, self.mid_y - 75, self.mid_x + 750, self.mid_y + 75
    #    elif(self.num == 3):
    #        return self.mid_x - 500, self.mid_y - 75, self.mid_x + 500, self.mid_y + 75
    #    elif(self.num == 4):
    #        return self.mid_x - 250, self.mid_y - 75, self.mid_x + 250, self.mid_y + 75
    #    elif(self.num == 5):
    #        return self.mid_x - 200, self.mid_y - 60, self.mid_x + 200, self.mid_y + 60
    #    elif(self.num == 6):
    #        return self.mid_x - 100, self.mid_y - 40, self.mid_x + 100, self.mid_y + 40
    #    elif(self.num == 7):
    #        return self.mid_x - 150, self.mid_y - 40, self.mid_x + 150, self.mid_y + 40
    #    elif(self.num == 8):
    #        return self.mid_x - 300, self.mid_y - 40, self.mid_x + 300, self.mid_y + 40

    def collide_brick(self,brick_cnt):
        return Brick.List_tile[brick_cnt][0] - Brick.List_tile[brick_cnt][4] , Brick.List_tile[brick_cnt][1] - Brick.List_tile[brick_cnt][5], Brick.List_tile[brick_cnt][0] + Brick.List_tile[brick_cnt][4] , Brick.List_tile[brick_cnt][1] + Brick.List_tile[brick_cnt][5]

    def Update(self,Brick_num):
        #Run Your Beat는 화면 스크롤링을 택하고있음
        #따라서 캐릭터는 고정되있고 화면이 이동
        #따라서 화면을 구성하는 객체도 일정하게 이동해줘야한다
        if(PCharacter.Player.move_x >= 500):
            for i in range(Brick_num):
                Brick.List_tile[i][0] -= PCharacter.Player.move_size

                if Brick.List_tile[i][0] <= -1500:
                    Brick.List_tile[i][0] = -1500

        for i in range(Brick_num):
            if Collision.collide_for_brick(character, self , i):
                Brick.List_tile[i][8] = True
            else:
                Brick.List_tile[i][8] = False

            if Brick.List_tile[i][8] == True :
                PCharacter.Player.CollwithTile = True

                PCharacter.Player.move_y = Brick.List_tile[i][1] + Brick.List_tile[i][5] + character.half_height

                PCharacter.Player.jump_cnt = 0

        #종료조건
        for i in range(Brick_num):
            if Brick.List_tile[i][8] == True and i == Brick_num:
                PCharacter.Player.move_size = 0

    def Draw(self,stage_tile_cnt):
        for i in range(stage_tile_cnt):
            if  Brick.List_tile[i][6] == 1:
                RES.res.FBrickImage.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])
            elif  Brick.List_tile[i][6] == 2:
                RES.res.SBrickImage.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])
            elif  Brick.List_tile[i][6] == 3:
                RES.res.TBrickImage.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])
            elif  Brick.List_tile[i][6] == 4:
                RES.res.FOBrickImage.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])
            elif  Brick.List_tile[i][6] == 5:
                RES.res.FloatingImage_one.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])
            elif  Brick.List_tile[i][6] == 6:
                RES.res.FloatingImage_two.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])
            elif  Brick.List_tile[i][6] == 7:
                RES.res.FCloud.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])
            elif  Brick.List_tile[i][6] == 8:
                RES.res.SCloud.draw(Brick.List_tile[i][0], Brick.List_tile[i][1])


                # self가 문제 -> 항상 마지막놈을 가리키고있음
                # f(Collision.collide(character , self)):
                #   print("Collision  ", self.num)

                #   if (self.num == 1 or self.num == 2 or self.num == 3 or self.num == 4):
                #       self.Brick_height_range = 150
                #   elif (self.num == 5):
                #       self.Brick_height_range = 120
                #   elif (self.num == 6):
                #       self.Brick_height_range = 80
                #   elif (self.num == 7 or self.num == 8):
                #       self.Brick_height_range = 80

                #   PCharacter.Player.CollwithTile = True
                #   PCharacter.Player.move_y = self.mid_y + (self.Brick_height_range / 2) + 50
                #   PCharacter.Player.jump_cnt = 0

                #   #if(character.jump_state == True):#참조
                #        #PCharacter.Player.jump_state = False #값 바꿀때

        #print(self.mid_x, self.mid_y, self.num)
        #if(self.num == 1):
        #    RES.res.FBrickImage.draw(self.mid_x,self.mid_y)
        #elif(self.num == 2):
        #    RES.res.SBrickImage.draw(self.mid_x, self.mid_y)
        #elif(self.num == 3):
        #    RES.res.TBrickImage.draw(self.mid_x, self.mid_y)
        #elif(self.num == 4):
        #    RES.res.FOBrickImage.draw(self.mid_x, self.mid_y)
        #elif(self.num == 5):
        #    RES.res.FloatingImage_one.draw(self.mid_x, self.mid_y)
        #elif(self.num == 6):
        #    RES.res.FloatingImage_two.draw(self.mid_x, self.mid_y)
        #elif(self.num == 7):
        #    RES.res.FCloud.draw(self.mid_x, self.mid_y)
        #elif (self.num == 8):
        #    RES.res.SCloud.draw(self.mid_x, self.mid_y)

    #def Draw_boundingbox(self):
    #    draw_rectangle(*self.get_bb())

#Brick.prev_mid_x, Brick.prev_mid_y = 0, 0
#Brick.next_mid_x, Brick.next_mid_y = 0, 0
#
#Brick.Brick_width_range = 0
#Brick.Brick_height_range = 0
#Brick.Brick_prev_width = 0
#Brick.Brick_prev_height = 0
#Brick.Brick_next_width = 0
#Brick.Brick_next_height = 0
#
#Brick.state = 0


