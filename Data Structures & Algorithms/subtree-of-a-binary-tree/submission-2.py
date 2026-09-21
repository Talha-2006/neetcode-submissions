# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p, q):
            if (p and not q) or (q and not p):
                return False
            if not p and not q:
                return True
            else:
                if p.val != q.val:
                    return False
                return check(p.left, q.left) and check(p.right, q.right)
        
        def dfs(root, subRoot):
            if (not root and subRoot) or (root and not subRoot):
                return False
            elif not root and not subRoot:
                return True
            else:
                if root.val == subRoot.val and check(root, subRoot):
                    return True

                return dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        return dfs(root, subRoot)
                
                