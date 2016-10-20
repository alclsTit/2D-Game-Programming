from pico2d import *

open_canvas(1500, 900)

class CBack:
    def __init__(self):
        self.x , self.y = 0, 800
        self.image = load_image('FirstStage.png')

    #def Update(self):
    #    if(gChar.x > 1000):
    #        self.x += 50
    #    delay(0.5)

    def Draw(self):
        self.image.draw(self.x,self.y)

class CChar:
    def __init__(self):
        self.x ,self.y = 0 , 150
        self.image = load_image('run_animation.png')
        self.move_frame = 0

    def Update(self):
        self.move_frame = (self.move_frame + 1) % 8
        self.x += 50
        delay(0.5)

    def Draw(self):
        self.image.clip_draw(self.move_frame * 100, 0, 100, 100 , self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if(event.type == SDL_QUIT):
            running  = False
        elif(event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False

background = CBack()
character = CChar()

#background.Update()


running = True
while(running):
    handle_events()

    clear_canvas()

    character.Update()

    background.Draw()
    character.Draw()

    update_canvas()

close_canvas()