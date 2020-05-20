import pyglet
from pyglet.window import mouse, key

from game_of_life import GameOfLife


class Window(pyglet.window.Window):

    def __init__(self):
        print('init')
        super(Window, self).__init__(600, 600)
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     10,
                                     0.3)
        self.running_life = False
        pyglet.clock.schedule_interval(self.update, 1.0/24.0)

    def on_draw(self):
        print('on_draw')
        # self.clear()
        if self.running_life:
            self.gameOfLife.draw()
        else:
            pass

    def update(self, dt):
        print('update')
        self.gameOfLife.run_rules()


if __name__ == '__main__':
    print('main')
    window = Window()


    @window.event
    def on_mouse_press(x, y, button, modifiers):
        print('on_mouse_press')
        if button == mouse.LEFT:
            window.gameOfLife.create_cell(x, y)

    @window.event
    def on_key_press(symbol, modifiers):
        print('on_key_press')
        if symbol == key.SPACE:
            if window.running_life:
                window.running_life = False
            else:
                window.running_life = True


    pyglet.app.run()
