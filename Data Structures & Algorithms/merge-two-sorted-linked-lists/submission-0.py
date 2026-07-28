# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if list 1 less is greater than the other, go to the next node in list 1 and compare,
        # if list 1 is greater than the other, temp = list.next
        #list.next = list2

        dummy = ListNode()      # sacrificial anchor
        tail = dummy            # the "end" of the list we're building
        while list1 != None and list2 != None:    
            if list1.val <= list2.val: # if list 1 is smaller than list2
                tail.next = list1
                list1 = list1.next # advance list1
                tail = tail.next # advance tail
            else :
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
        
        





        