
import random
import threading
import time
from gui import SimulationGUI
from robot import Robot, Grid


ROWS = 12
COLS = 16


def main():
grid = Grid(ROWS, COLS)


#The number of robots is random, between 4 and 10 (can be changed).
num_robots = random.randint(4, 8)


robots = []
for i in range(num_robots):
r = Robot(robot_id=i, grid=grid)
robots.append(r)


# Simulation GUI
gui = SimulationGUI(grid, robots)


# start robot threads
for r in robots:
r.start()


# start GUI loop (this will run in the main thread and update the display automatically)
gui.run()


# wait for robots to finish (GUI usually closes before this point or when all robots finish)
for r in robots:
r.join()


if __name__ == '__main__':
main()