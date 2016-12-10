from pico2d import *

import random
import RES

class Skybar:
    def __init__(self):
        self.x , self.y =  750, 750

    def Draw(self):
        RES.res.sky_bar.draw(self.x, self.y)


class Pinkbinbar:
    def __init__(self):
        self.x , self.y = 150, 750
        self.frame_x = 0
        self.frame_y = 0
        self.total_frame_x = 0

    def Update(self):
        if (self.frame_x == 7):
            self.total_frame_x = (self.total_frame_x + 1) % 8
        self.frame_x = (self.frame_x + 1) % 8

    def Draw(self):
        RES.res.pinkbin_bar.clip_draw(self.total_frame_x * 300, self.frame_y * 300 , 300, 300, self.x, self.y)

#9마리
class FlyingObject:

    FlyingObject_List = []
    num = 0

    def __init__(self):
        self.x , self.y = random.randint(600, 1400), random.randint(800, 890)
        self.frame_x , self.frame_y = 0, random.randint(0, 1)
        self.total_frame_x = 0

        self.FlyingObject_data = []
        self.FlyingObject_cnt = 0

    def Update(self):

        while(self.FlyingObject_cnt <= 7):
            self.x = random.randint(600, 1400)
            self.y = random.randint(800, 890)
            self.frame_x = 0
            self.frame_y = random.randint(0, 1)
            self.total_frame_x = 0
            self.move_size_x = random.randint(5, 15)
            self.move_size_y = random.randint(5, 15)

            self.FlyingObject_data = [self.x, self.y, self.frame_x, self.frame_y, self.total_frame_x, self.move_size_x, self.move_size_y ]

            FlyingObject.FlyingObject_List.append(self.FlyingObject_data)
            self.FlyingObject_cnt += 1

        FlyingObject.num = 0

        for  FlyingObject.num in range(self.FlyingObject_cnt):
            FlyingObject.FlyingObject_List[FlyingObject.num][0] -= FlyingObject.FlyingObject_List[ FlyingObject.num][5]
            FlyingObject.FlyingObject_List[FlyingObject.num][0] += FlyingObject.FlyingObject_List[ FlyingObject.num][6]

        FlyingObject.num = 0

        for  FlyingObject.num in range(self.FlyingObject_cnt):
            FlyingObject.FlyingObject_List[FlyingObject.num][2] = (FlyingObject.FlyingObject_List[FlyingObject.num][2] + 1) % 4
            if FlyingObject.FlyingObject_List[FlyingObject.num][2] == 3:
                FlyingObject.FlyingObject_List[FlyingObject.num][4] = (FlyingObject.FlyingObject_List[FlyingObject.num][4] + 1) % 3

        FlyingObject.num = 0

        for  FlyingObject.num in range(self.FlyingObject_cnt):
            if FlyingObject.FlyingObject_List[ FlyingObject.num][0] < 600 or FlyingObject.FlyingObject_List[ FlyingObject.num][0] > 1500 or FlyingObject.FlyingObject_List[ FlyingObject.num][1] > 900 or FlyingObject.FlyingObject_List[ FlyingObject.num][1] < 600:
                FlyingObject.FlyingObject_List.remove(FlyingObject.FlyingObject_List[ FlyingObject.num])
                self.FlyingObject_cnt -= 1
                break

    def Draw(self):
        for i in range(self.FlyingObject_cnt):
            RES.res.flying_object_bar.clip_draw(FlyingObject.FlyingObject_List[i][4] * 80, FlyingObject.FlyingObject_List[i][3] * 80, 80, 80,  FlyingObject.FlyingObject_List[i][0], FlyingObject.FlyingObject_List[i][1])

class Stop_station:
    coll_x , coll_y = 400, 675

    def __init__(self):
        self.x ,self.y = 400 , 675
        self.frame = 0
        self.total_frame = 0

    def Update(self):
        self.frame = (self.frame + 1) % 3
        if(self.frame == 2):
            self.total_frame = (self.total_frame + 1) % 30

    def get_bb(self):
        return self.x - 50 , self.y - 50, self.x + 50, self.y + 50

    def Draw(self):
        RES.res.stop_station.clip_draw(self.total_frame * 100, 0 , 100, 100, self.x , self.y)

    def Draw_boundingbox(self):
        draw_rectangle(*self.get_bb())



