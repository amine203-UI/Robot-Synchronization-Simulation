import tkinter as tk
from tkinter import ttk
import threading


CELL_SIZE = 30
PADDING = 2


class SimulationGUI:
def __init__(self, grid, robots):
self.grid = grid
self.robots = robots
self.root = tk.Tk()
self.root.title('Robot Synchronization Simulation')


width = grid.cols * CELL_SIZE + 20
height = grid.rows * CELL_SIZE + 80
self.canvas = tk.Canvas(self.root, width=width, height=height)
self.canvas.pack()


# Button to end simulation
btn = ttk.Button(self.root, text='Quit', command=self._on_quit)
btn.pack(pady=6)


# Periodic screen update
self._running = True
self._update_interval_ms = 120


def _on_quit(self):
# Gracefully shut down robots
for r in self.robots:
r.alive = False
self._running = False
self.root.destroy()


def draw_grid(self):
self.canvas.delete('all')
for i in range(self.grid.rows):
for j in range(self.grid.cols):
x1 = j * CELL_SIZE + PADDING
y1 = i * CELL_SIZE + PADDING
x2 = x1 + CELL_SIZE - PADDING*2
y2 = y1 + CELL_SIZE - PADDING*2
self.canvas.create_rectangle(x1, y1, x2, y2, outline='black')


# Draw robots
for r in self.robots:
if r.alive:
x = r.y * CELL_SIZE + CELL_SIZE/2
y = r.x * CELL_SIZE + CELL_SIZE/2
# Draw a circle representing the robot
self.canvas.create_oval(x-10, y-10, x+10, y+10, fill='red')
self.canvas.create_text(x, y, text=str(r.robot_id), fill='white')


def _update(self):
if not self._running:
return
self.draw_grid()
self.root.mainloop()