from pico2d import *
import PCharacter
import RES

character = PCharacter.Player()

#open_canvas(1500,900,sync=True)

class Background:

    def __init__(self):
        self.x , self.y = 750 , 450  #시작 지점은 해당 사진의 1/2위치
        self.frame_move = 0
        self.frame_move_second = 0
        self.switching_cnt = 0
        self.bgm = load_music('Evans[jubeat]_stage01.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def Update(self):
        if(PCharacter.Player.move_x >= 500):
            self.frame_move += character.move_size

        if(self.frame_move % 2500 == 0):
            self.frame_move = 0

        if(PCharacter.Player.Player_Die == True):
            self.bgm.stop()

    #def background_soundplay(self):


    def Draw(self):
        RES.res.Background_image.clip_draw(self.frame_move , 0, 1500, 900, self.x , self.y)


