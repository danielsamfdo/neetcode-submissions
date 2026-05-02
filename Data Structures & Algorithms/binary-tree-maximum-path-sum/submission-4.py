# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf');
        def ht(root):
            nonlocal res
            if root:
                lv = max(0, ht(root.left))
                rv = max(0, ht(root.right))
                res = max(res,  lv+rv+root.val)
                return max(lv, rv)+root.val
            return 0
        ht(root)
        return res