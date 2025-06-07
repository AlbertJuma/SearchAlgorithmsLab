# SearchAlgorithmsLab

I tried to develop a Python project that visualizes mazes and demonstrates AI search methods like **BFS**, **DFS**, and **A\***.  
It uses `matplotlib` to display the maze and paths clearly, helping beginners understand pathfinding techniques.

## Features
- Maze visualization
- BFS, DFS, and A* algorithms
- Simple and educational layout

## Requirements
- Python 3
- matplotlib

## Run
```bash
py## 🗂️ Project Structure

thon maze_diagram.py
SearchAlgorithmsLab/
│
├── main.py                # Runs the project (with BFS/DFS logic)
├── README.md              # Explains how to use the project
│
├── algorithms/            # Holds individual algorithm files
│   ├── bfs.py             # BFS logic
│   ├── dfs.py             # DFS logic
│   └── astar.py           # A* logic (if added)
│
├── visualizations/        # Drawing & animation functions
│   └── maze_plot.py
│
├── data/                  # Optional: Saved or random maze files
│   └── maze1.json
│
└── requirements.txt       # Lists libraries like matplotlib, numpy
