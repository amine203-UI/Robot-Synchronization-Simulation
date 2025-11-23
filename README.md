<h1 align="center">Robot Synchronization Simulation</h1>

## 🛍️ Overview

This project simulates the movement and synchronization of multiple robots inside a two-dimensional grid. Each robot is implemented as a separate thread and moves randomly from one cell to another. To prevent conflicts when multiple robots try to enter the same cell at the same time, the program uses semaphores (or locks) to ensure mutual exclusion. Each cell can only contain one robot at any moment.

The project also includes a graphical interface that displays the grid and updates in real time as robots move. Robots start at random positions, move for a random number of steps, and then exit the working area. The simulation demonstrates thread synchronization, shared resource protection, and safe concurrent programming in Python.

---
# Project Operation

1. Ensure Python 3.8+ is installed.

2. Create a virtual environment (recommended): 
```bash
python -m venv venv
source venv/bin/activate (Linux/Mac) 
venv\Scripts\activate (Windows)
```
3. Install requirements if applicable (no external packages are included by default):
```bash
 pip install -r requirements.txt
```
4. Run: 
```bash
python main.py
```
# Experiments and Test Scenarios
- Try changing the number of rows/columns in main.py to observe the effect of size.

- Try increasing the number of bots: This increases the chances of collisions and inability to enter (cells will remain protected).

- Try making the bots faster or slower by changing `sleep_between_moves`.

- Observe the behavior: Does it get deadlocked? (In the current version, the probability of a deadlock is low because the bot reserves a new cell without first reserving a series of cells.)

# Notes on Avoiding Deadlocks
- If you want to minimize the probability of a deadlock, you can use the following strategy:
1) Reserve cells in a specific order (e.g., by cell index) before moving.

2) Use try-acquire with a short waiting period and retry repeatedly.