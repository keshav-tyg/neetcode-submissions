# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
       
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        #Cuts off first half
        slow.next = None
        curr = second
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # Reversed the list
        # now we have 
        # 1, 2 ,3 ,4 
        # 6, 5
        #To interleave
        tail = head
        while tail and prev:
            temp = tail.next
            temp2 = prev.next
            tail.next = prev
            prev.next = temp
            tail = temp
            prev = temp2
        print(head)


            


        