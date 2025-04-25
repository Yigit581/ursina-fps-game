from ursina import *
from ursina.shaders import basic_lighting_shader as bls

Entity.default_shader = bls

class Portal(Entity):
    def __init__(self, player, pos): #def = metot
        super().__init__(model="sphere", position=pos, scale=Vec3(1, 3, 0.5), texture="portal")
        self.player = player
        self.billboard = True
    def jump_to(self):
        rx =random.randint(-30,30)
        ry =random.randint(1,2)
        rz =random.randint(-30,30)
        self.player.animate_position(Vec3(rx,ry,rz), duration=3, curve=curve.linear)

    def update(self):
        if distance_xz(self, self.player) < 2:
            self.jump_to()
