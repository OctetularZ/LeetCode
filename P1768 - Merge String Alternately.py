class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        if not word1 or not word2:
            return ""

        if not word1:
            return word1

        if not word2:
            return word1

        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            res += word1[i]
            res += word2[i]

        res += word1[min_length:]
        res += word2[min_length:]

        return res

# Can be done with two pointers too but I didn't see the need
