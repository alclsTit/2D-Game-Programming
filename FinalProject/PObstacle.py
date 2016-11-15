from pico2d import *
import PTile
import PCharacter
import random
import Collision
import RES
import Player_UI

List_obstacle = []

character = PCharacter.Player()
tile = PTile.Brick()

class Obstacle:

    pos_x , pos_y = 0 , 0
    Switch_Obstacle = 0
    Obstacle_cnt = 0

    Loop_flag = False

    move_cnt = 0
    Loop_cnt = 0
    define_cnt = 1
    def __init__(self):

        for PTile.Brick in PTile.List_tile:
            Obstacle.move_cnt += 1

            if (Obstacle.move_cnt % 4 == 0):
                for PTile.Brick in PTile.List_tile:
                    Obstacle.Loop_cnt += 1
                    if(Obstacle.Loop_cnt == 4):
                        Obstacle.define_cnt += 1
                        Obstacle.Loop_cnt -= 4 * Obstacle.define_cnt
                        break

                self.Obstacle_num = random.randint(1, 2)  # 장애물의 종류선택

                if (self.Obstacle_num == 1 or self.Obstacle_num == 2):
                    self.height = 50
                    self.die_cnt = 7
                    self.die_flag = False

                if (PTile.Brick.num == 1):
                    self.Brick_width_range = 2000
                elif (PTile.Brick.num == 2):
                    self.Brick_width_range = 1500
                elif (PTile.Brick.num == 3):
                    self.Brick_width_range = 1000
                elif (PTile.Brick.num == 4):
                    self.Brick_width_range = 500
                elif (PTile.Brick.num == 5):  # 부유물1
                    self.Brick_width_range = 400
                elif (PTile.Brick.num == 6):  # 부유물2
                    self.Brick_width_range = 200
                elif (PTile.Brick.num == 7):  # 구름1
                    self.Brick_width_range = 300
                elif (PTile.Brick.num == 8):  # 구름2
                    self.Brick_width_range = 600

                if (PTile.Brick.num == 1 or PTile.Brick.num == 2 or PTile.Brick.num == 3 or PTile.Brick.num == 4):
                    self.Brick_height_range = 150
                elif (PTile.Brick.num == 5):
                    self.Brick_height_range = 120
                elif (PTile.Brick.num == 6):
                    self.Brick_height_range = 80
                elif (PTile.Brick.num == 7 or PTile.Brick.num == 8):
                    self.Brick_height_range = 80

                self.x = PTile.Brick.mid_x + random.randint(0, self.Brick_width_range / 4)
                self.y = PTile.Brick.mid_y + self.Brick_height_range / 2 + self.height - 10
                self.frame_x = 0
                self.total_frame_x = 0
                self.frame_y = random.randint(1, 2)

                List_obstacle.append(self)
            break

    def get_bb(self):
        if (self.Obstacle_num == 1 or self.Obstacle_num == 2):
            return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def Update(self):
        self.frame_x = (self.frame_x + 1) % 6
        if(self.frame_x == 5):
            self.total_frame_x = (self.total_frame_x + 1) % 7

        if(self.die_flag == True):
            self.die_cnt -= 1
            if(self.die_cnt <= 0):
                Player_UI.User_UI.User_point -= 500
                List_obstacle.remove(self)

        if(character.move_x >= 500):
            self.x -= character.move_size

        if (self.x < - 1000):
            self.x = -1000

        if (Collision.collide(character, self)):
            print("Collision  ", self.Obstacle_num)

            self.frame_y = 0
            self.frame_x = 0
            self.die_flag = True


    def Draw(self):
        if(self.Obstacle_num == 1):
            RES.res.First_Obstacle.clip_draw(self.total_frame_x * 100, self.frame_y * 100, 100 ,100, self.x, self.y)

        if(self.Obstacle_num == 2):
            RES.res.Second_Obstacle.clip_draw(self.total_frame_x * 100, self.frame_y * 100, 100, 100, self.x, self.y)


temp = [Obstacle() for i in range(30)]