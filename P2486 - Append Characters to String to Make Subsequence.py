class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if not t:
            return 0

        s_p, t_p = 0, 0

        while s_p < len(s) and t_p < len(t):
            if s[s_p] == t[t_p]:
                t_p += 1

            s_p += 1

        return len(t) - t_p
