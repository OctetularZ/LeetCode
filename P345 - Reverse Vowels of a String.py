class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = ["a", "e", "i", "o", "u"]
        s = list(s)

        while left < right:
            if s[left].lower() not in vowels:
                left += 1
            elif s[right].lower() not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)


# Two pointers, one at the start, one at the end
# Keep going up on left pointer until a vowel is reached, repeat same for right side
# Then swap vowels
# Repeat until left and right meet
