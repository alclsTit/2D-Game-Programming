import PBackground
import PCharacter
import PTile
import PObstacle
import pygame
import time
import PObject
import GameManager
import PUpBar
import Player_UI
import Button
import Combo

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
pinkbin_bar = None
sky_bar = None
flying_object_bar = None
stop_station = None
button = None
combo = None

start_cnt = 0
start_sound = 0
Player_num = 0

# 초기화 부분
def enter():
    global background
    global character
    global stage_object
    global meso
    global font
    global sound
    global pinkbin_bar
    global sky_bar
    global flying_object_bar
    global stop_station
    global user_ui
    global button
    global combo

    background = PBackground.Background()
    character = PCharacter.Player()
    stage_object = PObject.StageObject()

    meso = PObject.Point_meso()

    pinkbin_bar = PUpBar.Pinkbinbar()
    sky_bar = PUpBar.Skybar()
    flying_object_bar = PUpBar.FlyingObject()
    stop_station = PUpBar.Stop_station()
    user_ui = Player_UI.User_UI()
    button = Button.Button_beat()
    combo = Combo.Combo()

    font = load_font('ENCR10B.TTF', 20)

    GameFramework.reset_time()


def exit():
    global start_cnt
    global Player_num
    global ranking_data

    global background
    global character
    global stage_object,meso
    global font, sound
    global sky_bar, pinkbin_bar, flying_object_bar, stop_station, button
    global user_ui
    global combo

    if (start_cnt == 0):
        ranking_data = [{"Player": Player_num,"Point" : Player_UI.User_UI.User_point, "Combo" : Player_UI.User_UI.User_combo,
                         "Cool Combo" : Player_UI.User_UI.User_coolcombo, "Hit Combo" : Player_UI.User_UI.User_hitcombo,
                         "Miss" : Player_UI.User_UI.User_miss}]
        f = open('save.txt', 'w')
        json.dump(ranking_data, f)
        f.close()
    else:
        f = open('save.txt', 'r')
        ranking_data = json.load(f)
        f.close()

        if (start_cnt != 0):
            ranking_data.append({"Player": Player_num,"Point" : Player_UI.User_UI.User_point, "Combo" : Player_UI.User_UI.User_combo,
                                 "Cool Combo": Player_UI.User_UI.User_coolcombo, "Hit Combo": Player_UI.User_UI.User_hitcombo,
                                 "Miss": Player_UI.User_UI.User_miss})

        f = open('save.txt', 'w')
        json.dump(ranking_data, f)
        f.close()

    start_cnt += 1
    Player_num += 1

    del (background)
    del (character)
    del (stage_object)
    del (meso)
    del (font)
    del (sound)
    del (sky_bar)
    del (pinkbin_bar)
    del (flying_object_bar)
    del (stop_station)
    del (user_ui)
    del (button)
    del (combo)
    #close_canvas()

def pause():
    pass


def resume():
    pass

key_count = 0
def handle_events(frame_time):
    global  key_count
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_ESCAPE): #종료
            GameFramework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_SPACE):
            if PCharacter.Player.CollwithTile == True:
                PCharacter.Player.jump_state = True
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_F1):     #랭킹스테이터스로 넘어감
            GameFramework.change_state(ranking_state)
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_F2):     #타이틀화면으로 넘어감
            GameFramework.change_state(title_state)
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_a):
            key_count = 0

            Button.Button_beat.a_button = True
            Button.Button_beat.s_button = False
            Button.Button_beat.d_button = False
            Button.Button_beat.f_button = False
            Button.Button_beat.b_button = False
        elif (event.type , event.key) == (SDL_KEYDOWN,SDLK_s):
            key_count = 0

            Button.Button_beat.a_button = False
            Button.Button_beat.s_button = True
            Button.Button_beat.d_button = False
            Button.Button_beat.f_button = False
            Button.Button_beat.b_button = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            key_count = 0

            Button.Button_beat.a_button = False
            Button.Button_beat.s_button = False
            Button.Button_beat.d_button = True
            Button.Button_beat.f_button = False
            Button.Button_beat.b_button = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_f):
            key_count = 0

            Button.Button_beat.a_button = False
            Button.Button_beat.s_button = False
            Button.Button_beat.d_button = False
            Button.Button_beat.f_button = True
            Button.Button_beat.b_button = False
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_b):
            key_count = 0

            Button.Button_beat.a_button = False
            Button.Button_beat.s_button = False
            Button.Button_beat.d_button = False
            Button.Button_beat.f_button = False
            Button.Button_beat.b_button = True

running = True
run_sound = True
state = 0

#show_lattice()

 # 업데이트 부분
def update(frame_time):

    #키를 누르지 않고 있을시 일정시간 뒤 초기화
    global key_count
    if key_count == 4:
        Button.Button_beat.a_button = False
        Button.Button_beat.s_button = False
        Button.Button_beat.d_button = False
        Button.Button_beat.f_button = False
        Button.Button_beat.b_button = False

    key_count = (key_count + 1) % 5

    character.Update(frame_time)
    background.Update()

    for PTile.Brick in PTile.List_tile:
        PTile.Brick.Update()

    for PObstacle.Obstacle in PObstacle.List_obstacle:
        PObstacle.Obstacle.Update()

    meso.Update_meso()

    stage_object.Update()

    pinkbin_bar.Update()

    flying_object_bar.Update()

    stop_station.Update()

    button.Update(1)

    combo.Update()

def draw(frame_time):
    # global character
    # global background
    # global tile
    # global obstacle
    # global m
    # global stage_object

    clear_canvas()
    background.Draw()

    #바 드로우
    sky_bar.Draw()
    pinkbin_bar.Draw()

    flying_object_bar.Draw()

    stop_station.Draw()
    stop_station.Draw_boundingbox()

    user_ui.Draw()

    button.Draw()

    combo.Draw()

    character.Draw()
    character.Draw_boundingbox()

    for PTile.Brick in PTile.List_tile:
        PTile.Brick.Draw()
        #PTile.Brick.Draw_boundingbox()

    for PObstacle.Obstacle in PObstacle.List_obstacle:
        PObstacle.Obstacle.Draw()

    meso.Draw_Meso()

    stage_object.Draw()

    update_canvas()

