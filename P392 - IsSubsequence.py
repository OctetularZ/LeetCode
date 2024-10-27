def isSubsequence(s, t):
    t_pointer = 0
    s_pointer = 0
    final_string = ""
    while s_pointer < len(s) and t_pointer < len(t):
        if s[s_pointer] == t[t_pointer]:
            final_string += t[s_pointer]
            s_pointer += 1
            t_pointer += 1
        else:
            t_pointer += 1
    if s_pointer == len(s):
        return True
    else:
        return False


test_string_sub = "abc"
test_string = "ahbgdc"
print(isSubsequence(test_string_sub, test_string))
