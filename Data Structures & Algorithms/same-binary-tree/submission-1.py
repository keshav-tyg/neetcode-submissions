# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        jak = []
        kak = []
        def height(root, bag):
            if root == None:
                bag.append(None)
                return
            bag.append(root.val)
            lefty = height(root.left, bag)
            righty = height(root.right, bag)
            return
        ptry = height(p, jak)
        qtry = height(q, kak)

        if jak == kak:
            return True
        else:
            return False




      
        