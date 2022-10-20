from game.casting.global_state import GlobalState
from game.casting.hud import HUD
from game.scripting.action import Action


class UpdateHUDAction(Action):

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        global_state:GlobalState = cast.get_first_actor("global")
        hud: HUD = cast.get_first_actor("hud")
        hud.get_first_hud("pause").update(global_state.is_paused())
        hud.get_first_hud("grid").update(global_state.is_grid())


