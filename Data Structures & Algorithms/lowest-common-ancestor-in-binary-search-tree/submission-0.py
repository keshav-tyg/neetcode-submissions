# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #things i dont understand
       

        # Plan: If both are smaller than root, go left
        # if both are greater than root, go right,
        # else
    
                if p.val > root.val and q.val > root.val:
                    return self.lowestCommonAncestor(root.right, p, q)
                
                elif p.val < root.val and q.val < root.val:
                    return self.lowestCommonAncestor(root.left, p, q)
                
                else:
                    return root
                
                

                #Test case
                # p = 2 and q = 4


    
        