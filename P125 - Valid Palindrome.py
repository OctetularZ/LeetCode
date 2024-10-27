def isPalindrome(s):
    stripped_string = s.replace(" ", "")
    lower_case_string = stripped_string.lower()
    while lower_case_string.isalnum() is False and lower_case_string != "":
        lower_case_string = "".join(char for char in lower_case_string if char.isalnum())
        print(lower_case_string)
    string_lst = list(lower_case_string)
    string_lst.reverse()
    reversed_string = str.join("", string_lst)
    if lower_case_string == reversed_string:
        return True
    else:
        return False


f = "."
print(isPalindrome(f))
