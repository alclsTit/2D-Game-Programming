from pico2d import *
import random
import PCharacter
import PTile
import Collision
import GameManager
import RES
import Player_UI
import GameFramework
import ranking_state

character = PCharacter.Player()

class StageObject:

    def __init__(self):
        #[파도 애니메이션]발판 오브젝트보다 낮게 구현
        self.front_x ,self.front_y = 0 , 30
        self.mid_x, self.mid_y = 750, 30
        self.back_x,self.back_y = 1500, 30

        #[돌고래 등장 애니메이션]
        self.show_dolpin = False
        self.dolpin_state = 0
        self.dolpin_timer = 0
        self.dol_pos_x , self.dol_pos_y = PCharacter.Player.move_x + random.randint(100,1400) , 50
        self.dolpin_frame = 0
        self.dolpin_stop = 0

    def Update(self):
        #파도 업데이트
        self.front_x += 20
        self.mid_x += 20
        self.back_x -= 20

        if (self.front_x >= 1500):
            self.front_x = 0

        if (self.mid_x >= 2250):
            self.mid_x = 750

        if (self.back_x <= 0):
            self.back_x = 1500

         #돌고래 업데이트
        self.dolpin_timer += 1
        if( self.dolpin_timer  >= 160):

            self.dolpin_stop = (self.dolpin_stop + 1) %11

            if(self.dolpin_state == 0 and self.dolpin_stop == 1 ):
                self.show_dolpin = True
            elif(self.dolpin_state == 1 and self.dolpin_stop == 1 ):
                self.dol_pos_y += 50
            elif(self.dolpin_state == 2 and self.dolpin_stop == 1 ):
                self.dol_pos_y += 100
                self.dol_pos_x -= 50
            elif(self.dolpin_state == 3 and self.dolpin_stop == 1 ):
                self.dol_pos_x -= 50
                self.dol_pos_y -= 20
            elif(self.dolpin_state == 4 and self.dolpin_stop == 1 ):
                self.dol_pos_x -= 50
                self.dol_pos_y -= 40
            elif (self.dolpin_state == 5 and self.dolpin_stop == 1):
                self.dol_pos_x -= 20
                self.dol_pos_y -= 80


            if (self.dolpin_stop == 10):
                self.dolpin_state += 1
                self.dolpin_frame += 1

            if(self.dolpin_state >= 6):
                self.dolpin_state = 0
                self.dolpin_frame = 0
                self.show_dolpin = False
                self.dolpin_timer = 0
                self.dol_pos_x = PCharacter.Player.move_x + random.randint(100, 1400)
                self.dol_pos_y = 50

    def Draw(self):
        RES.res.Wave_image.draw(self.front_x, self.front_y)
        RES.res.Wave_image.draw(self.mid_x, self.mid_y)
        RES.res.Wave_image.draw(self.back_x, self.back_y)

        if (self.show_dolpin == True):
            RES.res.dolpin_image.clip_draw(self.dolpin_frame * 200, 0, 200, 200, self.dol_pos_x,
                                           self.dol_pos_y)
            RES.res.dolpin_image.clip_draw(self.dolpin_frame * 200, 0, 200, 200, self.dol_pos_x - 200,
                                           self.dol_pos_y)

class Exit_door:
    Exit_flag = False
    Change_theme= False
    Show_once = False

    def __init__(self):
        self.mid_x = PTile.Brick.List_tile[PTile.Brick.number - 1][0]
        self.mid_y = PTile.Brick.List_tile[PTile.Brick.number - 1][1]

        self.half_width , self.half_height = 400 , 200

        self.change_theme = False
        self.change_scene_cnt = 0

    def Update(self):
        if PCharacter.Player.move_x >= 500:
            self.mid_x -= PCharacter.Player.move_size

        if PCharacter.Player.move_x >= self.mid_x:
            Exit_door.Exit_flag = True

            if Exit_door.Show_once == False:
                Exit_door.Show_once = True
                Exit_door.change_theme = True

            PCharacter.Player.move_size = 0

        if Exit_door.Exit_flag == True:
            if Exit_door.change_theme == True:
                #self.bgm = load_music('ending_theme.mp3')
                #self.bgm.set_volume(60)
                #self.bgm.repeat_play()
                Exit_door.change_theme = False

            self.change_scene_cnt += 1

            if self.change_scene_cnt >= 120:
                self.change_scene_cnt = 0
                GameFramework.change_state(ranking_state)



        #if Exit_door.Exit_flag == True:
        #    self.change_theme = True
        #    self.bgm.repeat_play()

        #if self.change_theme == True:
        #    self.bgm.repeat_play()
        #    self.change_theme = False

    def Draw(self):
        RES.res.Exit_door.draw(self.mid_x, self.mid_y * 2 + self.half_height)

