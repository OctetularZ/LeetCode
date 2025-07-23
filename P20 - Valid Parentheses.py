"""This method is kinda long-winded. The more efficient solution was to use a stack (which I got correct) but I also
had to use a dictionary too. It's funny because I actually did think of using a dictionary but tunnel vision is one
heck of a drug. I was using stack only, and I was getting closer and closer to the solution, so I just kept on going
and got the solution. Mine is 3ms but most optimal is 0ms. Both are O(n) though."""

# Lesson - Just trust your instincts next time or actual think about other approaches before zero-ing in on one.


def isValid(self, s: str) -> bool:
    n = len(s)

    if n == 0:
        return False
    if n == 1:
        return False

    open_brackets = ["(", "[", "{"]
    close_brackets = [")", "]", "}"]
    bracket_stack = []

    if s[0] in close_brackets:
        return False

    for i in range(n):
        if s[i] in open_brackets:
            bracket_stack.append(s[i])
        else:
            if (s[i] in close_brackets) and len(bracket_stack) == 0:
                return False
            last_open_bracket = bracket_stack.pop()
            if s[i] == ")" and last_open_bracket != "(":
                return False
            elif s[i] == "]" and last_open_bracket != "[":
                return False
            elif s[i] == "}" and last_open_bracket != "{":
                return False
    if len(bracket_stack) > 0:
        return False

    return True


# Optimal solution
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         mapping = {")": "(", "}": "{", "]": "["}
#
#         for char in s:
#             if char in mapping.values():
#                 stack.append(char)
#             elif char in mapping.keys():
#                 if not stack or mapping[char] != stack.pop():
#                     return False
#
#         return not stack
