from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from random import randint, choice
from game import Game

class Drops(Entity):
    def __init__(self, position):
        super().__init__() 
        self.model = choice(["cube" , "sphere"])
        self.scale = Vec3(0.3)
        self.color = color.random_color()
        self.position = position
        invoke(self.move, delay = 3)

    def move(self):
        if self:
            self.animate_position(Vec3(self.x, 0.5, self.z), duration= 3)
            destroy(self, delay=10)

    def update(self):
        if distance(self,Game.player) < 1:
            destroy(self)
            Game.hb.value += 10
            Game.player.health += 10