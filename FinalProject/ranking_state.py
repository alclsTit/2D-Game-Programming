import GameFramework
import RES
from pico2d import *


import main_state
import PCharacter
import start_state

name = "ranking_state"
font = None

def enter():
    global font
    font = load_font('ENCR10B.TTF', 30)

def exit():
    del(RES.res.score_image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_F1):   #랭킹스테이트에서 F1클릭시 메인스테이트로 넘어감
                if PCharacter.Player.Player_Die == False:
                    GameFramework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                    close_canvas()
                #if PCharacter.Player.Player_Die == True:
                #    GameFramework.change_state(start_state)
                #    PCharacter.Player.Player_Die = False

def update(frame_time):
    pass


def my_sort(input):
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[i]['point'] > input[j]['point']:
                input[i], input[j] = input[j], input[i]

def draw_ranking():
    f = open('save.txt','r')
    ranking_data = json.load(f)
    f.close()
    my_sort(ranking_data)

    font.draw(700,800 ,"[Ranking]", (255,0,255))
    y = 0
    for data in ranking_data[:10]:
        font.draw(100, 700 - 50 * y, "(Player : %d Point : %d Combo : %d Cool Combo : %d Hit Combo : %d Miss : %d)" %(data['Player'],data['Point'],
                                     data['Combo'],data['Cool Combo'],data['Hit Combo'],data['Miss']),(0,153,204))
        y += 1

def draw(frame_time):
    clear_canvas()
    RES.res.score_image.draw(750, 450)
    draw_ranking()
    update_canvas()