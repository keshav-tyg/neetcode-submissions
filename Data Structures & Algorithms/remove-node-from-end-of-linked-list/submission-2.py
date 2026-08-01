# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        while current != None:
            count += 1
            current = current.next
        index = count - n
        # [1, 2, 3, 4 , 5] #n = 5
        if index == 0:
            head = head.next
            return head
        current = head
        prev = None
        pos = 0

        while current and pos < index:
            prev = current
            current = current.next
            pos += 1
  

        prev.next = current.next
        return head
        





        #remove the end node,
        #so the negative of the number

        # [1, 2, 3, 4, 5]
        # n = 2

        # len - n
        