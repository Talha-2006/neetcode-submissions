# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        mid = (count + 1) // 2

        curr = head
        prev_mid = None
        count = 0

        while count < mid:
            prev_mid = curr
            curr = curr.next
            count += 1

        head2 = curr

        prev_mid.next = None

        prev = None
        curr = head2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head2 = prev

        head1 = head

        while head2:
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            head2.next = temp1

            head1 = temp1
            head2 = temp2

        




        