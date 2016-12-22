import PBackground
import PCharacter
import PTile
import PObstacle
import PObject
import GameManager
import PUpBar
import Player_UI
import Button
import Combo
import main_lobby

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
exit_door = None
exit_effect = None

stage_num = 0
stage_tile_cnt = 0

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
    global tile
    global obstacle
    global exit_door
    global exit_effect
    global ranking

    ranking = ranking_state.Ranking_state()

    background = PBackground.Background()
    character = PCharacter.Player()
    stage_object = PObject.StageObject()

    if main_lobby.Song.number == 2:
        stage_tile_cnt = 51


    tile = PTile.Brick(stage_tile_cnt)

    meso = PObject.Point_meso()

    obstacle = PObstacle.Obstacle()

    pinkbin_bar = PUpBar.Pinkbinbar()
    sky_bar = PUpBar.Skybar()
    flying_object_bar = PUpBar.FlyingObject()
    stop_station = PUpBar.Stop_station()
    user_ui = Player_UI.User_UI()
    button = Button.Button_beat()
    combo = Combo.Combo()
    exit_door = PObject.Exit_door()
    exit_effect = PObject.Exit_effect()



    # 발판 생성자 다수생성 -> 임시값
    #PTile.temp = [PTile.Brick() for i in range(50)]

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
    global tile
    global obstacle
    global exit_door
    global exit_effect

    #일부러 남겨둔것 -> 재입력시
    #if (start_cnt == 0):
    #ranking_data = [{"Player": 1, "Point": Player_UI.User_UI.User_point,
    #                 "Combo": Player_UI.User_UI.User_combo,
    #                 "Cool Combo": Player_UI.User_UI.User_coolcombo, "Hit Combo": Player_UI.User_UI.User_hitcombo,
    #                 "Miss": Player_UI.User_UI.User_miss}]
    #f = open('save.txt', 'w')
    #json.dump(ranking_data, f)#
    #f.close()

    f = open('save.txt', 'r')
    ranking_data = json.load(f)


    ranking_data.append(
        {"Player": len(ranking_data) + 1, "Point": Player_UI.User_UI.User_point, "Combo": Player_UI.User_UI.User_combo,
         "Cool Combo": Player_UI.User_UI.User_coolcombo, "Hit Combo": Player_UI.User_UI.User_hitcombo,
         "Miss": Player_UI.User_UI.User_miss})

    f = open('save.txt', 'w')
    json.dump(ranking_data, f)
    f.close()



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
    del (tile)
    del (obstacle)
    del (exit_door)
    del (exit_effect)
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

    if PCharacter.Player.Player_Die == False:
        background.Update()

        if main_lobby.Song.number == 2:
            stage_tile_cnt = 51
            stage_num = 1

        # 탈출 이펙트
        exit_effect.Update()

        tile.Update(stage_tile_cnt)

        # 장애물 업데이트
        obstacle.Update()

        # 메소 포인트 업데이트
        meso.Update_meso()

        # 스테이지 오브젝트 업데이트(돌고래 / 파도)
        stage_object.Update()

        # 상단의 핑크빈 업데이트
        pinkbin_bar.Update()

        # 상단의 날아다니는 오브젝트 업데이트
        flying_object_bar.Update()

        # 상단의 버튼 스톱모션 업데이트
        stop_station.Update()

        # 버튼 업데이트
        button.Update(stage_num)

        # 콤보 업데이트
        combo.Update()

        #탈출 오브젝트 업데이트
        exit_door.Update()





def draw(frame_time):
    #global  stage_tile_cnt
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

    #충돌체크 박스
    #stop_station.Draw_boundingbox()

    user_ui.Draw()
    user_ui.Draw_HP()

    button.Draw()

    combo.Draw()

    character.Draw()
    # 충돌체크 박스
    #character.Draw_boundingbox()

    if main_lobby.Song.number == 2:
        stage_tile_cnt = 51

    tile.Draw(stage_tile_cnt)
    #PTile.Brick.Draw_boundingbox()

    obstacle.Draw()

    meso.Draw_Meso()

    stage_object.Draw()

    exit_door.Draw()

    exit_effect.Draw()

    update_canvas()

