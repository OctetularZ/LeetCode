# DFS in Matrices
# -- Another common way of representing a graph is a matrix (2D grid).
# -- Each cell in grid represents a node
# -- Each cell adjacent to the node, represents a neighbor. (Only the up, down, left, and right).
# -- i.e. grid[1][1] is a node. Its neighbors are grid[0][1], grid[2][1], grid[1][0], and grid[1][2]
# -- DFS on matrix is similar to DFS on an adjacency list. 
# -- We still have to keep track of visited nodes, and we recursively call DFS on each neighbor of the current node.
# -- The main difference is that each cell can have at most 4 neighbors (up, down, left, right), and that we need to check if the neighbor is within the bounds of the grid before visiting it.

def dfs(matrix):
  visited = set() # Contains visited nodes
  # up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Contains all possible directions from any cell

  def dfs_helper(r, c): # Takes row and column - node
    if (r, c) in visited: # If the node has already been visited, skip it
      return

    # Check if cell is out of bounds, if so skip it as well
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
      # Check if row is less than 0 or greater than length of matrix
      # Check if column is less than 0 or greater than length of subarray in matrix - all subarrays should be the same length so using the first one is fine.
      return

    visited.add((r, c)) # Add node to set of visited nodes
    for dr, dc in directions: # For each possible direction, in directions (up, down, left, right)
      dfs_helper(r + dr, c + dc) # Run a dfs on each neighbour
    return
  
    # This for loop happens for each neighbour, so it covers all possible nodes.

  dfs_helper(0, 0)


# BFS on Matrices
# - Choose starting node and add to queue 
# - While queue is not empty, removed from node from front of queue and add to visited
# - Add neighbours to queue if they haven't been visited and are within the boundaries
# - Repeat

def bfs(grid):
  visited = set()
  # up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  queue = [(0, 0)] # Initialise queue
  visited.add((0, 0)) # Add first node to visited

  while queue:
    row, col = queue.pop(0)

    # enqueue neighbors
    for dr, dc in directions:
      n_row = row + dr
      m_col = col + dc

      # Check if node is in bounds and if neighbor is visited or not
      if 0 <= n_row < len(grid) \
                and 0 <= m_col < len(grid[0]) \
                and (n_row, m_col) not in visited:
        queue.append((n_row, m_col))
        visited.add((n_row, m_col))

# - Level (in a graph) - Number of edges between root node and current node ("distance" between two nodes)
# For level by level - use for loop
# - Adjacency list level-by-level

from collections import deque

def bfs_levels(graph, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    levels = []

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # IMPORTANT
        # we have finished processing all nodes at the current level
        levels.append(current_level)

    return levels

# - Matrix level-by-level

from collections import deque

def bfs_level_by_level(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # start at the top-left corner
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    levels = []
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            row, col = queue.popleft()
            current_level.append((row, col))
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c))

        # IMPORTANT
        # we have finished processing all nodes at this level
        levels.append(current_level)

    return levels

# - BFS can be used to find the shortest path between two nodes in a graph
# - 
# - 
# - 