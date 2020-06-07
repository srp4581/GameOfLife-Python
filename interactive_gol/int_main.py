import pyglet
from pyglet.window import key, mouse, FPSDisplay

from interactive_gol.int_game_of_life import GameOfLife


class GOLWindow(pyglet.window.Window):

    def __init__(self):
        super(GOLWindow, self).__init__(600, 600)
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     10,
                                     0.4)

    def on_draw(self):
        print("ondraw")
        self.clear()
        self.gameOfLife.draw()

    def update(self, dt):
        print("update")
        self.gameOfLife.run_rules()


window = GOLWindow()
fps_display = FPSDisplay(window)
event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)


@window.event
def on_key_press(symbol, modifiers):
    # print("on_key_press")
    if symbol == key.ENTER:
        print('     The enter key was pressed.')
        # update (run the rules) repeatedly
        pyglet.clock.schedule_interval(window.update, 1.0 / 10.0)


@window.event
def on_mouse_press(x, y, button, modifiers):
    # print("on_mouse_press")
    if button == mouse.LEFT:
        print('     The left mouse button was pressed.')
        window.gameOfLife.create_cell(x, y)


@window.event
def on_draw():
    # print("on_draw")
    window.clear()
    fps_display.draw()


pyglet.app.run()
