from ursina import *
from ursina.prefabs.health_bar import HealthBar

if __name__ == '__main__':
    app = Ursina()

    health_bar_1 = HealthBar(bar_color=color.red.tint(-.25), roundness=.5, max_value=100, value=50)
    print(health_bar_1.text_entity.enabled, health_bar_1.text_entity.text)
    # health_bar_1.show_text = False
    # health_bar_1.show_lines = True

    def input(key):
        if key == '+' or key == '+ hold':
            health_bar_1.value += 10
        if key == '-' or key == '- hold':
            health_bar_1.value -= 10
            print('ow')
    app.run()
