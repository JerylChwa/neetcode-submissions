# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(tree):
            nonlocal diameter
            if not tree:
                return 0
            left = dfs(tree.left)
            right = dfs(tree.right)
            diameter = max(diameter, left+right)

            return 1 + max(left, right)
        
        dfs(root)
        return diameter



        