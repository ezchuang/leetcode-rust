from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        res = False

        for n in nums:
            if n not in num_set:
                num_set.add(n)
            else:
                res = True
                break

        return res