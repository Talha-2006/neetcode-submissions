# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(minimum, maximum, root):
            if not root:
                return True
            if root.val >= maximum:
                return False
            if root.val <= minimum:
                return False
            else:
                return valid(minimum, root.val, root.left) and valid(root.val, maximum, root.right)

        return valid(-1 * float("inf"), float("inf"), root) 
        