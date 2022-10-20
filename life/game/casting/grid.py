from typing import List

from life import constants
from life.game.casting.actor import Actor
from life.game.casting.cell import Cell
from life.game.shared.point import Point


def _get_grid_pos_from_point(point)->str:
    """Gets string rep of point for grid
        Args:
            point (Point)
            """
    return f"{point.get_x()}_{point.get_y()}"


def _get_render_pos_from_grid_point(grid_point):
    """Converts grid cells into the rendering position for the render

        Args:
            grid_point (Point): point on the grid

    """
    return grid_point.scale(constants.CELL_SIZE)


def _wrap_point(point):
    """Wraps the point around the grid if you request a point outside of the grid supports negitive numbers
        up to -1 * rows or -1 * columns
        Args:
            point (Point):
    """
    max_y = constants.ROWS
    max_x = constants.COLUMNS
    if point.get_x() >= 0:
        new_x = point.get_x() % max_x
    else:
        new_x = (max_x + point.get_x()) % max_x

    if point.get_y() >= 0:
        new_y = point.get_y() % max_y
    else:
        new_y = (max_y + point.get_y()) % max_y
    return Point(new_x, new_y)


class Grid(Actor):

    def __init__(self):
        super().__init__()
        self._grid = {}
        self._populate_grid()

    def get_all_entities_around_point(self, point) -> List[Cell]:
        cells_around = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    # ignore center, its us
                    continue
                else:
                    cells_around.append(self.get_entity_at(point.add(Point(x, y))))
        return cells_around

    def get_all_entities(self):
        results = []
        for key in self._grid.keys():
            # print(key, self._grid[key].get_position().get_x(),self._grid[key].get_position().get_y())
            if self._grid[key] is not None:
                results.append(self._grid[key])

        return results

    def get_entity_at(self, point) -> Cell:
        """Gets the entity at a given point if it exists

            Args:
                point (Point): The given point.
            """
        point = _wrap_point(point)
        return self._grid[_get_grid_pos_from_point(point)]

    def set_entity_at(self, point, entity):
        """Set the entity at a given point, and updates its position for proper rendering

            Args:
                point (Point): The given point.
                entity (Actor): Actor to place
        """
        point = _wrap_point(point)
        entity.set_position(_get_render_pos_from_grid_point(point))
        entity.set_grid_position(point)
        self._grid[_get_grid_pos_from_point(point)] = entity


    def has_entity(self, point):
        """Checks to see if point exists and if it isn't empty

            Args:
                point (Point): The given point.

        """
        point = _wrap_point(point)
        return _get_grid_pos_from_point(point) in self._grid and self._grid[_get_grid_pos_from_point(point)] is not None

    def _populate_grid(self):
        for i in range(0, constants.ROWS):
            for k in range(0, constants.COLUMNS):
                print(k, i)
                cell = Cell()
                cell.set_alive(False)
                self.set_entity_at(Point(k, i), cell)
