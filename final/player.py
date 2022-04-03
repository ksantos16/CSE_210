import pyray


class Player:
    """
    A boy with backpack.

    The responsibility of Player is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """

    def __init__(self, texture='boy.png'):
        self._texture = pyray.load_texture(texture)
        self._width = 400
        self._height = 250

    def draw(self):

        pyray.draw_texture(self._texture, int(self._width/2 - self._texture.width/2),
                           int(self._height/2 - self._texture.height/2), pyray.RAYWHITE)
