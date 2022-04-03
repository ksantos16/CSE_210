import pyray


class Background:

    def __init__(self, texture='path.png'):
        self._texture = pyray.load_texture(texture)
        self._width = 800
        self._height = 650

    def draw(self):

        pyray.draw_texture(self._texture, int(self._width/2 - self._texture.width/2),
                           int(self._height/2 - self._texture.height/2), pyray.RAYWHITE)
