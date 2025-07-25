from typing import List, Optional
from collections import Counter, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: Optional[TreeNode], mask: int) -> int:
        if not root:
            return 0
        
        mask = mask ^ (1 << root.val)
        if not root.left and not root.right:
            return 1 if mask & (mask - 1) == 0 else 0

        return self.dfs(root.left, mask) + self.dfs(root.right, mask)


    # def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    #     return self.countPseudoPalindrome(root, defaultdict(int))

    # def countPseudoPalindrome(self, root: Optional[TreeNode], count: dict[int]) -> int:
    #     if not root:
    #         return 0
        
    #     count[root.val] ^= 1
    #     if not root.left and not root.right:
    #         res = int(self.isPseudoPalindrome(count))
    #         count[root.val] ^= 1
    #         return res

    #     left = self.countPseudoPalindrome(root.left, count)
    #     right = self.countPseudoPalindrome(root.right, count)
    #     count[root.val] ^= 1

    #     return left + right

    # def isPseudoPalindrome(self, count: dict[int]) -> bool:
    #     res = 0

    #     for b in count.values():
    #         if res & b == 1:
    #             return False
    #         res = res | b
        
    #     return True