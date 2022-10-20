from life.game.casting.actor import Actor


class GlobalState(Actor):
    def __init__(self):
        super().__init__()
        self._pause = True
        self._show_grid = False

    def is_paused(self):
        return self._pause

    def toggle_pause(self):
        self._pause = not self._pause

    def is_grid(self):
        return self._show_grid

    def toggle_grid(self):
        self._show_grid = not self._show_grid
