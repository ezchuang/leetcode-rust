from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            dig_sum = 0
            while n:
                n, r = divmod(n, 10)
                dig_sum += r
            if i == dig_sum:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()

    input1 = [0, 1, 2, 3, 4]
    expected1 = 0  # 0 的 digit sum 為 0，index 也是 0
    assert sol.smallestIndex(input1) == expected1, f"Test1 Fail: got {sol.smallestIndex(input1)}"

    input2 = [10, 11, 12, 13]
    expected2 = -1  # 無任何 index 與 digit sum 相符
    assert sol.smallestIndex(input2) == expected2, f"Test2 Fail: got {sol.smallestIndex(input2)}"

    input3 = [0, 10, 11, 12, 4]
    expected3 = 0  # index 0 = 0 → digit sum 0
    assert sol.smallestIndex(input3) == expected3, f"Test3 Fail: got {sol.smallestIndex(input3)}"

    input4 = [9, 18, 27, 36, 4]
    expected4 = 4  # 4 的 digit sum 為 4，index 也是 4
    assert sol.smallestIndex(input4) == expected4, f"Test4 Fail: got {sol.smallestIndex(input4)}"

    input5 = [1, 2, 3, 4, 5]
    expected5 = -1
    assert sol.smallestIndex(input5) == expected5, f"Test5 Fail: got {sol.smallestIndex(input5)}"

    print("All tests passed!")
