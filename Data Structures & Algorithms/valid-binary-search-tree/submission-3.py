# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, l, h):
            if not node:
                return True
            if node.val <= l or node.val >= h:
                return False
            return is_valid(node.left, l, node.val) and is_valid(node.right, node.val, h)

        mn = float("-inf")
        mx = float("inf")

        return is_valid(root, mn, mx)