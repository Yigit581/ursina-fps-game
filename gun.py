from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from game import Game
from bullet import Bullet

Entity.default_shader = bls

class Gun(Button):
    def __init__(self, position, id):
        super().__init__( 
        parent=scene,
        model="cube",
        color=color.azure,
        position=position,
        scale=Vec3(0.2, 0.2, 1),
        origin_y= -0.5
        )
        self.id=id
        self.player=Game.player
        self.on=False
        self.ground=True
    

    def get_gun(self):
        self.parent=camera
        self.position=Vec3(0.5, -0.5, 0.5)
        self.on=True
        self.ground=False

    def on_click(self):
        if distance_2d(self, self.player) < 5:
            self.get_gun()

    def input(self, key):
        if key == "left mouse down" and self.on and not self.ground:
            Bullet(self)
            self.blink(color.orange)
            invoke(self.change_color, delay=3)

    def change_color(self):
        self.color=color.random_color()
        
        
if __name__ == "__main__":
    from ursina.prefabs.first_person_controller import FirstPersonController
    app = Ursina(borderless=False)
    Sky()
    Game.player=FirstPersonController()
    gun1=Gun(position=Vec3( 10, 0, 15), id=1)
    gun2=Gun(position=Vec3( 15, 0, 10), id=2)  
    ground = Entity(model="plane", scale=100, texture="grass", collider="box")
    print("Gun modülü çalıştırıldı")
    app.run()
