from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, [float("-inf"), float("inf")])

    def dfs(self, root: Optional[TreeNode], boundary: List[int]) -> bool:
        if not root:
            return True

        if root.left and (root.left.val >= root.val or root.left.val <= boundary[0]):
            return False
        if root.right and (root.right.val <= root.val or root.right.val >= boundary[1]):
            return False

        return self.dfs(root.left, [boundary[0], root.val]) and self.dfs(root.right, [root.val, boundary[1]])