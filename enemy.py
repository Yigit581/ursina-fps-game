from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from bullet import Bullet
from game import Game
from partic import Particle
from random import randint as r
from particle_emitter import ParticleEmitter
from drops import Drops

Entity.default_shader = bls

class Enemy:
    def __init__(self, pos= Vec3(0), psound=None):
        self.entity = Entity(model="cube",position=pos, color=color.red)
        self.entity.look_at(Vec3(0))
        self.speed = random.uniform(1,10)
        self.startpos = pos
        self.psound = psound
    
    def move(self, player):
        self.entity.position += self.entity.forward * self.speed * time.dt
        if abs(self.entity.x) > 30 or abs(self.entity.y) < 1 or abs(self.entity.z) > 30:
            self.entity.position = self.startpos
            self.entity.look_at(player)
    
    def collide(self, player):
        if distance(self.entity,player) < 2:
            self.entity.position = Vec3(r(-30,30),r(5,10),r(-30,30))
            self.entity.look_at(Game.player)
            if player.armor > 0:                   
                Game.ab.value -= 10
                player.armor -= 10
            else:    
                Game.hb.value -= 10
                player.health -= 10

    def collide_bullet(self):
        for b in Bullet.bullets:
            if distance(self.entity, b ) < 1:
                self.entity.position = Vec3(r(-30,30),r(5,10),r(-30,30))
                self.entity.look_at(Game.player)
                ParticleEmitter(position=b.position)
                for i in range(10):
                    Particle(position= b.position)
                drop = Drops(position=b.position)