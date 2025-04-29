from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        i, j = 0, len(nums)-1 
        # 1 2 3 4 5 6 7 8

        while i < j:
            if nums_sorted[i] + nums_sorted[j] > target:
                j -= 1
            elif nums_sorted[i] + nums_sorted[j] < target:
                i += 1
            else:
                break

        res = []
        for index in range(len(nums)):
            if nums[index] == nums_sorted[i] or nums[index] == nums_sorted[j]:
                res.append(index)

        return res