# Backtracking

# - Backtracking algorithms use DFS to search all possible paths to a solution (like PathSum problem)
# - Key steps:
# - 1) - Backtracking
# -- Function first adds the value of leaf node to a "total" (can be string, array, number, etc), store other stuff if needed
# -- At leaf node, check if value has been reached (or on each iteration)
# -- If not, the function takes away from whatever variable you stored (if any), then backtracks to previous node in tree which still holds the total up to that node, then explores right child.
# - 2) - Pruning
# -- Functions checks if target has already been reached/surpassed
# -- If so, function takes away from variable immediately before returning to previous node as there's no reason to continue down that path.


def pathSum(root, target):
    def backtrack(node, path, total):
        if not node:
            return
        
        path.append(node.val)
        total += node.val

        # KEY STEP 2
        # current sum exceeds target
        # so pop to remove the current node from the path
        # return to backtrack to previous node on the call stack
        if total > target:
            path.pop()
            return
        
        if not node.left and not node.right:
            # add the path to the result
            # note we have to make a copy (path[:]) of the path
            # since future recursive calls modify path
            if total == target:
                result.append(path[:])
        else:
            backtrack(node.left, path, total)
            backtrack(node.right, path, total)

        # KEY STEP 1
        # we have finished exploring all paths containing the current node
        # so pop to remove the current node from the path
        # return to backtrack to previous node on the call stack.
        path.pop()

    result = []
    backtrack(root, [], 0)
    return result


# Solution Spaces Trees
# - In most backtracking problems, we will not be given an explicit tree to traverse.
# - Instead our algorithm, will need to construct the tree based on the problem.
# - To define our recursive function, we need to figure out what information we need to pass to each recursive call / node so that it can reach its neighbors.
# - This determines the parameters of our recursive function.

# Example - Phone number keyboard combinations
# - At the root node, we start with an emtpy string.
# - The children of the root node are "a", "b", and "c", which correspond to the digit 2.
# - So we can label the root node with 2 parameters, the empty string, and 0, which represents the index of the digit in the input phone number we are currently processing.

# - Next:
# - We can get "a", "b", "c" by iterating over the letters corresponding to our digit "2", and adding each letter to our current combination (which right now is the empty string).
# - For each of these letters, we make a recursive call with the updated combination and the next digit in the phone number.

def letterCombinations(digits):
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    } # Define phone number options

    def backtrack(path, idx): # Two variables, path - current combination, idx - index in number input
        if idx == len(digits): # Base case - If we've reached the end of the digit input combination
            result.append(path) # Add path combination to result array
            return

        for letter in phone[digits[idx]]: # Iterate through each possible letter from number
            backtrack(path + letter, idx + 1) # Recurse until length of input is reached, Add letter to path and 1 to index

    result = []
    if digits:
        backtrack("", 0) # Begin recursion with empty string and index 0
    return result

# Time complexity:
# - Branching Factor - Each digit maps to at most 4 letters
# - Depth of tree - This is n for this question
# Time - 4^n
