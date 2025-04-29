class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count_map = {} # {C: 1, D: 3} <- DCDD
        res = False

        if len(s) != len(t):
            return res

        for c in s:
            if c not in char_count_map:
                char_count_map[c] = 1
            else:
                char_count_map[c] += 1

        for c in t:
            if c not in char_count_map or char_count_map[c] == 0:
                return res
            else:
                char_count_map[c] -= 1

        res = True
        return res