class Exit_effect:
    def __init__(self):
        self.mid_x = PTile.Brick.List_tile[PTile.Brick.number - 1][0]
        self.mid_y = PTile.Brick.List_tile[PTile.Brick.number - 1][1]

        self.half_width , self.half_height = 500 , 150
        self.start_height = 800

        self.frame_x, self.frame_y = 0 , 0
        self.total_frame_y = 0
        self.show_time = 0

    def Update(self):
        if Exit_door.Exit_flag == True:

            if self.show_time >= 5:
               self.show_time = 5
            else:
               self.show_time += 1

            if self.show_time >= 5:
                self.mid_x = 750

                if self.start_height == self.half_height + self.mid_y * 2:
                    self.total_frame_y = 4
                else:
                    self.frame_y = (self.frame_y + 1) % 5

                if self.frame_y == 4:
                    self.total_frame_y = (self.total_frame_y + 1) % 6

                if self.start_height <= self.half_height + self.mid_y * 2:
                    self.start_height = self.half_height + self.mid_y * 2
                else:
                    self.start_height -= 30

    def Draw(self):
        RES.res.Exit_effect.clip_draw(self.frame_x * 1000, (4 - self.total_frame_y) * 300 ,1000, 300, self.mid_x,  self.start_height)

class Point_meso:
    meso_counting = 0

    #메소의 이전 위치값 계산변수
    prev_meso_x = 0
    prev_meso_y = 0

    # [메소(포인트) 만들기]
    meso_width_size , meso_height_size = 25 , 20
    big_meso_width_size , big_meso_height_size = 50 , 40
    bronze_point , silver_point , gold_point = 20 ,50 ,100
    IsFirst = True
    coin_num = 0
    meso_range = 50

    def __init__(self):
        # 메소 x,y값 초기화
        self.meso_x , self.meso_y = 0 , 0

        self.meso_frame_x , self.meso_frame_y = 0 , 1
        self.meso_total_frame_x = 0

        self.define_meso_pos = 0

        self.define_rand_ypos , self.meso_rand_y = 0 , 0
        self.rand_ypos_fix = 0


        # 메소 포인트
        self.define_rcolor = 0
        self.point = 0

        # 메소 사라질때
        self.disappear_cnt = 0

        # 메소 저장소
        self.Store_meso = []
        self.IsDamaged = False

        Point_meso.meso_counting = 0
        Point_meso.prev_meso_x = 0
        Point_meso.prev_meso_y = 0
        Point_meso.IsFirst = True
        Point_meso.coin_num = 0

        # 발판 위에 메소(포인트) 생성
        for i in range(PTile.Brick.number):
            # 첫 발판은 메소를 생성하지 않는다
            if Point_meso.IsFirst == True:
                Point_meso.IsFirst = False
                continue

            while (True):
                # 발판이 끝날때 까지 메소생성
                if (self.meso_x + self.meso_width_size > PTile.Brick.List_tile[i][0] + PTile.Brick.List_tile[i][4]):
                    self.define_meso_pos = 0
                    break
                else:
                    if (self.rand_ypos_fix == 0):
                        self.define_rand_ypos = random.randint(1, 7)

                    self.rand_ypos_fix = (self.rand_ypos_fix + 1) % 6

                    if (self.define_rand_ypos == 1):
                        self.meso_rand_y = 0
                    elif (self.define_rand_ypos == 2):
                        self.meso_rand_y = 15
                    elif (self.define_rand_ypos == 3):
                        self.meso_rand_y = -15
                    elif (self.define_rand_ypos == 4):
                        self.meso_rand_y = 35
                    elif (self.define_rand_ypos == 5):
                        self.meso_rand_y = -35
                    elif (self.define_rand_ypos == 6):
                        self.meso_rand_y = 60
                    elif (self.define_rand_ypos == 7):
                        self.meso_rand_y = -60

                    if (self.define_meso_pos == 0):
                        self.meso_x = PTile.Brick.List_tile[i][0] - PTile.Brick.List_tile[i][4] + Point_meso.meso_range
                        self.meso_y = PTile.Brick.List_tile[i][1] + PTile.Brick.List_tile[i][5] + self.meso_height_size

                        self.define_meso_pos += 1

                        # 메소의 색깔에따라 포인트 다르게주기 -> 주기적으로
                        self.define_rcolor = random.randint(1, 3)
                        if (self.define_rcolor == 1):
                            self.point = self.bronze_point
                        elif (self.define_rcolor == 2):
                            self.point = self.silver_point
                        else:
                            self.point = self.gold_point
                    else:
                        self.meso_x = Point_meso.prev_meso_x + self.meso_width_size + Point_meso.meso_range
                        self.meso_y = Point_meso.prev_meso_y + self.meso_rand_y

                        #최대로 메소가 생성 될 수 있는 위치 500
                        if (self.meso_y  > 500):
                            self.meso_y = 500
                         #생성된 메소가 발판보다 낮은 위치에 생성될 때
                        if (self.meso_y <= PTile.Brick.List_tile[i][1] + PTile.Brick.List_tile[i][5]):
                            self.meso_y = PTile.Brick.List_tile[i][1] + PTile.Brick.List_tile[i][5] + self.meso_height_size

                    Point_meso.prev_meso_x = self.meso_x
                    Point_meso.prev_meso_y = self.meso_y

                    #메소저장소(x, y위치 , 프레임x,y ,포인트 , 삭제카운트)
                    self.Store_meso = [self.meso_x , self.meso_y , self.meso_frame_x, self.meso_frame_y , self.point , self.disappear_cnt, self.IsDamaged, self.meso_total_frame_x]

                    #코인 수 저장
                    Point_meso.coin_num += 1
                    Point_meso.meso_total_frame_x = 0
                    # 메소 리스트 만들어 위치(x,y)값 , 프레임값, 포인트값 집어넣기
                    GameManager.List_meso.append(self.Store_meso)

    def Update_meso(self):
       #메소(포인트) 업데이트
       for i in range(self.coin_num):
             #if(GameManager.List_meso[i][0] >= 0 and GameManager.List_meso[i][0] <= 1500):  #화면에 보이는 메소들만 충돌체크
             if(Collision.collide_for_coin(character,self,i)):
                GameManager.List_meso[i][3] = 0
                GameManager.List_meso[i][6] = True

             if (PCharacter.Player.move_x >= 500):
                  GameManager.List_meso[i][0] -= character.move_size

       Point_meso.meso_counting = 0

       #메소 프레임 업데이트
       for Point_meso.meso_counting in range(self.coin_num):
           GameManager.List_meso[Point_meso.meso_counting][2] = (GameManager.List_meso[Point_meso.meso_counting][2] + 1) % 11
           if(GameManager.List_meso[Point_meso.meso_counting][2] == 10):
               GameManager.List_meso[Point_meso.meso_counting][7] = (GameManager.List_meso[Point_meso.meso_counting][7] + 1) % 4

       Point_meso.meso_counting = 0

       # 메소와 캐릭터간의 충돌체크
       for Point_meso.meso_counting in range(self.coin_num):
           if(GameManager.List_meso[Point_meso.meso_counting][6] == True):
               if(GameManager.List_meso[Point_meso.meso_counting][5] == 4):
                   Player_UI.User_UI.User_point += GameManager.List_meso[Point_meso.meso_counting][4]
                   GameManager.List_meso.remove(GameManager.List_meso[Point_meso.meso_counting])
                   self.coin_num  -= 1
                   break
                   #Point_meso.meso_counting -= 1
               else:
                   if (GameManager.List_meso[Point_meso.meso_counting][5] == 0):
                       GameManager.List_meso[Point_meso.meso_counting][1] += 5
                   elif (GameManager.List_meso[Point_meso.meso_counting][5] == 1):
                       GameManager.List_meso[Point_meso.meso_counting][1] += 10
                   elif (GameManager.List_meso[Point_meso.meso_counting][5] == 2):
                       GameManager.List_meso[Point_meso.meso_counting][1] += 15
                   elif (GameManager.List_meso[Point_meso.meso_counting][5] == 3):
                       GameManager.List_meso[Point_meso.meso_counting][1] += 20
                   GameManager.List_meso[Point_meso.meso_counting][5] += 1

       Point_meso.meso_counting = 0

    def collide_meso(self,meso_num):
       return GameManager.List_meso[meso_num][0] - self.meso_width_size , GameManager.List_meso[meso_num][1] - self.meso_height_size, GameManager.List_meso[meso_num][0] + self.meso_width_size , GameManager.List_meso[meso_num][1] + self.meso_height_size


    def Draw_Meso(self):
        for i in range(self.coin_num):
            if (GameManager.List_meso[i][4] == 20): #x_frame, y_frame, width / 2, height / 2, x_pos, y_pos
                RES.res.bronze_meso_image.clip_draw(GameManager.List_meso[i][7] * 50, GameManager.List_meso[i][3] * 40, 50, 40, GameManager.List_meso[i][0] ,GameManager.List_meso[i][1])
            elif(GameManager.List_meso[i][4] == 50):
                RES.res.silver_meso_image.clip_draw(GameManager.List_meso[i][7] * 50, GameManager.List_meso[i][3] * 40, 50, 40, GameManager.List_meso[i][0] ,GameManager.List_meso[i][1])
            elif(GameManager.List_meso[i][4] == 100):
                RES.res.gold_meso_image.clip_draw(GameManager.List_meso[i][7] * 50, GameManager.List_meso[i][3] * 40, 50, 40, GameManager.List_meso[i][0] ,GameManager.List_meso[i][1])



