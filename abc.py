from random import shuffle

# Generate a random maze
def generate_maze(width, height):
  # Initialize the grid with all walls intact
  grid = [[1 for j in range(width)] for i in range(height)]
  
  # Use depth-first search to visit each cell and "carve" a path
  def dfs(x, y):
    # Mark the current cell as visited
    grid[x][y] = 0
    
    # Shuffle the list of directions to visit the cells in a random order
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    shuffle(directions)
    
    # Visit each of the unvisited cells
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < height and 0 <= ny < width and grid[nx][ny] == 1:
        dfs(nx, ny)
  
  # Start from a random cell
  start_x = randint(0, height - 1)
  start_y = randint(0, width - 1)
  dfs(start_x, start_y)
  
  return grid

# Solve the maze using breadth-first search
def solve_maze(maze):
  # Initialize the queue with the start cell
  start = (0, 0)
  queue = [start]
  
  # Keep track of the cells that have been visited
  visited = set()
  
  # Loop until the queue is empty
  while queue:
    # Get the next cell to visit
    x, y = queue.pop(0)
    
    # Mark the cell as visited
    visited.add((x, y))
    
    # Check if the cell is the end cell
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
      return visited
    
    # Add the unvisited neighbors to the queue
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
      nx, ny = x + dx, y + dy
      if 0 <= nx < len(maze) and 0 <= ny < len


