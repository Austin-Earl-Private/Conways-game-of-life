from life.game.casting.cast import Cast
from life.game.casting.grid import Grid
from life.game.scripting.action import Action
from life.game.services.mouse_service import MouseService


class AddActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, mouse_service:MouseService):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._mouse_service = mouse_service


    def execute(self, cast:Cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if self._mouse_service.is_key_down("m_l"):
            mouse_pos_grid = self._mouse_service.get_mouse_pos_snap_in_grid()
            grid:Grid = cast.get_first_actor("grid")
            cell = grid.get_entity_at(mouse_pos_grid)
            if not cell.is_alive():
                cell.set_alive(True)
        if self._mouse_service.is_key_down("m_r"):
            mouse_pos_grid = self._mouse_service.get_mouse_pos_snap_in_grid()
            grid: Grid = cast.get_first_actor("grid")
            cell = grid.get_entity_at(mouse_pos_grid)
            if cell.is_alive():
                cell.set_alive(False)

