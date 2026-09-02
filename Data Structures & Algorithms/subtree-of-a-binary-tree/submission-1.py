# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
            
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            is_left_same = self.isSameTree(p.left, q.left)
            is_right_same = self.isSameTree(p.right, q.right)
            return is_left_same and is_right_same
        else:
            return False



