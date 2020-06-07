import pyglet

from tutorial_gol.game_of_life import GameOfLife


class Window(pyglet.window.Window):

    def __init__(self):
        super(Window, self).__init__(600, 600)
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     10,
                                     0.4)
        pyglet.clock.schedule_interval(self.update, 1.0/10.0)

    def on_draw(self):
        self.clear()
        self.gameOfLife.draw()

    def update(self, dt):
        self.gameOfLife.run_rules()


if __name__ == '__main__':
    print('main')
    window = Window()

    pyglet.app.run()
