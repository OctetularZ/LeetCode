class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        l, r = 0, 0

        while l <= len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1

            if l == len(s):
                return True

            r += 1

        return False

# O(n) | where 'n' is the length of s (or t), solution - Loop through every letter in s and then every letter in t
# If the letter of s is available in t, then continue. If we reach the end of s, then we can return true
# Otherwise if we reach the end of t and we still haven't reached the end of s, then we can return False.

# Another solution is to use a hashmap storing key-value pairs of a character and its positions.
# This method will still be O(n) in respect to length of 's' as we still need to go through every letter
