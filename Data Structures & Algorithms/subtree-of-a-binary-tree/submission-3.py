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

        # both root and subroot empty
        if not root and not subRoot:
            return True
        # both root and subroot present
        elif root and subRoot and root.val == subRoot.val:
            # if value is the same, check the subtree on left and right whether they are identical
            # but still need to check if left and right of root is same val as subroot val
                if root.left and root.left.val == subRoot.val:
                    return isSame(root, subRoot) or self.isSubtree(root.left, subRoot)
                elif root.right and root.right.val == subRoot.val:
                    return isSame(root, subRoot) or self.isSubtree(root.right, subRoot)
                else:
                    return isSame(root, subRoot)

        else:
            if not root or not subRoot:
                return False
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)





