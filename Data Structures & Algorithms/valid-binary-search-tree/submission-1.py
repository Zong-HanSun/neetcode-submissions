# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], left: float, right: float) -> bool:
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            is_left_valid = isValid(node.left, left, node.val)
            is_right_valid = isValid(node.right, node.val, right)
            return is_left_valid and is_right_valid

            

        return isValid(root, float("-inf"), float("inf"))

        
        