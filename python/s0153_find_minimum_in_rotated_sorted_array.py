from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r - l) // 2 + l
            if nums[m] < nums[r]:
                r = m
                continue
            l = m + 1

        return nums[l]
    

if __name__ == "__main__":
    sol = Solution()

    input_list1 = [3,4,5,1,2]
    expected1 = 1
    assert sol.findMin(input_list1) == expected1, f"Test1 Fail: got {sol.findMin(input_list1)}"

    input_list2 = [4,5,6,7,0,1,2]
    expected2 = 0
    assert sol.findMin(input_list2) == expected2, f"Test2 Fail: got {sol.findMin(input_list2)}"

    input_list3 = [11,13,15,17]
    expected3 = 11
    assert sol.findMin(input_list3) == expected3, f"Test3 Fail: got {sol.findMin(input_list3)}"

    print("All tests passed!")