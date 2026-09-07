# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def builder(node):
            if not node:
                return 
            builder(node.left) 
            res.append(node.val) 
            
            builder(node.right)
    
        builder(root)
        # res = sorted(res)
            
        return res[k-1]
