## Graphs

# - Graphs consist of nodes (a.k.a vertices) and edges that connect the nodes
# - Nodes connected by an edge are neighbours of each other (crucial part of graph traversal)
# - Graphs can contain cycles unlike trees. (Tree is a connected graph with no cycles) (Binary tree is the same but each node can only have at most 2 children)
# - A cycle is path that starts and ends at the same node
# - Connected graph - Where there is a path between every pair of nodes
# - Disconnected graph - Where there are at least two nodes that are not connected to each other via a path
# - Connected components - Nodes connected to each other
# - Directed graph - Edges between nodes only go 1 direction
# - Undirected - Edges between nodes go both directions (most common for interviews)


# Adjacency List
# - Common way of representing a graph
# - We are given a list of nodes (dict) where each node is mapped to a list of its neighbours. Below is python representation.

adjList = {    
        1: [2],    
        2: [1, 3, 4],    
        3: [2, 4],    
        4: [2, 3, 5],    
        5: [4]    
    }

# - Allows O(1) lookups


# DFS for graphs
# - Graphs are typically represented as an adjacency list or as a matrix
# - The most important thing to remember is to keep track of the visited nodes as you traverse, since graphs (unlike trees) can contain cycles.
# - DFS concept is the same, go as deep as possible then backtrack
# - Differences:
# -- Each node can have any amount of neighbors, so we need a for loop to iterate over each neighbor rather than making calls to the left and right children of the current node.
# -- Because graphs can contain cycles, we need to keep track of nodes we have already visited. If we encounter a node that has already been visited, we should return immediately without making any further recursive calls (or skip it in the loop altogether). Otherwise, we may end up in an infinite loop. 
# -- We don't need an explicit base case like we do in the trees. Eventually, we will visit all nodes in the graph, and the recursion will stop on its own (with the help of the visited set).

def dfs(adjList):
  if not adjList: # If adjacency list is empty, return (there are no nodes)
    return
  visited = set() # Where we store nodes we've already visited

  def dfs_helper(node):
    if node in visited: # If we've already visited the node, skip it
      return

    visited.add(node) # Add the current node to set of visited nodes so we don't use it again

    for neighbor in adjList[node]: # For each node's neighbour, run the dfs on the neighbour
      dfs_helper(neighbor)
    return

  # For loop handles disconnected components, otherwise we don't need it.
  # For example, if it was a tree, all nodes are connected. So we should be able to visit all nodes purely from neighbours of first node (or any node), as there should be a path to any node from a single node.
  for node in adjList:
    if node not in visited:
      dfs_helper(node)



# BFS for graphs
# - Stores a set of visited nodes too
# - BFS on adjacency list is pretty straight-forward
# - Start with node, visit node and add it's neighbours to queue if their not in visited already, then repeat

def bfs(start):
  visited = set([start]) # Initialise the set with the first node
  queue = [start] # Initialise queue

  while queue:
    node = queue.pop(0)
    for neighbor in adjList[node]: # Adds each neighbour the queue
      if neighbor not in visited: # Adds neighbour to queue if not visited. We initialise set with start first incase it has itself as a neighbour, we can say we already visited it. Avoids an infinite loop.
        visited.add(neighbor) # Add to visited set
        queue.append(neighbor) # Add neighbour to queue
