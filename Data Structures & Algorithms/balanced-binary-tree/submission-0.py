# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, 0)

            left = dfs(root.left)
            right = dfs(root.right)

            if not left[0] or not right[0]:
                return (False, -1)

            if abs(left[1] - right[1]) > 1:
                return (False, -1)

            height = 1 + max(left[1], right[1])

            return (True, height)

        res = dfs(root)

        return res[0]
        
            
        
            
            
            



        