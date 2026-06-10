from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        res = []

        def backtrack(path, open_count, closed_count):
            if len(path) == n * 2 and open_count == closed_count:
                res.append(path)
                return

            if (open_count > n) or (closed_count > n):
                return

            if closed_count > open_count:
                return

            backtrack(path + '(', open_count + 1, closed_count)
            backtrack(path + ')', open_count, closed_count + 1)

        backtrack('(', 1, 0)
        return res

# Thought process:
# Backtracking
# Must start with open bracket
# Must end with close bracket
# Base case - If brackets == n * 2 and close brackets == open brackets
# Issue - We're not sure if brackets are actually valid or not?
# How do we ensure they are valid?
# If open brackets == n/2, then we can't have anymore open brackets, rest has to be closed. Vice versa for closed.
# If parenthesis is already valid and closed and open brackets are equal, then next bracket must be an open bracket.
# You can have n/2 many open brackets, but one condition for having valid parentheses everytime is: closed brackets can never be more than current open brackets.

# Solution:
# Start with open bracket
# Base case - If brackets == n * 2
# At each iteration, conditions to ensure valid parenthesis:
# Closed brackets cannot be more than open brackets, if so return
# Each backtrack has two option, open or closed bracket
# Prune - If open bracket or close bracket more than n/2