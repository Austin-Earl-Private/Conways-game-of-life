import pyray

from life import constants
from life.constants import MAX_X, MAX_Y
from life.game.shared.point import Point


def _clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def _snap(value, size_of_snap):
    remainder = (value % size_of_snap)
    return int(value - remainder)


class MouseService:
    """Detects player input. 
    
    The responsibility of a MouseService is to indicate whether or not a mouse key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new MouseService."""
        self._keys = {
            'm_l': pyray.MouseButton.MOUSE_BUTTON_LEFT,
            'm_r': pyray.MouseButton.MOUSE_BUTTON_RIGHT}

    def clamp(self, n, smallest, largest):
        return _clamp(n, smallest, largest)

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key]
        return pyray.is_mouse_button_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d or i, j, k, l)
        """
        pyray_key = self._keys[key]
        return pyray.is_mouse_button_down(pyray_key)

    def get_mouse_pos_raw(self):
        return pyray.get_mouse_position()

    def get_mouse_pos_snap_in_grid(self):
        vec = self.get_mouse_pos_raw()
        x = _snap(vec.x, constants.CELL_SIZE)
        y = _snap(vec.y, constants.CELL_SIZE)
        cell_x = int(x / constants.CELL_SIZE)
        cell_y = int(y / constants.CELL_SIZE)
        return Point(cell_x, cell_y)
