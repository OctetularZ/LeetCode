class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_number = 0
        current_string = ""

        for char in s:
            if char == "[": # If start of new letters:
                stack.append(current_string) # Add current string to stack
                stack.append(current_number) # Add current number to stack
                current_string = "" # Reset both
                current_number = 0
            elif char == "]": # If end of sequence:
                num = stack.pop() # Get number from stack
                prev_string = stack.pop() # Get previous string from stack
                current_string = prev_string + (current_string * num) # Multiply current string by number and add string in stack to start
            elif char.isdigit():
                current_number = (current_number * 10) + int(char) # If digit, multiply current digit by 10 then add new digit to it
            else:
                current_string += char # If letter, add to end of current_string

        return current_string



# Store current string, start as ""
# Intialise stack, start as []
# Store current number, start as 0

# For each character in decoded string -
# If char = [, add current string to stack, add current number to stack, current number = 0, current string = ""
# If char = ], get current number, get current string (both from stack), multiply then add to start of current string (outside of stack - "total" string essentially)
# If char = number, current number = current number * 10 + new number
# If char = letter, current string = current string + character
