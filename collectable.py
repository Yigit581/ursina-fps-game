from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from game import Game

Entity.default_shader = bls

class Collectable(Entity):
    def __init__(self, position=Vec3(0)):
        models = ["cube","coin","sphere"]
        super().__init__(model=random.choice(models), scale=Vec3(0.5, 0.5, 0.1), color=color.yellow)
        if random.randint(0,1) == 0:
            self.item = "score"
        else:
            self.item = "armor"
            self.color=color.black

    def relocate(self):
        self.position = Vec3(random.uniform(-50, 50), 1, random.uniform(-50, 50))

    def collision(self, player):
        if distance(self, player) < 2:
            print_on_screen(" + score")
            self.relocate()
            Game.score += 1
            print(Game.score)
            if self.item == "armor":
                Game.ab.value += 10
                Game.player.armor += 10