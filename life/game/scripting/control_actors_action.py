from life.game.scripting.action import Action
from life.game.casting.global_state import GlobalState
from life.game.services.keyboard_service import KeyboardService


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service: KeyboardService):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        global_state:GlobalState = cast.get_first_actor("global")

        if self._keyboard_service.key_released('space'):
            global_state.toggle_pause()

        if self._keyboard_service.key_released('g'):
            global_state.toggle_grid()

