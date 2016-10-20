from pico2d import *

#from array import *
import random
import PCharacter
import Collision

name = "PTile"

List_tile = []

character = PCharacter.Player()

class Brick:
    prev_mid_x, prev_mid_y  =0, 0
    next_mid_x, next_mid_y = 0, 0

    Brick_width_range = 0
    Brick_height_range = 0
    Brick_prev_width = 0
    Brick_prev_height = 0
    Brick_next_width = 0
    Brick_next_height = 0

    state = 0
    cnt = 0
    #클래스 변수 ->객체가 공유
    FBrickImage = None
    SBrickImage = None
    TBrickImage = None
    FOBrickImage = None
    FloatingImage_one = None
    FloatingImage_two = None
    FCloud = None
    SCloud = None

    def __init__(self):
        if (Brick.state == 0):
            self.mid_x = 500
            self.mid_y = 75
            self.num = 3

            self.prev_width = 500
            self.prev_height = 75

            Brick.prev_mid_x = self.mid_x
            Brick.prev_mid_y = self.mid_y
            Brick.Brick_prev_width = self.prev_width
            Brick.Brick_prev_height = self.prev_height

            #공통변수
            Brick.state += 1

            List_tile.append(self)
            #Brick.select_num = self.num
        else:
            #Brick.select_num = random.randint(1, 8)
            self.num = random.randint(1,8)

            #self -> 고유변수
            if (self.num  == 1):
               self.Brick_width_range = 2000
            elif(self.num  == 2):
                self.Brick_width_range = 1500
            elif(self.num  == 3):
                self.Brick_width_range = 1000
            elif(self.num == 4):
                self.Brick_width_range = 500
            elif(self.num  == 5): #부유물1
                self.Brick_width_range = 400
            elif(self.num  == 6): #부유물2
                self.Brick_width_range = 200
            elif(self.num == 7): #구름1
                self.Brick_width_range = 300
            elif(self.num == 8): #구름2
                self.Brick_width_range = 600

            self.Brick_next_width = self.Brick_width_range / 2

            #next_left값은 해당 이미지의 정중앙 x값 ->얘 바꿨음
            self.next_mid_x = Brick.prev_mid_x + Brick.Brick_prev_width + random.randint(100, 300) + self.Brick_next_width

            Brick.Brick_prev_width = self.Brick_width_range / 2

            #발판마다 다른 세로길이가 다르므로 체크
            # self -> 고유변수
            if (self.num == 1 or self.num == 2 or self.num == 3 or self.num == 4):
                self.Brick_height_range = 150
            elif (self.num == 5):
                self.Brick_height_range = 120
            elif (self.num == 6):
                self.Brick_height_range = 80
            elif (self.num == 7 or self.num == 8):
                self.Brick_height_range = 80

            self.Brick_next_height = self.Brick_height_range / 2

            #발판 오브젝트 y축 값(높은 발판, 낮은 발판) 결정하기
            if (self.num % 4 == 0 or self.num % 5 == 0):
                if(self.num % 4 == 0):
                    if (Brick.prev_mid_y >= 350):
                        self.next_mid_y = 350
                    else:
                        #발판의 번호가 4의 배수 일 때
                        #해당 발판의 top은 이전 top + 랜덤값
                        #top은 해당이미지의 정중앙 y값
                        self.next_mid_y = Brick.prev_mid_y + Brick.Brick_prev_height + random.randint(0, 150) + self.Brick_next_height
                else:
                    if (Brick.prev_mid_y <= 80):
                        self.next_mid_y = 80
                    else:
                        # 발판의 번호가 5의 배수 일 때
                        # 해당 발판의 top은 이전 top - 랜덤값
                        self.next_mid_y = Brick.prev_mid_y - Brick.Brick_prev_height - random.randint(0, 150) - self.Brick_next_height
            else:
                #발판의 번호가 4,5의 배수가 아닐 때 = 이전 발판의 높이와 그대로
                self.next_mid_y = Brick.prev_mid_y

            Brick.Brick_prev_height = self.Brick_height_range / 2

            #발판의 top위치 - 해당발판의 세로길이 = 발판의 bottom위치
            #Brick.next_bottom = Brick.next_top - Brick.Brick_height_range

            Brick.prev_mid_x = self.next_mid_x
            Brick.prev_mid_y = self.next_mid_y

            self.mid_x = self.next_mid_x
            self.mid_y = self.next_mid_y

            #self.num = Brick.select_num

            # 발판 오브젝트 이미지 로드
            if (Brick.FBrickImage == None):
                Brick.FBrickImage = load_image('Brick_First.png')
            if (Brick.SBrickImage == None):
                Brick.SBrickImage = load_image('Brick_Second.png')
            if (Brick.TBrickImage == None):
                Brick.TBrickImage = load_image('Brick_Third.png')
            if (Brick.FOBrickImage == None):
                Brick.FOBrickImage = load_image('Brick_Fourth.png')
            if (Brick.FloatingImage_one == None):
                Brick.FloatingImage_one = load_image('Floating_one.png')
            if (Brick.FloatingImage_two == None):
                Brick.FloatingImage_two = load_image('Floating_two.png')
            if (Brick.FCloud == None):
                Brick.FCloud = load_image('Cloud_one.png')
            if (Brick.SCloud == None):
                Brick.SCloud = load_image('Cloud_two.png')

            List_tile.append(self)

    def get_bb(self):
        if(self.num == 1):
            return self.mid_x - 1000, self.mid_y - 75, self.mid_x + 1000, self.mid_y + 75
        elif(self.num == 2):
            return self.mid_x - 750, self.mid_y - 75, self.mid_x + 750, self.mid_y + 75
        elif(self.num == 3):
            return self.mid_x - 500, self.mid_y - 75, self.mid_x + 500, self.mid_y + 75
        elif(self.num == 4):
            return self.mid_x - 250, self.mid_y - 75, self.mid_x + 250, self.mid_y + 75
        elif(self.num == 5):
            return self.mid_x - 200, self.mid_y - 60, self.mid_x + 200, self.mid_y + 60
        elif(self.num == 6):
            return self.mid_x - 100, self.mid_y - 40, self.mid_x + 100, self.mid_y + 40
        elif(self.num == 7):
            return self.mid_x - 150, self.mid_y - 40, self.mid_x + 150, self.mid_y + 40
        elif(self.num == 8):
            return self.mid_x - 300, self.mid_y - 40, self.mid_x + 300, self.mid_y + 40

        #if(Brick.select_num == 1):
        #    return self.mid_x - 1000, self.mid_y - 75, self.mid_x + 1000, self.mid_y + 75
        #elif(Brick.select_num == 2):
        #    return self.mid_x - 750, self.mid_y - 75, self.mid_x + 750, self.mid_y + 75
        #elif(Brick.select_num == 3):
        #    return self.mid_x - 500, self.mid_y - 75, self.mid_x + 500, self.mid_y + 75
        #elif(Brick.select_num == 4):
        #    return self.mid_x - 250, self.mid_y - 75, self.mid_x + 250, self.mid_y + 75
        #elif(Brick.select_num == 5):
        #    return self.mid_x - 200, self.mid_y - 60, self.mid_x + 200, self.mid_y + 60
        #elif(Brick.select_num == 6):
        #    return self.mid_x - 100, self.mid_y - 40, self.mid_x + 100, self.mid_y + 40
        #elif(Brick.select_num == 7):
        #    return self.mid_x - 150, self.mid_y - 40, self.mid_x + 150, self.mid_y + 40
        #elif(Brick.select_num == 8):
        #    return self.mid_x - 300, self.mid_y - 40, self.mid_x + 300, self.mid_y + 40

    def Update(self):
        if(character.move_x >= 500):
            self.mid_x -= character.move_size

        if(self.mid_x < - 1000):
            self.mid_x = -1000
        # and (character.jump_state == True) and (character.jump_cnt > 5)
        #and (PCharacter.Player.move_y - 50 > self.mid_y)

        #if((PCharacter.Player.move_y >= self.mid_y + (self.Brick_height_range / 2)) == True):
            #self.cnt += 1


        #self가 문제 -> 항상 마지막놈을 가리키고있음
        if(Collision.collide(character , self)):
            print("Collision  ", self.num)

            if (self.num == 1 or self.num == 2 or self.num == 3 or self.num == 4):
                self.Brick_height_range = 150
            elif (self.num == 5):
                self.Brick_height_range = 120
            elif (self.num == 6):
                self.Brick_height_range = 80
            elif (self.num == 7 or self.num == 8):
                self.Brick_height_range = 80

            PCharacter.Player.move_y = self.mid_y + (self.Brick_height_range / 2) + 50
            PCharacter.Player.jump_cnt = 0

            #if(character.jump_state == True):#참조
                 #PCharacter.Player.jump_state = False #값 바꿀때

    def Draw(self):
        print(self.mid_x, self.mid_y, self.num)
        if(self.num == 1):
            Brick.FBrickImage.draw(self.mid_x,self.mid_y)
        elif(self.num == 2):
            Brick.SBrickImage.draw(self.mid_x, self.mid_y)
        elif(self.num == 3):
            Brick.TBrickImage.draw(self.mid_x, self.mid_y)
        elif(self.num == 4):
            Brick.FOBrickImage.draw(self.mid_x, self.mid_y)
        elif(self.num == 5):
            Brick.FloatingImage_one.draw(self.mid_x, self.mid_y)
        elif(self.num == 6):
            Brick.FloatingImage_two.draw(self.mid_x, self.mid_y)
        elif(self.num == 7):
            Brick.FCloud.draw(self.mid_x, self.mid_y)
        elif (self.num == 8):
            Brick.SCloud.draw(self.mid_x, self.mid_y)

#발판 생성자 다수생성 -> 임시값
temp = [Brick() for i in range(20)]


