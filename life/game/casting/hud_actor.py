from life.game.casting.actor import Actor


class HudActor(Actor):
    def __init__(self):
        super().__init__()
        self._state = False

    def update(self,state):
        self._state = state