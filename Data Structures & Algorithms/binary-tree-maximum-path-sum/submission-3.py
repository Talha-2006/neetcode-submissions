# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1 * float("inf")
        def dfs(root):
            if not root:
                return 0
            else:
                max_left = 0
                max_right = 0
                if root.left:
                    max_left = dfs(root.left)
                if root.right:
                    max_right = dfs(root.right)
                
                curr_total = root.val + max(max_left, 0) + max(max_right, 0)

                self.res = max(curr_total, self.res)

                return root.val + max(max_left, max_right, 0)
        
        dfs(root)
        return self.res




        