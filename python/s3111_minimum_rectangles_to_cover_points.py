from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        count = 0
        
        curr_right = -1
        for n in points:
            if n[0] <= curr_right:
                continue
            curr_right = n[0] + w
            count += 1
        
        return count


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: 簡單 3 點
    points1 = [[1, 2], [2, 3], [3, 1]]
    w1 = 1
    expected1 = 2
    assert sol.minRectanglesToCoverPoints(points1, w1) == expected1, f"Test1 Fail: got {sol.minRectanglesToCoverPoints(points1, w1)}"

    # Test case 2: 同 x 值、不同 y 值的點
    points2 = [[0, 1], [0, 2], [0, 3]]
    w2 = 0
    expected2 = 1
    assert sol.minRectanglesToCoverPoints(points2, w2) == expected2, f"Test2 Fail: got {sol.minRectanglesToCoverPoints(points2, w2)}"

    # Test case 3: points 間距大，無法共用 rectangle
    points3 = [[1, 2], [10, 2], [20, 2]]
    w3 = 5
    expected3 = 3
    assert sol.minRectanglesToCoverPoints(points3, w3) == expected3, f"Test3 Fail: got {sol.minRectanglesToCoverPoints(points3, w3)}"

    # Test case 4: 全部可用一個 rectangle 覆蓋
    points4 = [[0, 0], [1, 1], [2, 2]]
    w4 = 5
    expected4 = 1
    assert sol.minRectanglesToCoverPoints(points4, w4) == expected4, f"Test4 Fail: got {sol.minRectanglesToCoverPoints(points4, w4)}"

    # Test case 5: 空輸入
    points5 = []
    w5 = 2
    expected5 = 0
    assert sol.minRectanglesToCoverPoints(points5, w5) == expected5, f"Test5 Fail: got {sol.minRectanglesToCoverPoints(points5, w5)}"

    # Test case 6: 寬度為 0，點在不同 x 座標
    points6 = [[0, 0], [1, 0], [2, 0]]
    w6 = 0
    expected6 = 3
    assert sol.minRectanglesToCoverPoints(points6, w6) == expected6, f"Test6 Fail: got {sol.minRectanglesToCoverPoints(points6, w6)}"

    print("All tests passed!")
