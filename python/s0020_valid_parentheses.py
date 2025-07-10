class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        p_stack = []

        for p in s:
            if p in p_dict:
                p_stack.append(p)
                continue
            if not p_stack:
                return False
            elif p != p_dict[p_stack.pop()]:
                return False
        
        return len(p_stack) == 0
    
if __name__ == "__main__":
    sol = Solution()

    input_s1 = "()"
    expected1 = True
    assert sol.isValid(input_s1) == expected1, f"Test1 Fail: got {sol.isValid(input_s1)}"

    input_s2 = "()[]{}"
    expected2 = True
    assert sol.isValid(input_s2) == expected2, f"Test2 Fail: got {sol.isValid(input_s2)}"

    input_s3 = "(]"
    expected3 = False
    assert sol.isValid(input_s3) == expected3, f"Test3 Fail: got {sol.isValid(input_s3)}"

    input_s4 = "([])"
    expected4 = True
    assert sol.isValid(input_s4) == expected4, f"Test4 Fail: got {sol.isValid(input_s4)}"

    print("All tests passed!") 