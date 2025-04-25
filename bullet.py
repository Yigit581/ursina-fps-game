from ursina import *
from ursina.shaders import basic_lighting_shader as bls


class Bullet(Entity):
    bullets = []
    def __init__(self, gun):
        super().__init__(parent = gun, model="cube", color=color.black, scale = 0.3, collider="box")
        Bullet.bullets.append(self)
        self.go()

    def go(self):
        self.world_parent = scene
        self.animate_position(self.position + self.forward * 50, duration= 1, curve=curve.linear)
        destroy(self, 3)
        invoke(self.remove_bullet, delay=3)

    def remove_bullet(self):
        Bullet.bullets.remove(self)