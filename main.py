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
                                     0.5)
        pyglet.clock.schedule_interval(self.update, 1.0/10.0)

    def on_draw(self):
        print('on_draw')
        self.clear()
        self.gameOfLife.draw()

    def update(self, dt):
        # pass
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
            print('Space was pressed')
            window.gameOfLife.draw()


    pyglet.app.run()
