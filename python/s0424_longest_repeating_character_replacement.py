from collections import defaultdict

class Solution:
    # inspired by others
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = defaultdict(int)
        res = 0
        l, max_count = 0, 0

        for r in range(len(s)):
            right = s[r]
            char_dict[right] += 1
            max_count = max(max_count, char_dict[right])

            if r - l + 1 - max_count > k:
                left = s[l]
                char_dict[left] -= 1
                res = max(res, r - l)
                l += 1

        return max(res, r - l + 1)
    
if __name__ == "__main__":
    sol = Solution()

    input1 = "ABAB"
    input_k1 = 2
    expected1 = 4
    assert sol.characterReplacement(input1, input_k1) == expected1, f"Test1 Fail: got {sol.characterReplacement(input1, input_k1)}"

    input2 = "AABABBA"
    input_k2 = 1
    expected2 = 4
    assert sol.characterReplacement(input2, input_k2) == expected1, f"Test1 Fail: got {sol.characterReplacement(input2, input_k2)}"

    input3 = "ABBB"
    input_k3 = 1
    expected3 = 4
    assert sol.characterReplacement(input3, input_k3) == expected2, f"Test2 Fail: got {sol.characterReplacement(input3, input_k3)}"

    print("All tests passed!")