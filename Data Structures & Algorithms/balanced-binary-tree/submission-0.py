# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        output = True
        def height(root):
            nonlocal output

            if root == None:
                return 0
            
            tryleft = height(root.left)
            tryright = height(root.right)

            if tryleft - tryright > 1 or tryright - tryleft > 1:
                output = False
            return 1 + max(tryleft, tryright)
        height(root)
        return output
        


        