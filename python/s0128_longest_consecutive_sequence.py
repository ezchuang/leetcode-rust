from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        size = len(nums_set)
        res_len = 0

        while nums_set:
            target: int = nums_set.pop()

            # find next
            next_t: int = target + 1
            while next_t in nums_set:
                nums_set.remove(next_t)
                next_t += 1

            # find prev
            prev_t: int = target - 1
            while prev_t in nums_set:
                nums_set.remove(prev_t)
                prev_t -= 1

            res_len = max(next_t - prev_t - 1, res_len)

        return res_len
    

if __name__ == "__main__":
    sol = Solution()

    nums1 = [100,4,200,1,3,2]
    expected1 = 4
    assert sol.longestConsecutive(nums1) == expected1, f"Test1 Fail: got {sol.longestConsecutive(nums1)}"

    nums2 = [0,3,7,2,5,8,4,6,0,1]
    expected2 = 9
    assert sol.longestConsecutive(nums2) == expected2, f"Test2 Fail: got {sol.longestConsecutive(nums2)}"

    nums3 = [1,0,1,2]
    expected2 = 3
    assert sol.longestConsecutive(nums3) == expected2, f"Test3 Fail: got {sol.longestConsecutive(nums3)}"

    print("All tests passed!")