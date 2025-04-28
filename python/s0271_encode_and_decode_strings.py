from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return ""
        
        res = ""
        for s in strs:
            res += f"#{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) <= 0:
            return []

        res = []
        i = 0
        while i < len(s): # #2#45
            if s[i] != "#": # i = 0
                return []
            j = i + s[i + 1:].index("#") + 1 # j = 2
            length = int(s[i + 1: j]) # 2 = int([1:2])
            next_i = j + length + 1
            res.append(s[j + 1: next_i]) # 45 = s[2:5]
            i = next_i

        return res