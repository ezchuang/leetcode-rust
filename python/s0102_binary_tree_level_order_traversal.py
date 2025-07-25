from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.traversalByOrder(root, 0, res)
        return res
        
    def traversalByOrder(self, 
        root: Optional[TreeNode], 
        order: int, 
        res: List[List[int]]):
        if not root:
            return

        if len(res) <= order:
            res.append([])
        res[order].append(root.val)

        self.traversalByOrder(root.left, order + 1, res)
        self.traversalByOrder(root.right, order + 1, res)