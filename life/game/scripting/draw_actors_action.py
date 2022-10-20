from game.casting.global_state import GlobalState
from game.casting.hud import HUD
from game.scripting.action import Action
import constants
from game.casting.cast import Cast
from game.services.video_service import VideoService
from game.shared.point import Point


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service:VideoService):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast:Cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        grid = cast.get_first_actor("grid")
        hud:HUD = cast.get_first_actor("hud")
        global_state: GlobalState =cast.get_first_actor("global")
        self._video_service.clear_buffer()
        self._video_service.draw_actors(grid.get_all_entities())
        self._video_service.draw_actors(hud.get_all_huds())
        if global_state.is_grid():
            self._video_service.draw_grid()
        self._video_service.draw_line(Point(0,constants.ROWS*constants.CELL_SIZE),Point(constants.MAX_X,constants.ROWS*constants.CELL_SIZE),constants.WHITE)
        self._video_service.flush_buffer()
