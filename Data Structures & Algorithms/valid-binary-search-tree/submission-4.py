# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def x(root, minV, maxV):
            if not root:
                return True
            if root.val > minV and root.val < maxV:
                return x(root.left, minV, root.val) and x(root.right, root.val, maxV)
            return False
        
        return x(root, float("-inf"), float("inf"))