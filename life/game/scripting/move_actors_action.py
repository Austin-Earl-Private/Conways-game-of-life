from game.scripting.action import Action
from game.casting.cell import Cell
from typing import List

from game.casting.grid import Grid
from game.shared.point import Point


class MoveActorsAction(Action):
    def execute(self,cast,script):

        global_state = cast.get_first_actor("global")
        if not global_state.is_paused():
            grid: Grid = cast.get_first_actor("grid")
            cells: List[Cell] = grid.get_all_entities()
            cells_to_modify = []
            for cell in cells:
                grid_pos = cell.get_grid_position()
                cells_around = []
                for x in range(-1,2):
                    for y in range(-1,2):
                        if x==0 and y==0:
                            # ignore center, its us
                            continue
                        else:
                            cells_around.append(grid.get_entity_at(grid_pos.add(Point(x,y))))

                alive_cells = 0
                for found_cell in cells_around:
                    if(found_cell.is_alive()):
                        alive_cells +=1

                if alive_cells <2:
                    new_state = Cell()
                    new_state.set_alive(False)
                    cells_to_modify.append((cell.get_grid_position(),new_state))
                elif alive_cells>= 4 and cell.is_alive():
                    new_state = Cell()
                    new_state.set_alive(False)
                    cells_to_modify.append((cell.get_grid_position(), new_state))
                elif alive_cells == 3 and not cell.is_alive():
                    new_state = Cell()
                    new_state.set_alive(True)
                    cells_to_modify.append((cell.get_grid_position(), new_state))

            for set in cells_to_modify:
                grid.set_entity_at(set[0],set[1])

        # all_actors = cast.get_all_actors()
        # for actor in all_actors:
        #     actor.move_next()
        # players = cast.get_actors("players")
        # for player in players:
        #     player.grow_tail(1)

