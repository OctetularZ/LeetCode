class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        substring = {}
        max_freq = 0
        max_substring = 0

        for end in range(len(s)):
            substring[s[end]] = substring.get(s[end], 0) + 1
            max_freq = max(max_freq, substring[s[end]])

            if k + max_freq < end - start + 1:
                substring[s[start]] -= 1
                start += 1
            
            max_substring = max(max_substring, end - start + 1)

        return max_substring

# How this works:
# Substring is valid if the most frequent character + k is greater than or equal to the length of the substring.
