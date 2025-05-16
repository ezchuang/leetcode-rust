from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res_set = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res_set.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res_set
    

if __name__ == "__main__":
    sol = Solution()

    nums1 = [-1,0,1,2,-1,-4]
    expected1 = [[-1,-1,2],[-1,0,1]]
    assert sol.threeSum(nums1) == expected1, f"Test1 Fail: got {sol.threeSum(nums1)}"

    nums2 = [0,1,1]
    expected2 = []
    assert sol.threeSum(nums2) == expected2, f"Test2 Fail: got {sol.threeSum(nums2)}"

    nums3 = [0,0,0,0]
    expected2 = [[0,0,0]]
    assert sol.threeSum(nums3) == expected2, f"Test3 Fail: got {sol.threeSum(nums3)}"

    print("All tests passed!")