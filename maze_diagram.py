import matplotlib.pyplot as plt
import numpy as np
from collections import deque

# Maze: 0 = path, 1 = wall
maze = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
]

maze = np.array(maze)
start = (0, 0)
end = (9, 9)

# BFS to find shortest path
def bfs(maze, start, end):
    rows, cols = maze.shape
    visited = set()
    queue = deque()
    queue.append((start, [start]))
    visited.add(start)
    
    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == end:
            return path
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))
    return None

shortest_path = bfs(maze, start, end)

# Fake longest-ish path by walking around (for visual)
longest_path = [
    (0,0), (1,0), (2,0), (2,1), (2,2), (3,2), (4,2), (4,1), (4,0),
    (5,0), (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (7,6),
    (8,6), (8,7), (8,8), (8,9), (9,9)
]

# Draw the maze with paths
def draw_maze(maze, start, end, shortest=None, longest=None):
    fig, ax = plt.subplots(figsize=(6,6))
    ax.imshow(maze, cmap='gray_r')

    ax.text(start[1], start[0], 'S', ha='center', va='center', color='green', fontsize=12)
    ax.text(end[1], end[0], 'E', ha='center', va='center', color='red', fontsize=12)

    if longest:
        x, y = zip(*[(c, r) for r, c in longest])
        ax.plot(x, y, color='orange', linestyle='--', linewidth=1.5, label='Longer Possible Path')

    if shortest:
        for (r, c) in shortest:
            if (r, c) != start and (r, c) != end:
                ax.add_patch(plt.Circle((c, r), 0.25, color='blue'))
        x, y = zip(*[(c, r) for r, c in shortest])
        ax.plot(x, y, color='blue', linewidth=2, label='Shortest Path (BFS)')

    ax.set_xticks([])
    ax.set_yticks([])
    plt.title("Maze Search: Shortest vs Longer Paths")
    plt.legend()
    plt.show()

draw_maze(maze, start, end, shortest_path, longest_path)
