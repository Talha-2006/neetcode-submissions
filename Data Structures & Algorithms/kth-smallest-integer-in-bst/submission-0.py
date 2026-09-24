# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered = []
        
        def build_list(root):
            if root.left:
                build_list(root.left)
            ordered.append(root.val)
            if root.right:
                build_list(root.right)

        build_list(root)
        return ordered[k-1]


        