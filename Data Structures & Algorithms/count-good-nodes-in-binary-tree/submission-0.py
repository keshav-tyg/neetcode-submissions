#USE DFS
#go to the deepest part and search
#Even the roots value can't be bigger than the node x

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def find(root, maxsofar):
            if not root:
                return 0
            good = 1 if root.val >= maxsofar else 0
            maxsofar = max(maxsofar, root.val)
            return good + find(root.left, maxsofar) + find(root.right, maxsofar)

        return find(root, root.val)


    
        