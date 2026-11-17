# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # reverse the second half 
        # merge first half and second half 

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next 
        
        # reverse starting from slow 
        list1 = head
        list2 = slow.next 
        slow.next = None # split lists 

        # reverse list 2 
        prev = None 
        
        while list2: 
            nxt = list2.next
            list2.next = prev 
            prev = list2
            list2 = nxt
        
        list2 = prev 

        # merge list1 and list2

        start = list1 
        while list1 and list2: 
            tmp1 = list1.next
            tmp2 = list2.next

            list1.next = list2
            list2.next = tmp1
            
            list1 = tmp1
            list2 = tmp2 


            







