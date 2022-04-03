
import pyray
from player import Player
from background import Background

screenWidth = 800
screenHeight = 650


def run():
    # Main loop
    background = Background()
    player = Player()

    pyray.init_window(screenWidth, screenHeight)

    BACKGROUND = pyray.load_texture('path.png')
    CHARACTER = pyray.load_texture('boy.png')
    while not pyray.window_should_close():
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        background
        player
        pyray.end_drawing()

    # clean up
    pyray.close_window()


if __name__ == "__main__":
    run()
