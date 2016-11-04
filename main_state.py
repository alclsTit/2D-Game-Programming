import PBackground
import PCharacter
import PTile
import PObstacle
import pygame
import time
import PObject
import GameManager

import GameFramework
import title_state
import ranking_state

from pico2d import *

name = "main_state"

background = None
character = None
obstacle = None
stage_object = None
meso = None
font = None
sound = None
tile = None

start_cnt = 0

# 초기화 부분
def enter():
    global background
    global character
    global stage_object
    global meso
    global font
    global sound

    background = PBackground.Background()
    character = PCharacter.Player()
    stage_object = PObject.StageObject()
    meso = PObject.Point_meso()
    font = load_font('ENCR10B.TTF', 20)

    pygame.mixer.init()
    sound = pygame.mixer.Sound("Evans[jubeat]_stage01.wav")

    GameFramework.reset_time()

def exit():
    global start_cnt

    if (start_cnt == 0):
        ranking_data = [{"Player": PCharacter.Player_num ,"Point" : PCharacter.Player.point ,"time": PCharacter.Player.time, "x": PCharacter.Player.move_x}]
        f = open('save.txt', 'w')
        json.dump(ranking_data, f)
        f.close()
    else:
        f = open('save.txt', 'r')
        ranking_data = json.load(f)
        f.close()

        if (start_cnt != 0):
            ranking_data.append({"Player": PCharacter.Player_num,"Point" : PCharacter.Player.point ,"time": PCharacter.Player.time, "x": PCharacter.Player.move_x})

        f = open('save.txt', 'w')
        json.dump(ranking_data, f)
        f.close()

    start_cnt += 1
    PCharacter.Player_num += 1

    del(background)
    del(character)
    del(stage_object)
    del(meso)
    del(font)
    del(sound)

    close_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_ESCAPE): #종료
            GameFramework.quit()
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_F1):     #랭킹스테이터스로 넘어감
            GameFramework.change_state(ranking_state)
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_F2):     #타이틀화면으로 넘어감
            GameFramework.change_state(title_state)


running = True
run_sound = True
state = 0

#show_lattice()
def draw(frame_time):
    #global character
    #global background
    #global tile
    #global obstacle
    #global meso
    #global stage_object

    clear_canvas()

    background.Draw()
    character.Draw()

    for PTile.Brick in PTile.List_tile:
        PTile.Brick.Draw()

    for PObstacle.Obstacle in PObstacle.List_obstacle:
        PObstacle.Obstacle.Draw()

    meso.Draw_Meso()

    stage_object.Draw()

    update_canvas()

    # 업데이트 부분
def update(frame_time):
    #global character
    #global background
    #global tile
    #global obstacle
    #global meso
    #global stage_object#

    character.Update(frame_time)
    background.Update()

    for PTile.Brick in PTile.List_tile:
        PTile.Brick.Update()

    for PObstacle.Obstacle in PObstacle.List_obstacle:
        PObstacle.Obstacle.Update()

    meso.Update_meso()
    stage_object.Update()



        #while(running):
   #global frame_time
   #handle_events()

   #for PTile.Brick in PTile.List_tile:
       #PTile.Brick.Update()

   #for PObstacle.Obstacle in PObstacle.List_obstacle:
       #PObstacle.Obstacle.Update()

   #meso.Update_meso()
   #for PObject.StageObejct in PObject.List_meso:
   #    PObject.StageObject.Update_meso()

   #stage_object.Update()
   #clear_canvas()
   #for PTile.Brick in var_steps:
   #    PTile.Brick.Update()

   # 렌더링 부분
   #background.Draw()

   #for PObject.StageObejct in PObject.List_meso:
   #    PObject.StageObject.Draw_Meso()

   #for PObstacle.Obstacle in PObstacle.List_obstacle:
       #PObstacle.Obstacle.Draw()

   #meso.Draw_Meso()

   #character.Draw()

   #for PTile.Brick in PTile.List_tile:
       #PTile.Brick.Draw()

   #stage_object.Draw()

   #update_canvas()

    #시작부터 40초 걸림
   #if(run_sound == True):
        #sound.play()
        #run_sound = False


   #delay(0.1)




#character = PCharacter.Player()
#brick = PTile.Brick()
#
#def main():
#
#    Objects = [brick for i in range(2)]
#
#    # 외부 입력부분
#    def handle_events():
#        global running
#        events = get_events()
#        for event in events:
#            if event.type == SDL_QUIT:
#                running = False
#            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#                running = False
#
#
#    running = True
#    while(running):
#       handle_events()
#
#       # 업데이트 부분
#       PCharacter.Update()
#
#       clear_canvas()
#
#       # 렌더링 부분
#       for PTile in Objects:
#           PTile.Draw()
#
#       PCharacter.Draw()
#
#       update_canvas()
#
#       delay(0.1)
#
#    close_canvas()
#
#if __name__ == '__main__':
#        main()