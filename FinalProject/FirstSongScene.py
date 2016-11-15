import GameFramework
from pico2d import *
import RES

import main_state

name = "FirstSongScene"
logo_time = 0.0
opacify_state = 1.0

def enter():
     pass

def exit():
    del(RES.res.first_song)

def update(frame_time):
    global logo_time
    global opacify_state

    if logo_time > 2.0:
        logo_time = 0
        GameFramework.push_state(main_state)

    opacify_state -= 0.0008
    logo_time += frame_time

    #global name
    #global logo_time

    #if (logo_time > 0.2):
    #    logo_time = 0
    #    GameFramework.push_state(title_state)
    #    #game_framework.quit()
    #logo_time += frame_time

def draw(frame_time):
    global opacify_state

    clear_canvas()
    RES.res.first_song.opacify(opacify_state)
    RES.res.first_song.draw(750,450)
    update_canvas()

def handle_events(frame_time):
    events = get_events()


def pause(): pass
def resume(): pass




