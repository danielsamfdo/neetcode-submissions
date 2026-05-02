# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(0)
        point = dummyhead
        c = 0
        while l1 and l2:
            point.next = ListNode((l1.val + l2.val + c)%10)
            c = (l1.val + l2.val + c) // 10
            point = point.next
            l1 = l1.next
            l2 = l2.next
        if not l1:
            while l2:
                point.next = ListNode((l2.val + c)%10)
                c = ( l2.val + c ) // 10
                l2 = l2.next
                point = point.next
        if not l2:
            while l1:
                point.next = ListNode((l1.val  + c)%10)
                c = (l1.val + c) // 10
                l1 = l1.next
                point = point.next
        if c:
            point.next = ListNode(c)
        return dummyhead.next
