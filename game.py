from ursina import *
from ursina.shaders import basic_lighting_shader as bls

class Game:
    score = 0
    player=Entity()

    hb = Entity() #hb = health bar
    ab = Entity() #ab = armor bar