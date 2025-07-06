class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict and s_dict[s[i]] >= l:
                res = max(i-l, res)
                l = s_dict[s[i]] + 1 if s_dict[s[i]] > l else l + 1
            s_dict[s[i]] = i

        res = max(len(s)-l, res)

        return res
    
if __name__ == "__main__":
    sol = Solution()

    input1 = "abcabcbb"
    expected1 = 3
    assert sol.lengthOfLongestSubstring(input1) == expected1, f"Test1 Fail: got {sol.lengthOfLongestSubstring(input1)}"

    input2 = "bbbbb"
    expected2 = 1
    assert sol.lengthOfLongestSubstring(input2) == expected2, f"Test1 Fail: got {sol.lengthOfLongestSubstring(input2)}"

    input3 = "pwwkew"
    expected3 = 3
    assert sol.lengthOfLongestSubstring(input3) == expected3, f"Test2 Fail: got {sol.lengthOfLongestSubstring(input3)}"

    print("All tests passed!")