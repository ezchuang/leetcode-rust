class Solution:
    def smallestString(self, s: str) -> str:
        changed = False
        s_list = list(s)
        for i in range(len(s_list)):
            if s_list[i] != "a":
                s_list[i] = chr(ord(s_list[i]) - 1)
                changed = True
            elif changed:
                break
                
        if not changed:
            s_list[-1] = "z"

        return "".join(s_list)
    
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: 單一字元，且為 'a'
    s1 = "a"
    expected1 = "z"
    assert sol.smallestString(s1) == expected1, f"Test1 Fail: got {sol.smallestString(s1)}"

    # Test case 2: 沒有 'a'
    s2 = "bc"
    expected2 = "ab"
    assert sol.smallestString(s2) == expected2, f"Test2 Fail: got {sol.smallestString(s2)}"

    # Test case 3: 有一段開頭不是 'a'，然後遇到 'a'
    s3 = "bacc"
    expected3 = "aacc"
    assert sol.smallestString(s3) == expected3, f"Test3 Fail: got {sol.smallestString(s3)}"

    # Test case 4: 開頭全都是 'a'
    s4 = "aaa"
    expected4 = "aaz"
    assert sol.smallestString(s4) == expected4, f"Test4 Fail: got {sol.smallestString(s4)}"

    # Test case 5: 只有一個字元，不是 'a'
    s5 = "c"
    expected5 = "b"
    assert sol.smallestString(s5) == expected5, f"Test5 Fail: got {sol.smallestString(s5)}"

    # Test case 6: 中間夾雜 'a'
    s6 = "abca"
    expected6 = "aaba"
    assert sol.smallestString(s6) == expected6, f"Test6 Fail: got {sol.smallestString(s6)}"

    print("All tests passed!")