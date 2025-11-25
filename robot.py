import threading
import random
import time


# Grid class (contains locks and locations)
class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [[None for _ in range(cols)] for _ in range(rows)]
        # Lock for each cell
        self.locks = [[threading.Lock() for _ in range(cols)] for _ in range(rows)]

    def try_occupy(self, x, y):
        """Try to occupy the cell if available. Returns True if success."""
        lock = self.locks[x][y]
        acquired = lock.acquire(blocking=False)
        if acquired:
            self.cells[x][y] = True
        return acquired

    def leave(self, x, y):
        self.cells[x][y] = None
        lock = self.locks[x][y]
        try:
            lock.release()
        except RuntimeError:
            pass

    def in_bounds(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols


class Robot(threading.Thread):
    DIRECTIONS = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1),
        (0, 0)
    ]

    def __init__(self, robot_id, grid: Grid):
        super().__init__()
        self.robot_id = robot_id
        self.grid = grid

        # Random initial position
        self.x = random.randint(0, grid.rows - 1)
        self.y = random.randint(0, grid.cols - 1)

        # Ensure the initial cell is free
        while not self.grid.try_occupy(self.x, self.y):
            self.x = random.randint(0, grid.rows - 1)
            self.y = random.randint(0, grid.cols - 1)

        self.alive = True
        self.max_moves = random.randint(20, 80)
        self.sleep_between_moves = (0.08, 0.5)

    def step(self):
        """Robot makes one move attempt."""
        # Release current cell
        self.grid.leave(self.x, self.y)

        dx, dy = random.choice(self.DIRECTIONS)
        new_x = self.x + dx
        new_y = self.y + dy

        if self.grid.in_bounds(new_x, new_y) and self.grid.try_occupy(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            # If move fails, re-occupy the original cell
            self.grid.try_occupy(self.x, self.y)

    def run(self):
        moves = 0
        while moves < self.max_moves and self.alive:
            self.step()
            moves += 1
            time.sleep(random.uniform(*self.sleep_between_moves))

        # Leaving the grid
        self.grid.leave(self.x, self.y)
