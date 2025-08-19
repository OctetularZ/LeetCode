from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        basket = {}
        max_fruits = 0

        for end in range(len(fruits)):
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                start += 1

            max_fruits = max(max_fruits, end - start + 1)
        
        return max_fruits


# Sliding window, Use two pointers for window
# basket - Hold fruits visited
# Loop through array to get end/to increase window size
# Add fruit to basket
# While there are more than two types of fruits in basket, Keep taking away left most fruit until it equals 0, then remove fruit from basket, converge window by 1 (start += 1)
# update maximum number of fruits
