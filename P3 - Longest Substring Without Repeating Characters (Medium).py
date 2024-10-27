def lengthOfLongestSubstring(s):
    if s == '':
        return 0
    elif len(s) == 1:
        return 1
    else:
        longest_string = ''
        longest_string_atm = ''
        previous_letters = ''
        current_index = 1
        while current_index != len(s):
            for letter in s:
                if letter not in previous_letters:
                    longest_string_atm += letter
                    previous_letters += letter
                else:
                    break
            if len(longest_string_atm) > len(longest_string):
                longest_string = longest_string_atm
                longest_string_atm = ''
            else:
                longest_string_atm = ''
            s = s[current_index:]
            previous_letters = ''

        return len(longest_string)


print(lengthOfLongestSubstring('abc'))
