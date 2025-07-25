from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        total = 0
        start, prev = 0, 0
        
        for curr in range(1, len(nums)):
            if nums[prev] == nums[curr]:
                total += self.getCount(curr - start)
                start = curr
            prev = curr

        total += self.getCount(len(nums) - start)
        return total

    def getCount(self, n):
        return (n + 1) * n // 2
    

if __name__ == "__main__":
    sol = Solution()

    # Test case 1: 完全交錯
    nums1 = [0, 1, 0, 1]
    # 4 + 3 + 2 + 1 = 10
    expected1 = 10
    assert sol.countAlternatingSubarrays(nums1) == expected1, f"Test1 Fail: got {sol.countAlternatingSubarrays(nums1)}"

    # Test case 2: 都一樣
    nums2 = [1, 1, 1, 1]
    # 每一個長度都是1 => 4
    expected2 = 4
    assert sol.countAlternatingSubarrays(nums2) == expected2, f"Test2 Fail: got {sol.countAlternatingSubarrays(nums2)}"

    # Test case 3: 有長有短
    nums3 = [0, 1, 1, 1]
    expected3 = 5
    assert sol.countAlternatingSubarrays(nums3) == expected3, f"Test3 Fail: got {sol.countAlternatingSubarrays(nums3)}"

    # Test case 4: 單一元素
    nums4 = [0]
    expected4 = 1
    assert sol.countAlternatingSubarrays(nums4) == expected4, f"Test4 Fail: got {sol.countAlternatingSubarrays(nums4)}"

    # Test case 5: 空陣列
    nums5 = []
    expected5 = 0
    assert sol.countAlternatingSubarrays(nums5) == expected5, f"Test5 Fail: got {sol.countAlternatingSubarrays(nums5)}"

    # Test case 6: 交錯起頭但馬上斷
    nums6 = [0, 0, 1]
    #  ,   但只有 ,  ,  ,  , 共4
    expected6 = 4
    assert sol.countAlternatingSubarrays(nums6) == expected6, f"Test6 Fail: got {sol.countAlternatingSubarrays(nums6)}"

    print("All tests passed!")