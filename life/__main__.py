from life import constants
from life.game.casting.actor import Actor
from life.game.casting.cast import Cast
from life.game.casting.cell import Cell
from life.game.casting.global_state import GlobalState
from life.game.casting.grid import Grid
from life.game.casting.grid_hud import GridHUD
from life.game.casting.hud import HUD
from life.game.casting.paused_hud import PausedHUD
from life.game.directing.director import Director
from life.game.scripting.add_actors_action import AddActorsAction
from life.game.scripting.control_actors_action import ControlActorsAction
from life.game.scripting.draw_actors_action import DrawActorsAction
from life.game.scripting.move_actors_action import MoveActorsAction
from life.game.scripting.script import Script
from life.game.scripting.update_hud_action import UpdateHUDAction
from life.game.services.keyboard_service import KeyboardService
from life.game.services.mouse_service import MouseService
from life.game.services.video_service import VideoService
from life.game.shared.point import Point


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

    # cast.add_actor("players", Cycle(Point(third_width, half_height), constants.RED, 1))

    # p2_score = Score()
    # p2_score.set_position(Point(third_width * 2, 0))
    # cast.add_actor("scores", Score())
    # cast.add_actor("scores", p2_score)

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
