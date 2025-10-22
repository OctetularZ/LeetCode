# Depth-First Search

# Binary Tree
# - Root - The top node
# - Each node can have at most two children, Left Child and Right Child
# - Leaf - A node with no children
# - Height/Depth of binary tree - Maximum number of levels in the tree/Longest path from root node to leaf node (by edges) Also log(n)
# - Balanced binary tree - Where the height of the left and right subtree of each node differ by at most 1
# - Complete binary tree - A binary tree where every level, except potentially the last, is completely filled. And all nodes are as far left as possible. Like heaps. Height of O(log n)
# - Binary Search Tree - A binary tree where:
# -- All nodes in left subtree have a value less than the root
# -- All nodes in right subtree have a value greater than the root
# -- Same property applies to every subtree in the tree.
# -- This property allows for efficient search, insertion, and deletion of nodes in the tree.

# Depth First Search
# - Go deep as far as possible and then backtrack
# - At each node, check for left and right child
# - If left child, go left, otherwise go right
# - Keep going left till you can go left anymore, then checks for rights going up and repeat process on rights
# - Typically implemented as a recursive function

def dfs(node):
    # base case
    if not node:
        return

    dfs(node.left) # recursive call
    dfs(node.right) # recursive call

# - Call stack - Stack-like data structure which keeps track of the function calls that are currently being executed. How DFS backtracks.
# -- Call frame - Contains the current line of code being executed and the variables which are local to the function call
# -- Since there is a left node, we make a recursive call to the left node and this pushes a new call frame onto the call stack where node = left node.
# -- Execution begins at the first line of code in this new call frame

# - Base Case - where node is None

# - Backtracking
# -- When we reach our base case, we start going back.
# -- One our first base case hit, we return and the call frame is popped of the call stack.
# -- Then the execution returns to the call frame which is now on top of the call stack.
# -- After backtracking to the previous call frame, we make a call to the right node and the process repeats.
# -- Whenever a function returns, we have checked all nodes in the left and right subtree of that node

# Time complexity - O(N) (Each node is visited once)  (Or get work done on each recursive call and multiply by N)
# Space complexity - O(N) Each recursive call on the call stack is part of space complexity

# Example - Sum of all nodes in a tree
# - Sum of tree is the root node + the sum of the left and right subtrees
# - This applies to every subtree in the tree too

sum(node) = sum(node.left) + sum(node.right) + node.val

# - Solving recursively - Smaller subproblems to the same problem
# - Subtree returns it's value to it's parents which can the be used
# - Answer bubbles up to the root node, this is true for all problems solved usinf DFS
# - Base cases are problems we can solve without recursion:
# -- An empty subtree has a sum of 0
# -- The subtree rooted at a leaf node has a sum equal to the value of the leaf node (there is no left or right)

def dfs(node):
    # base case: empty subtree
    if node is None:
        return 0
    
    # base case: leaf node
    if node.left is None and node.right is None:
        return node.val
    
    left = dfs(node.left)
    right = dfs(node.right)
    return left + right + node.val

# - To determine what the return value should be for a different problem, imagine you're at a node in the tree and ask yourself: "What information do I need from my left and right subtrees to solve the problem for my subtree?"

# Example - Finding largest value in tree

def maxValue(node):
    if node is None:
        return float('-inf')
    
    if node.left is None and node.right is None:
        return node.val

    left = maxValue(node.left)
    right = maxValue(node.right)
    return max(left, right, node.val)

# - Common mistakes:
# -- Ensure the return types are the same in the base case and recursive cases
# -- Be able to clearly define what is being returned at each recursive call

# ------------

# Helper functions and global variables
# - Return values allow us to pass values from "bottom-up"
# - However sometimes we need to pass data from the "top-down"
# - We can use parameters of our recursive function to do this (like in P112 - Path Sum)
# - If we need more parameters than our original function signature allows, then we can use a helper function to help us recurse.

# - When working in DFS questions, always think of return value and base case first

# Good Node
def goodNodes(root):
  def dfs(root, max_):
    if root is None:
        return 0
    
    count = 0
    if root.val >= max_:
      count += 1
      max_ = root.val
    
    left = dfs(root.left, max_)
    right = dfs(root.right, max_)
    return left + right + count

  return dfs(root, -float("inf"))

# - Root-to-leaf problems commonly need a help function
# - We mainly need helper functions for when Leetcode confines main function signatures to only allow one parameter
# - We can also use global variables if we need to for example, get all good nodes from the tree

def goodNodes(root):
    nodes = [] # Not truly global, only available to goodNodes function
    def dfs(root, max_):
        nonlocal nodes # Gets the global nodes variable
        if root is None:
            return
        
        if root.val >= max_:
            max_ = root.val
            nodes.append(root) # Add good node to nodes list
        
        dfs(root.left, max_) # Not assigned to a variable as we're not returning anything
        dfs(root.right, max_)           

    dfs(root, -float('inf')) # We don't return anything we only append to nodes list
    return nodes

# - You can add arrays together with "+", this is new. I had no idea.
# - Global variables are also useful when the return values of each recursive function differs from what the question is asking.



# Types of DFS
# - Connected Components
# -- These types of problems use DFS to identify the number of connected nodes in a graph

# -- i.e. Finding the number of islands in a matrix where each "1" represents a cell of land:
# --- We traverse over each unvisited cell in the matrix (Double for loop with indexes - use range(len()) or enumerate).
# --- If the cell contains a 1, then we use DFS to traverse all land cells (cells with 1) neighboring that cell and every neighbor of that cell (marking cells as visited as we go (by storing index in a set)).
# --- When that completes, we have fully explored a single island, and we move onto the next island, which is the next unvisited cell in the matrix that contains a 1.

# - Boundary DFS
# -- These types of problems involve starting a DFS traversal from the boundary of a matrix.
# -- i.e. Finding all "1"s that are connected to the boundary of a matrix
