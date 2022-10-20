import constants
from game.casting.cast import Cast
from game.casting.cell import Cell
from game.casting.global_state import GlobalState
from game.casting.grid import Grid
from game.casting.grid_hud import GridHUD
from game.casting.hud import HUD
from game.casting.paused_hud import PausedHUD
from game.directing.director import Director
from game.scripting.add_actors_action import AddActorsAction
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.script import Script
from game.scripting.update_hud_action import UpdateHUDAction
from game.services.keyboard_service import KeyboardService
from game.services.mouse_service import MouseService
from game.services.video_service import VideoService
from game.shared.point import Point


def main():
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    mouse_service = MouseService()

    # create the cast
    cast = Cast()
    cast.add_actor("global", GlobalState())
    grid = Grid()
    grid.set_entity_at(Point(4, 5), Cell())
    grid.set_entity_at(Point(5, 5), Cell())
    grid.set_entity_at(Point(6, 5), Cell())

    cast.add_actor("grid", grid)

    hud = HUD()

    paused_hud = PausedHUD()
    point = Point(10, constants.MAX_Y - constants.CELL_SIZE * 3)
    paused_hud.set_position(point)
    paused_hud.update(True)
    grid_hud = GridHUD()
    grid_hud.update(False)
    point = Point(10, constants.MAX_Y - constants.CELL_SIZE * 2)
    grid_hud.set_position(point)

    hud.add_hud("pause", paused_hud)
    hud.add_hud("grid", grid_hud)
    cast.add_actor("hud", hud)
    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", UpdateHUDAction())
    script.add_action("update", MoveActorsAction())
    script.add_action("update", AddActorsAction(mouse_service))
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
