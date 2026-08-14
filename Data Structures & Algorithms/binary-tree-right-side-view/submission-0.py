# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Include root
        #Include the ones that are on the right
        #Pick the rightmost of the level
        result = []

        q = collections.deque()
        q.append(root)
        while q:
            #get the length of the current level
            qLen = len(q)
            level = []
            #Run while the current level
            for i in range(qLen):
                #node will be what was popped on the left of the queue
                node = q.popleft()
                #if node is not null
                #add the value of it to level
                #and make sure to append its children to q back
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            #if level isnt none, append it to result
            if level:
                result.append(level[-1])
        return result



        