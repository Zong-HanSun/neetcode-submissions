# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l_tree_depth = self.maxDepth(root.left)
        r_tree_depth = self.maxDepth(root.right)
        
        return 1 + max(l_tree_depth, r_tree_depth)