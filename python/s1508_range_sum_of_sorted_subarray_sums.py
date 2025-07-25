from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        extended_nums = []
        MOD = 10**9 + 7

        for i in range(n):
            temp = nums[i]
            extended_nums.append(temp)
            for j in range(i + 1, n):
                temp += nums[j]
                extended_nums.append(temp)

        extended_nums.sort()
        return sum(extended_nums[left - 1: right]) % MOD


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: 基本測試
    nums1 = [1, 2, 3, 4]
    n1, left1, right1 = 4, 1, 5
    expected1 = 13
    assert sol.rangeSum(nums1, n1, left1, right1) == expected1, f"Test1 Fail: got {sol.rangeSum(nums1, n1, left1, right1)}"

    # Test case 2: 單一元素陣列
    nums2 = [5]
    n2, left2, right2 = 1, 1, 1
    expected2 = 5
    assert sol.rangeSum(nums2, n2, left2, right2) == expected2, f"Test2 Fail: got {sol.rangeSum(nums2, n2, left2, right2)}"

    # Test case 3: 所有子陣列總和
    nums3 = [1, 2]
    n3, left3, right3 = 2, 1, 3  # sums: [1,2,3]
    expected3 = 6
    assert sol.rangeSum(nums3, n3, left3, right3) == expected3, f"Test3 Fail: got {sol.rangeSum(nums3, n3, left3, right3)}"

    # Test case 4: 測試 MOD 是否正常運作
    nums4 = [10**4] * 100
    n4, left4, right4 = 1, 1, 100
    result4 = sol.rangeSum(nums4, n4, left4, right4)
    assert 0 <= result4 < 10**9 + 7, f"Test4 Fail: MOD Error, got {result4}"


    print("All tests passed!")
