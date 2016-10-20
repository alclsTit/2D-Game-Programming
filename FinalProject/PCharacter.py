from pico2d import *
import math

name = "PCharacter"

#var_steps = [PTile.Brick() for i in range(20)]

#캐릭터 현재위치, 동작 변화, 이미지 로드, 스테이터스
class Player:
    jump_cnt = 0
    move_x = 0
    move_y = 0
    move_size = 50

    jump_state = False

    def __init__(self):
        self.x , self.y = 0 , 200
        self.frame_x = 0
        self.frame_y = 9
        self.image = load_image('character_ani.png')
        self.hp = 100

        Player.move_x = self.x
        Player.move_y = self.y

     #50은 캐릭터의 정중앙으로부터 양쪽간의 거리
    def get_bb(self):
           return Player.move_x - 50, Player.move_y - 50,  Player.move_x + 50 , Player.move_y + 50

    def Update(self):
        self.frame_x = (self.frame_x + 1) % 4

        Player.move_x += 50

        if Player.move_x >= 500:
            Player.move_x = 500

        if(Player.jump_state):
            Player.jump_cnt += 1
            if(Player.jump_cnt == 1):
                Player.move_y += 10
            elif(Player.jump_cnt == 2):
                Player.move_y += 30
            elif (Player.jump_cnt == 3):
                Player.move_y += 60
            elif(Player.jump_cnt == 4):
                Player.move_y += 100
            elif(Player.jump_cnt > 5):
                Player.jump_state = False
        else:
            Player.move_y -= math.sqrt(2 * 10 * Player.move_y)

        #for PTile.Brick in var_steps:
        #    if Collision.collide(PTile.Brick,Player):
        #        print("Collision")
        #        self.y = PTile.Brick.mid_y + PTile.Brick.Brick_height_range / 2


    def Draw(self):
        self.image.clip_draw(self.frame_x * 100, self.frame_y * 100, 100, 100, Player.move_x, Player.move_y)



