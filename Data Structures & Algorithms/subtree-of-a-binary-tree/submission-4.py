# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, sub):
            if not root and not sub:
                return True
            elif root and sub and root.val == sub.val:
                left = isSame(root.left, sub.left)
                right = isSame(root.right, sub.right)
                return left and right
            return False

        if not root and not subRoot:
            return True
        elif not root:
            return False
        elif not subRoot:
            return True

        if isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)





