from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from particle_emitter import ParticleEmitter
from particle import Particle

Entity.default_shader = bls

class GroundEnemy(Button):
    def __init__(self, pos=Vec3(0)):
        super().__init__(parent=scene, model="cube", color=color.blue, position=pos)
        self.start_pos=pos
        self.speed = random.uniform(5,10)

    def move(self, player):
        self.position += self.forward * self.speed * time.dt
        if abs(self.x) > 45 or abs(self.z) > 45:
            self.position = Vec3(random.randint(-50,50),self.y,random.randint(-50,50))
            self.look_at(Vec3(player.x, 0.5, player.y))
            

    def on_click(self):
        for i in range(10):
            Particle(position=self.position)
        ParticleEmitter(position=self.position, file='particles/dust_2.ptf')
        self.position = Vec3(random.randint(-50,50),self.y,random.randint(-50,50))
            