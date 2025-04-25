from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from random import uniform

class Particle(Entity):
    def __init__(self, position):
        super().__init__(model="cube", color=color.red, position=position, scale=uniform(0.1 , 0.3))
        self.velocity=Vec3(uniform(-3,3), uniform(-3,3), uniform(-3,3))
        self.life_time=uniform(1,2)
        self.rotation=Vec3(uniform(-180,180), uniform(-180,180), uniform(-180,180))
    
    def update(self):
        self.position += self.velocity * time.dt      
        self.life_time -= time.dt
        if self.life_time <= 0:
            destroy(self)

if __name__ == "__main__":
    app=Ursina(borderless=False)
    ground= Entity(model="plane", scale=200, texture="grass")
    def input(key):
        if key == "space":
            for i in range(10):
                Particle(position=Vec3(0,5,0))
                


    EditorCamera()
    Sky()
    app.run()