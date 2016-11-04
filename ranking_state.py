import GameFramework
import RES
from pico2d import *


import main_state

name = "ranking_state"
font = None

def enter():
    global font
    font = load_font('ENCR10B.TTF', 20)

def exit():
    del(RES.res.score_image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_F1):   #랭킹스테이트에서 F1클릭시 메인스테이트로 넘어감
                GameFramework.change_state(main_state)


def update(frame_time):
    pass

def draw_ranking():
    def my_sort(input):
        for i in range(len(input)):
            for j in range(i + 1, len(input)):
                if input[i]['point'] > input[j]['point']:
                    input[i], input[j] = input[j], input[i]

    f = open('save.txt','r')
    ranking_data = json.load(f)
    f.close()
    my_sort(ranking_data)

    font.draw(300,500 ,"[Ranking]", (255,0,255))
    y = 0
    for data in ranking_data[:10]:
        font.draw(100, 450 - 40 * y, "(User : %d Point : %d Time : %4.1f x : %3d )" %(data['User'],data['Point'],data['time'],data['x']),(255,0,255))
        y += 1

def draw(frame_time):
    clear_canvas()
    RES.res.score_image.draw(1500, 900)
    draw_ranking()
    update_canvas()