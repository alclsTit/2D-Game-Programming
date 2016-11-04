import GameFramework
import RES
from pico2d import *

import main_state

name = "TitleState"

def enter():
    pass

def exit():
    del(RES.res.title_image)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                GameFramework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                GameFramework.change_state(main_state)



def update(frame_time):
    pass


def draw(frame_time):
    clear_canvas()
    RES.res.title_image.draw(750, 450)
    update_canvas()



