# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root or subRoot:
            return False

        if subRoot.val == root.val:
            self.isSameTree(subRoot,root)
        else:
            self.isSubtree(root.right, subRoot.right)
            self.isSubtree(root.left,subRoot.left)

        return True

a=Solution()
a.isSubtree([3,4,5,1,2],[4,1,2])