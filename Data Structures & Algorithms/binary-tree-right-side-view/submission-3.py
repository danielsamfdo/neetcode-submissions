# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}
        def dfs(node, ht):
            nonlocal ans
            if not node:
                return
            if ht not in ans:
                ans[ht] = node.val

            if node.right:
                dfs(node.right, ht+1)
            if node.left:
                dfs(node.left, ht+1)
            
        dfs(root, 0)
        return [v for k,v in ans.items()]
