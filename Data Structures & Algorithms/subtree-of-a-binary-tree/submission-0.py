# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = False
        def dfs_double(root, subRoot):
            if not root and not subRoot:
                return 0

            if not root or not subRoot:
                return 1

            if root.val != subRoot.val:
                return 1

            left = dfs_double(root.left, subRoot.left)
            right = dfs_double(root.right, subRoot.right)

            return max(left, right)
            
        def dfs(root, subRoot):
            if not root:
                return

            if root.val == subRoot.val:
                val = dfs_double(root, subRoot)

                if val == 0:
                    self.flag = True
                    return

            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
        
        dfs(root, subRoot)

        return self.flag
        