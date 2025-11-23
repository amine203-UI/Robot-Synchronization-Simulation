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
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)]


def __init__(self, robot_id, grid: Grid):
super().__init__()
self.robot_id = robot_id
self.grid = grid
self.x = random.randint(0, grid.rows - 1)
self.y = random.randint(0, grid.cols - 1)
# Ensure the initial cell is occupied before starting
while not self.grid.try_occupy(self.x, self.y):
self.x = random.randint(0, grid.rows - 1)
self.y = random.randint(0, grid.cols - 1)


self.alive = True
self.max_moves = random.randint(20, 80)
self.sleep_between_moves = (0.08, 0.5)


def run(self):
moves = 0
while moves < self.max_moves and self.alive:
self.step()
moves += 1
time.sleep(random.uniform(*self.sleep_between_moves))


# Leaving: release the current cell
return