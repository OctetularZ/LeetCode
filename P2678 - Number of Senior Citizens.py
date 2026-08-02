from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0

        for citizen in details:
            age = int(citizen[11:13])
            if age > 60:
                counter += 1
        
        return counter
