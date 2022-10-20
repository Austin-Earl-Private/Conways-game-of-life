from life.game.casting.hud_actor import HudActor


class PausedHUD(HudActor):
    def __init__(self):
        super().__init__()
        self._note = "(Push Space to pause and play the simulation) Left mouse click to add new cells | Right click to remove"

    def update(self, is_paused):
        if is_paused:
            self.set_text(f"Paused {self._note}")
        else:
            self.set_text(f"Running {self._note}")
