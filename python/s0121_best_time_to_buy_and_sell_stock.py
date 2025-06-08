from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = prices[0]

        for n in prices:
            if n < buy:
                buy = n
            elif n - buy > res:
                res = n - buy

        return res
    

if __name__ == "__main__":
    sol = Solution()

    nums1 = [7,1,5,3,6,4]
    expected1 = 5
    assert sol.maxProfit(nums1) == expected1, f"Test1 Fail: got {sol.maxProfit(nums1)}"

    nums2 = [7,6,4,3,1]
    expected2 = 0
    assert sol.maxProfit(nums2) == expected2, f"Test2 Fail: got {sol.maxProfit(nums2)}"

    print("All tests passed!")