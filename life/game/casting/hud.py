from typing import List

from life.game.casting.actor import Actor
from life.game.casting.hud_actor import HudActor


class HUD(Actor):
    def __init__(self):
        super().__init__()
        self._hud = {}

    def add_hud(self, group, hud):
        if not group in self._hud.keys():
            self._hud[group] = []

        if not hud in self._hud[group]:
            self._hud[group].append(hud)

    def get_huds(self, group):
        results = []
        if group in self._hud.keys():
            results = self._hud[group].copy()
        return results

    def get_all_huds(self)->List[HudActor]:
        results = []
        for group in self._hud:
            results.extend(self._hud[group])
        return results

    def get_first_hud(self, group):
        result = None
        if group in self._hud.keys():
            result = self._hud[group][0]
        return result

    def remove_hud(self, group, hud):
        if group in self._hud:
            self._hud[group].remove(hud)
