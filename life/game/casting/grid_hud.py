from life.game.casting.actor import Actor
from life.game.casting.hud_actor import HudActor


class GridHUD(HudActor):
    def __init__(self):
        super().__init__()
        self._note = "(Push G to show or hide the grid)"

    def update(self, is_shown):
        if is_shown:
            self.set_text(f"Grid Hidden {self._note}")
        else:
            self.set_text(f"Grid Shown {self._note}")
