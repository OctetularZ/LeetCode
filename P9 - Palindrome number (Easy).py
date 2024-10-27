class Solution(object):
    def isPalindrome(self, x):
        integer_str = str(x)
        integer_lst = []
        for integer in integer_str:
            integer_lst.append(integer)
        integer_lst.reverse()
        integer_str_rev = ''.join(integer_lst)
        if integer_str == integer_str_rev:
            return True
        else:
            return False
