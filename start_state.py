import GameFramework
from pico2d import *
import RES

import title_state

name = "StartState"
logo_time = 0.0
opacify_state = 1.0

def enter():
     pass

def exit():
    del(RES.res.logo_image)

def update(frame_time):
    global logo_time
    global opacify_state

    if logo_time > 2.0:
        logo_time = 0
        GameFramework.push_state(title_state)

    opacify_state -= 0.008
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
    RES.res.logo_image.opacify(opacify_state)
    RES.res.logo_image.draw(750,450)
    update_canvas()

def handle_events(frame_time):
    events = get_events()


def pause(): pass
def resume(): pass




