from ursina import *
from ursina.shaders import basic_lighting_shader as bls
from ursina.prefabs.first_person_controller import FirstPersonController
from enemy import Enemy 
from ground_enemy import GroundEnemy
from collectable import Collectable 
from game import Game
from gun import Gun
from portal import Portal
from platform_1 import Platform
from ursina.prefabs.health_bar import HealthBar
from particle_emitter import ParticleEmitter


Entity.default_shader = bls

app = Ursina(borderless=False)

psound = Audio("sounds/particle.wav", autoplay= False)

ground = Entity(model="plane", scale=100, texture="grass", collider="box")
player = FirstPersonController(health = 100, armor = 0)

Game.hb = HealthBar(bar_color = color.lime.tint(-.25), roundness= 0.5, max_value=100, value=100,x=0.3)
hb_icon = Entity(model="quad", parent=camera.ui, texture="health_core", scale=0.03, y=0.44, x=0.25)
Game.ab = HealthBar(bar_color = color.gray.tint(-.25), roundness= 0.5, max_value=100, value=0,x=0.3, y=0.5)
ab_icon = Entity(model="quad", parent=camera.ui, texture="shield", scale=0.03, y=0.485, x=0.25)



Game.player= player

enemies = []
for i in range(10):
    randomx = random.uniform(-30, 30)
    randomy = random.uniform(5, 10) 
    randomz = random.uniform(-30, 30)
    e = Enemy(pos=Vec3(randomx, randomy, randomz), psound=psound)
    enemies.append(e)

ground_enemies = []
for i in range(10):
    randomx = random.uniform(-30, 30)
    randomz = random.uniform(-30, 30)
    g_enemy = GroundEnemy(pos=Vec3(randomx, 0.5, randomz))
    ground_enemies.append(g_enemy)

collectable_list = []
for i in range(20):
    collectable = Collectable()
    collectable.relocate()
    collectable_list.append(collectable)

gun1=Gun(position=Vec3( 10, 0, 15), id=1)
gun2=Gun(position=Vec3( 15, 0, 10), id=2)

portal = Portal(player, pos=Vec3(10,1.5,10))

platform = Platform(player)

def update():
    for enemy in enemies:
        enemy.move(player)  
        enemy.collide(player)
        enemy.collide_bullet()

    for ground_enemy in ground_enemies:
        ground_enemy.move(player)
     
    for collectable in collectable_list:
        collectable.collision(player)

    
Sky()

app.enableParticles()

app.run()
