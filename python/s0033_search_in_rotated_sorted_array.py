from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (r - l) // 2 + l

            if target == nums[r]:
                return r
            if nums[m] < nums[r]:
                if target <= nums[m] or target > nums[r]:
                    r = m
                    continue
                l = m + 1
                continue
            if target > nums[m] or target < nums[r]:
                l = m + 1
                continue
            r = m

        return r if nums[r] == target else -1
    
if __name__ == "__main__":
    sol = Solution()

    input_list1 = [4,5,6,7,0,1,2]
    target1 = 0
    expected1 = 4
    assert sol.search(input_list1, target1) == expected1, f"Test1 Fail: got {sol.search(input_list1, target1)}"

    input_list2 = [4,5,6,7,0,1,2]
    target2 = 3
    expected2 = -1
    assert sol.search(input_list2, target2) == expected2, f"Test2 Fail: got {sol.search(input_list2, target2)}"

    input_list3 = [1]
    target3 = 0
    expected3 = -1
    assert sol.search(input_list3, target3) == expected3, f"Test3 Fail: got {sol.search(input_list3, target3)}"

    print("All tests passed!")