# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal = True
        def dfs(tree):
            nonlocal bal
            if not tree:
                return 0
            left = dfs(tree.left)
            right = dfs(tree.right)
            if abs(left-right) > 1:
                bal = False
                
            return 1 + max(left, right)
        dfs(root)
        return bal