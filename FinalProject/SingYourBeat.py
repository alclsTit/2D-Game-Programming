import GameFramework
import start_state
from pico2d import *
import RES

open_canvas(1500,900,sync=True)
hide_lattice()
RES.load_resource()
GameFramework.run(start_state)