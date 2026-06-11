from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = []

        def backtrack(path, current_digit):
            if len(path) == len(digits):
                res.append(path)
                return

            if len(path) > len(digits) or current_digit >= len(digits):
                return

            possible_letters = digit_map[digits[current_digit]]
            for letter in possible_letters:
                backtrack(path + letter, current_digit + 1)

        backtrack('', 0)
        return res

# Backtracking params - (path, current_digit)
# Base case - len(path) == len(digits) - add to result arr and return
# if len(path) > len(digits) - return
# for loop inside through each possible number in current digit - backtrack to match with next digit possibility
