from pico2d import *
import PCharacter

global run_state
run_state = True

class Input:
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                run_state = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                run_state = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
                jump_state = True
                jump_cnt = 0