# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        dummy = ListNode(0, head)
        prev_group_tail = dummy
        curr = head

        for _ in range(length // k):
            first = curr
            prev = None
            count = 0

            while count < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count += 1

            prev_group_tail.next = prev
            first.next = curr

            prev_group_tail = first

        return dummy.next

            
            

        