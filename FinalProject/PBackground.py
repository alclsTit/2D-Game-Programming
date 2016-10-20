from pico2d import *
import PCharacter

open_canvas(1500, 900)

character = PCharacter.Player()

class Background:
    Background_image = None

    def __init__(self):
        self.x , self.y = 750 , 450  #시작 지점은 해당 사진의 1/2위치
        self.frame_move = 0
        self.frame_move_second = 0
        self.switching_cnt = 0

        if Background.Background_image == None:
            Background.Background_image = load_image('FirstStage_s.png')

    def Update(self):
        if(character.move_x >= 500):
           self.frame_move += character.move_size

        if(self.frame_move % 2500 == 0):
            self.frame_move = 0


    def Draw(self):
           self.Background_image.clip_draw(self.frame_move , 0, 1500, 900, self.x , self.y)


