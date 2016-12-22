
import platform
import os

#코드로 환경변수 설정
if platform.architecture()[0] == '32bit':               #컴퓨터가 32비트이면 해당파일의 32비트SDL을 참조
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:                                                    #컴퓨터가 32비트이외이면 해당파일의 64비트SDL을 참조
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import GameFramework
import start_state
from pico2d import *
import RES

open_canvas(1500,900,sync=True)
hide_lattice()
RES.load_resource()
GameFramework.run(start_state)
close_canvas()