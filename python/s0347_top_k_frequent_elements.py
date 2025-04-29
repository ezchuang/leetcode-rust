from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        count_dict = {}
        res = []

        for num in nums:
            if num not in num_count:
                num_count[num] = 0
            num_count[num] += 1

        sorted_num_arr_with_count = sorted(num_count.items(), key=lambda x: x[1], reverse=True)

        for arr_with_count in sorted_num_arr_with_count:
            if len(res) >= k:
                break
            res.append(arr_with_count[0])
        
        return res