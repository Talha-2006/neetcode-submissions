# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        sum1 = 0
        curr = l1
        while curr:
            sum1 += (curr.val * (10 ** count))
            count += 1
            curr = curr.next
        
        count = 0
        sum2 = 0
        curr = l2
        while curr:
            sum2 += (curr.val * (10 ** count))
            count += 1
            curr = curr.next
        
        total = str(sum1 + sum2)

        head = None
        for i in range(len(total) -1, -1, -1):
            if not head:
                head = ListNode(int(total[i]))
                prev = head
            else:
                new = ListNode(int(total[i]))
                prev.next = new
                prev = new
        
        return head
        

        