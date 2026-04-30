# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def serialize(node, arr):
            if not node:
                arr.append(None)
                return
            arr.append(node.val)
            serialize(node.left, arr)
            serialize(node.right, arr)
    
        arr1, arr2 = [],[]
        serialize(p, arr1)
        serialize(q, arr2)
        return arr1 == arr2
