from collections import defaultdict
from collections import deque
from collections import Counter

class Solution:
    def minWindow_ver2(self, s: str, t: str) -> str:
        """
        Method: Two-pointer
        Think: --, Inspired by NeetCode
        Write and debug: 5 min

        Time Complexity: O(n + m)
        Space complexity: O(m)
        """
        if len(s) < len(t) or len(t) <= 0:
            return ""
        
        t_count = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(t_count)
        res = [-1, -1]
        res_len = float("inf")
        l = 0
        
        for r, c in enumerate(s):
            window[c] += 1
            if c in t_count and window[c] == t_count[c]:
                have += 1

            # get the smallest substring by push the left index to the next
            while have == need:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        return s[res[0]: res[1] + 1] if res_len != float("inf") else ""


    def minWindow_ver1(self, s: str, t: str) -> str:
        """
        Method: Index-queue
        Think: 1hr
        Write and debug: 1 hr

        Time Complexity: O(n + m)
        Space complexity: O(m)
        """
        t_dict = defaultdict(int)
        s_dict = defaultdict(deque)
        l = -1
        res_string = ""

        # Count the required number of each character in t
        for c in t:
            t_dict[c] += 1

        for r in range(len(s)):
            right = s[r]
            if right not in t_dict:
                continue

            # Set the initial left pointer when we first find a relevant character
            if l == -1:
                l = r

            # Add the current index of the character to its list in s_dict
            s_dict[right].append(r)

            # If the number of occurrences exceeds the required amount in t_dict,
            # remove the oldest (leftmost) index of that character
            if len(s_dict[right]) > t_dict[right]:
                removed = s_dict[right].popleft()
                # If the removed index is not the current left pointer, no need to update window
                if removed != l:
                    continue

            # Check whether we have all required characters in sufficient quantities
            is_sub_String = all(len(s_dict[c]) >= nums for c, nums in t_dict.items())
            if not is_sub_String:
                continue
            
            # Update the left pointer to the smallest index among 
            # the leftmost positions of each character
            l = min(s_dict.values(), key=lambda value: value[0])[0]
            # Update the result if the current window is smaller than the previous one
            if r - l + 1 < len(res_string) or len(res_string) == 0:
                res_string = s[l: r + 1]

        return res_string
    
if __name__ == "__main__":
    sol = Solution()

    input_s1 = "ADOBECODEBANC"
    input_t1 = "ABC"
    expected1 = "BANC"
    assert sol.minWindow_ver2(input_s1, input_t1) == expected1, f"Test1 Fail: got {sol.minWindow_ver1(input_s1, input_t1)}"

    input_s2 = "a"
    input_t2 = "a"
    expected2 = "a"
    assert sol.minWindow_ver2(input_s2, input_t2) == expected2, f"Test1 Fail: got {sol.minWindow_ver1(input_s2, input_t2)}"

    input_s3 = "a"
    input_t3 = "aa"
    expected3 = ""
    assert sol.minWindow_ver2(input_s3, input_t3) == expected3, f"Test2 Fail: got {sol.minWindow_ver1(input_s3, input_t3)}"

    print("All tests passed!")