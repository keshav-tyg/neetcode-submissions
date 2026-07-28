# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashes = set()
        tail = head
        index = 0
        while tail:
            if tail in hashes:
                return True
            hashes.add(tail)
            tail = tail.next
            index += 0
        
        if tail == None:
            index = -1
            return False


        
