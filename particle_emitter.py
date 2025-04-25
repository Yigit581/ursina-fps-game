from ursina import *
from ursina.shaders import lit_with_shadows_shader as lit
from direct.particles.Particles import Particles
from direct.particles.ParticleEffect import ParticleEffect
from panda3d.core import Filename
from direct.particles.ForceGroup import ForceGroup
import time
 
class ParticleEmitter(Entity):
    
    def __init__(self, position=Vec3(0,0,0), file='particles/dust.ptf', life=1, deathtime=2, parent=None):
        super().__init__(position=position,shader=lit)
        self.stoptime = time.time() + life
        self.effect = ParticleEffect() 
        self.effect.loadConfig(file)
        self.life = life
        self.deathtime = deathtime
        if parent == None:
            self.effect.start(parent=self)
        else:
            self.effect.start(parent=parent)
        
        
    def update(self):
        if time.time() > self.stoptime:
            self.effect.soft_stop()
            invoke(self.die, delay=self.deathtime)     
        return
    
    def die(self):
        destroy(self)
        return

if __name__ == "__main__":
    from ursina import*

    app = Ursina(borderless=False)

    def input(key):
        if key == "space":
            ParticleEmitter()

    EditorCamera()

    Sky()

    app.enable_particles()

    app.run()


