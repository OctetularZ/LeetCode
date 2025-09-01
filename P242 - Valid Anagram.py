import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        s_d = collections.Counter(s)
        t_d = collections.Counter(t)

        return s_d == t_d
