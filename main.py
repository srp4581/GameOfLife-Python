import pyglet
from pyglet.window import mouse

from game_of_life import GameOfLife


class Window(pyglet.window.Window):

    def __init__(self):
        super(Window, self).__init__(600, 600)
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     10,
                                     0.5)
        pyglet.clock.schedule_interval(self.update, 1.0/24.0)

    def on_draw(self):
        self.clear()
        self.gameOfLife.draw()

    def update(self, dt):
        self.gameOfLife.run_rules()


if __name__ == '__main__':
    window = Window()


    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            print('x= ', window.gameOfLife.grid_height)
            print('y= ', window.gameOfLife.grid_width)
            print('coordinate', x, ', ', y)
            window.gameOfLife.create_cell(x, y)

    pyglet.app.run()
