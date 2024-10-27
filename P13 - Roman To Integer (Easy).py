# Mine

class Solution(object):
    def romanToInt(self, s):
        previous_letter = None
        current_letter = None
        total = 0
        for letter in s:
            current_letter = letter
            if (previous_letter == 'I') and (current_letter == 'V' or current_letter == 'X'):
                total -= 2
            elif (previous_letter == 'X') and (current_letter == 'L' or current_letter == 'C'):
                total -= 20
            elif (previous_letter == 'C') and (current_letter == 'D' or current_letter == 'M'):
                total -= 200
            if current_letter == 'I':
                total += 1
            elif current_letter == 'V':
                total += 5
            elif current_letter == 'X':
                total += 10
            elif current_letter == 'L':
                total += 50
            elif current_letter == 'C':
                total += 100
            elif current_letter == 'D':
                total += 500
            elif current_letter == 'M':
                total += 1000
            previous_letter = letter
        return total


# Model answer
class ModelSolution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]
