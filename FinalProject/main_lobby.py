import GameFramework
import RES
from pico2d import *

import FirstSongScene

name = "main_lobby"

class Song:
    coll_with_mouse = False
    mouse_x,mouse_y = 0,0

    def __init__(self):
        self.x ,self.y = 750, 450
        self.bgm = load_music('football.mp3')
        self.bgm.set_volume(80)
        self.bgm.repeat_play()

    def update(self):
        if(self.x - 120 < Song.mouse_x and Song.mouse_x < self.x + 120 and self.y - 120 < Song.mouse_y  and Song.mouse_y < self.y + 120):
            Song.coll_with_mouse = True


    #def get_bb(self):
        #return self.x - 120 , self.y - 120, self.x + 120, self.y + 120

def enter():
    global sel_song
    sel_song = Song()


def exit():
    global sel_song
    sel_song.bgm.stop()

    del(RES.res.main_lobby)


def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    global x,y
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        elif (event.type,event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            Song.mouse_x, Song.mouse_y = event.x, 900 - event.y
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                GameFramework.quit()

def update(frame_time):
    global sel_song

    sel_song.update()
    if(Song.coll_with_mouse):
        GameFramework.change_state(FirstSongScene)


def draw(frame_time):
    clear_canvas()
    RES.res.main_lobby.draw(750, 450)
    update_canvas()



