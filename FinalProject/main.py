#import PCharacter

import PBackground
import PCharacter
import PTile
import PObstacle
import pygame
import time

from pico2d import *

#open_canvas(1500, 900)

#음악재생
pygame.mixer.init()
sound = pygame.mixer.Sound("Sound01.wav")


background = PBackground.Background()
character = PCharacter.Player()
obstacle = PObstacle.Obstacle()
# 초기화 부분

def handle_events():
    global running
    global jump_state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            PCharacter.Player.jump_state = True

running = True
state = 0

#PTile.Tile_List


show_lattice()

while(running):
   handle_events()

   # 업데이트 부분
   background.Update()
   character.Update()

   for PTile.Brick in PTile.List_tile:
       PTile.Brick.Update()

   for PObstacle.Obstacle in PObstacle.List_obstacle:
       PObstacle.Obstacle.Update()

   clear_canvas()
   #for PTile.Brick in var_steps:
   #    PTile.Brick.Update()

   # 렌더링 부분
   background.Draw()

   for PObstacle.Obstacle in PObstacle.List_obstacle:
       PObstacle.Obstacle.Draw()

   character.Draw()

   for PTile.Brick in PTile.List_tile:
       PTile.Brick.Draw()

   update_canvas()

   sound.play()

   delay(0.1)




#character = PCharacter.Player()
#brick = PTile.Brick()
#
#def main():
#
#    Objects = [brick for i in range(2)]
#
#    # 외부 입력부분
#    def handle_events():
#        global running
#        events = get_events()
#        for event in events:
#            if event.type == SDL_QUIT:
#                running = False
#            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#                running = False
#
#
#    running = True
#    while(running):
#       handle_events()
#
#       # 업데이트 부분
#       PCharacter.Update()
#
#       clear_canvas()
#
#       # 렌더링 부분
#       for PTile in Objects:
#           PTile.Draw()
#
#       PCharacter.Draw()
#
#       update_canvas()
#
#       delay(0.1)
#
#    close_canvas()
#
#if __name__ == '__main__':
#        main()