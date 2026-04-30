# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            if (abs(self.height(root.left) - self.height(root.right)) > 1):
                return False
            else : 
                return True & (self.isBalanced(root.left) ) & (self.isBalanced(root.right) )
        else:
            return True


    def height(self,node):
        if node:
            return 1 + max(self.height(node.left),self.height(node.right))
        else:
            return 0