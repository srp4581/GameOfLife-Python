import pyglet
from game_of_life import GameOfLife


class Window(pyglet.window.Window):

    def __init__(self):
        super(Window, self).__init__(600, 600)
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     5)

    def on_draw(self):
        self.clear()
        self.gameOfLife.draw()


if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
