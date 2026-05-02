# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        # fast = head
        # slow = head.next
        fast, slow = head, head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        # if slow:
        #     print(slow.val)
        # if fast:
        #     print(fast.val)
        # if slow == fast and slow is not None:
        #     return True
        
        return False
