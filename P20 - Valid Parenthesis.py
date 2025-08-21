class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for bracket in s:
            if bracket not in bracket_dict:
                stack.append(bracket)
            else:
                if not stack or bracket_dict[bracket] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0     

# Add all close bracket corresponding brackets to open bracket to a dictionary
# Initialise stack
# Loop through brackets
# If bracket not in stacks keys, add to stack, otherwise, don't add to stack and pop from stack
# Return True is stack is empty
# Return False, if close bracket doensn't match bracket on stack
