class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        substring = {}
        longest_string = 0
        
        for end in range(len(s)):
            substring[s[end]] = substring.get(s[end], 0) + 1
            while substring[s[end]] > 1:
                substring[s[start]] -= 1
                start += 1
            
            longest_string = max(longest_string, end - start + 1)
        
        return longest_string


# Lessons learnt, Using count to store each value is optimal.
# Adding a duplicate to a dictionary doesn't add another key with a different value, it UPDATES the exisiting key.
# This was an annoying concept which had me stuck for absolutely no reason. This is also why using count is better as this isnt a problem.
# Removing all instances will not allow start += 1, the window to be converged as much as needed. 
# It was actually only allow the window to converge once as all instances can be removed 'once'. Messing up the whole algorithm.

