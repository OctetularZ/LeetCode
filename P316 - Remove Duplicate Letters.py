class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        last_occurence = {s[i]: i for i in range(len(s))}

        for i in range(len(s)):
            if s[i] in visited:
                continue

            while stack and stack[-1][0] > s[i] and i < last_occurence[stack[-1][0]]:
                char, idx = stack.pop()
                visited.remove(char)

            stack.append([s[i], i])
            visited.add(s[i])

        res = [x[0] for x in stack]
        res = ''.join(res)
        return res

# Use hashmap to map the last occurence of every unique char
# Loop through string and add to a stack
# If the top of the stack is greater than the current char, and appears later, then pop if from stack
# Add current char onto stack
# Repeat until end of string is reached
