# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(root) -> int:
            if not root:
                return 0
            else:
                left = 0
                right = 0
                if root.left:
                    left = 1 + dfs(root.left)
                if root.right:
                    right = 1 + dfs(root.right)
                self.longest = max(self.longest, right + left)
                return max(right, left)
        
        dfs(root)
        return self.longest


        
        