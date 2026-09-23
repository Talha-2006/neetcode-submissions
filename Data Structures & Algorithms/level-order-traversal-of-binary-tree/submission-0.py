# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        res = []
        if not root:
            return res
        

        while q:
            curr = q.popleft()

            if len(res) < curr[1] + 1:
                res.append([curr[0].val])
            else:
                res[curr[1]].append(curr[0].val)


            if curr[0].left:
                q.append((curr[0].left, curr[1] + 1))
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))
        
        return res
            

            
