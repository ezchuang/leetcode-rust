from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            max_area = max(
                max_area, 
                min(height[l], height[r]) * (r - l)
            )

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area
    

if __name__ == "__main__":
    sol = Solution()

    height1 = [1,8,6,2,5,4,8,3,7]
    expected1 = 49
    assert sol.maxArea(height1) == expected1, f"Test1 Fail: got {sol.maxArea(height1)}"

    height2 = [1,1]
    expected2 = 1
    assert sol.maxArea(height2) == expected2, f"Test2 Fail: got {sol.maxArea(height2)}"

    print("All tests passed!")