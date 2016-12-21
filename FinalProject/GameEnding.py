import GameFramework
import RES
import ranking_state
from pico2d import *

#import PBackground
#import PCharacter
#import PTile
#import PObstacle
#import PObject
#import GameManager
#import PUpBar
#import Player_UI
#import Button
#import Combo
#import main_lobby

name = "Game_Ending"
class Ending:
    def __init__(self):
        self.bgm = load_music('virus.mp3')
        self.bgm.set_volume(80)
        self.bgm.repeat_play()

def enter():
    global game_ending
    game_ending = Ending()

    #global font
    #font = load_font('ENCR10B.TTF', 30)

def exit():
    #global background
    #global character
    #global stage_object, meso
    #global font, sound
    #global sky_bar, pinkbin_bar, flying_object_bar, stop_station, button
    #global user_ui
    #global combo
    #global tile
    #global obstacle

    #del (background)
    #del (character)
    #del (stage_object)
    #del (meso)
    #del (font)
    #del (sound)
    #del (sky_bar)
    #del (pinkbin_bar)
    #del (flying_object_bar)
    #del (stop_station)
    #del (user_ui)
    #del (button)
    #del (combo)
    #del (tile)
    #del (obstacle)

    del(RES.res.Game_ending)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            GameFramework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):   #게임종료씬에서 SPACE를 누를경우 랭킹스테이트로 넘어감
                    GameFramework.change_state(ranking_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                    close_canvas()


def update(frame_time):
    pass


def draw(frame_time):
    global font
    clear_canvas()

    RES.res.Game_ending.draw(750, 450)

    font = load_font('ENCR10B.TTF', 50)
    font.draw(100, 800, "ESC : Bye~~", (255, 0, 0))
    font.draw(100, 750, "SPACE : Ranking Page", (0, 0 , 255))

    update_canvas()


def pause():
    pass

def resume():
    pass


