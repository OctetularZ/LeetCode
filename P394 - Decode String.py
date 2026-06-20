class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        int_stack = []
        current_str = ""
        current_numb = ""

        for i in range(len(s)):
            if s[i].isalpha():
                current_str += s[i]
            elif s[i].isnumeric():
                current_numb += s[i]
            elif s[i] == '[':
                str_stack.append(current_str)
                int_stack.append(int(current_numb))
                current_str = ""
                current_numb = ""
            elif s[i] == ']':
                temp = current_str
                current_str = str_stack.pop()
                number = int_stack.pop()
                current_str += temp * number

        return current_str

# [a]
# [2]
# bbb


# Stack - Only store letters and numbers
# Iterate though characters in s
# Global variable to keep track of result string
# Add each character to stack until close bracket is reached
# When close bracket is reached, add string to start of global variable
# When a number is reached, multiply global variable by number
# When end of s is reached, add any remaining letters to end of res
# Another variable to store current string we are building so we can add to stack
