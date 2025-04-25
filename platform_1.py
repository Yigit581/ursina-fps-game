from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from game import Game
from partic import Particle


Entity.default_shader = bls

class Platform():
    def __init__(self, player, num_platform=10, num_moving=5, num_falling=3, num_flying=5, num_rotating=4, num_particle = 3):
        self.player=player
        self.number_platform = num_platform
        self.number_moving = num_moving
        self.number_falling = num_falling
        self.number_flying = num_flying
        self.number_rotating = num_rotating
        self.number_particle = num_particle


        # for i in range(self.number_platform):
        #     x=random.uniform(-40,40)
        #     y=random.uniform(2,10)
        #     z=random.uniform(-40,40)
        #     Basic_Platform(self.player, pos=Vec3(x,y,z))

        # for i in range(self.number_moving):
        #     x=random.uniform(-40,40)
        #     y=random.uniform(2,10)
        #     z=random.uniform(-40,40)
        #     Moving_Platform(self.player, pos=Vec3(x,y,z))

        # for i in range(self.number_falling):
        #     x=random.uniform(-40,40)
        #     y=random.uniform(2,10)
        #     z=random.uniform(-40,40)
        #     Falling_Platform(self.player, pos=Vec3(x,y,z))

        # for i in range(self.number_flying):
        #     x=random.uniform(-40,40)
        #     y=random.uniform(2,10)
        #     z=random.uniform(-40,40)
        #     Flying(player=self.player, pos=Vec3(x,y,z), highlight_color=color.black)

        # for i in range(self.number_rotating):
        #     x=random.uniform(-40,40)
        #     y=random.uniform(2,10)
        #     z=random.uniform(-40,40)
        #     Rotating_Platform(player=self.player, pos=Vec3(x,y,z), highlight_color=color.gray)
        
        for i in range(self.number_particle):
            x=random.uniform(-40,40)
            y=random.uniform(2,10)
            z=random.uniform(-40,40)
            Particle_Platform(player=self.player, pos=Vec3(x,y,z), highlight_color=color.brown)        

    
class Basic_Platform(Button):
    def __init__(self, player, pos=Vec3(0)):
        super().__init__(parent=scene,model="cube", scale=Vec3(4,1,4), texture="brick", color=color.yellow)
        self.player=player
        self.position = pos

    def on_click(self):
        if distance(self, self.player) < 10:
            self.player.animate_position(self.position + Vec3(0,1,0), duration=3, curve=curve.linear)

class Moving_Platform(Button):
    def __init__(self, player, pos=Vec3(0)):
        super().__init__(parent=scene,model="cube", scale=Vec3(4,1,4), texture="brick", color=color.green)
        self.player=player
        self.position = pos
        self.player_on = False


    def on_click(self):
        if distance(self, self.player) < 10:
            self.player.animate_position(self.position + Vec3(0,1,0), duration=3, curve=curve.linear)
            invoke(self.move, delay = 3)

    def move(self):
        self.player_on = True
        randomx = random.randint(-40,40)
        randomz = random.randint(-40,40)
        self.animate_position(Vec3(randomx, self.y, randomz), duration=5, curve=curve.linear)
        invoke(self.make_false, delay=5)

    def update(self):
        if self.player_on:
            self.player.position = self.position + Vec3(0,1,0)
     
    def make_false(self):
        self.player_on = False

class Falling_Platform(Button):
    def __init__(self, player, pos=Vec3(0), **kwargs):
        super().__init__(parent=scene,model="cube", scale=Vec3(4,1,4), texture="brick", color=color.blue, **kwargs)
        self.player=player
        self.position = pos
        self.player_on = False
        self.start_pos = pos

    def on_click(self):
        if distance(self, self.player) < 10:
            self.player.animate_position(self.position + Vec3(0,1,0), duration=3, curve=curve.linear)
            invoke(self.move, delay = 3)

    def move(self):
        self.player_on = True
        self.animate_position(Vec3(self.x, 0, self.z), duration=3, curve=curve.linear)
        invoke(self.make_false, delay=3)
    
    def update(self):
        if self.player_on:
            self.player.position = self.position + Vec3(0,1,0)

    def make_false(self):
        self.player_on = False
        self.animate_position(self.start_pos, duration=3, curve=curve.linear)

class Flying(Falling_Platform):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color=color.black

    def move(self):
        self.player_on = True
        self.animate_position(Vec3(self.x, self.y + 10, self.z), duration=3, curve=curve.linear)
        invoke(self.make_false, delay=3)

class Rotating_Platform(Flying):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color=color.gray

    def move(self):
        self.player_on = True
        self.animate_rotation(Vec3(self.rotation_x, self.rotation_y + 360, self.rotation_z), duration=3, curve=curve.linear)
        invoke(self.make_false, delay=3)

    def update(self):
        if self.player_on:
            self.player.position = self.position + Vec3(0,1,0)
            self.player.rotation = self.rotation  
    
class Particle_Platform(Flying):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color=color.brown

    def move(self):
        self.player_on = True
        invoke(self.make_false, delay=1)    
    
    def update(self):
        if self.player_on:
            self.player.position = self.position + Vec3(0,1,0)

    def make_false(self):
        self.player_on = False
        self.explode()
        self.position = Vec3(random.randint(-45,45),2,random.randint(-45,45))

    def explode(self):
        for i in range(20):
            Particle(position= self.position)