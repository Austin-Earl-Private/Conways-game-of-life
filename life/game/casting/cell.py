from life import constants
from life.game.casting.actor import Actor
from life.game.shared.color import Color


class Cell(Actor):
    """
    Attributes:

    """

    def __init__(self):
        super().__init__()
        self.set_text("#")
        self.set_color(constants.WHITE)
        self._alive = True
        self.set_draw_square(True)


    def set_alive(self, state):
        """Sets the Cell to be alive or dead

            Args:
                state (bool)
            """
        if state:
            self.set_color(constants.WHITE)
        else:
            self.set_color(Color(0, 0, 0))
            # self.set_color(constants.RED)

        self._alive = state

    def is_alive(self):
        """Gets the Cell state of alive or dead


            """
        return self._alive
