# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        l = count

        curr = head
        count = 0
        prev = None
        while curr:
            if (l - count) == n:
                break
            else:
                prev = curr
                curr = curr.next
                count += 1
        
        if not prev:
            if head:
                return head.next
            return None
        
        prev.next = curr.next
        return head


        