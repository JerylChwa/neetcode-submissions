# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # use fast and slow pointer to split linkedlist in 2
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # if odd number of nodes, this is the smaller half
        prev = slow.next = None # this is meant for the last element of second half after reversing
        # reverse the links for second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        
        # combine the 2 halves
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


       


        