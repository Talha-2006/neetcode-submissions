"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = None
        curr = head
        head_curr = None
        hash_table = {}

        while curr:
            if not new_head:
                new_head = Node(curr.val)
                head_curr = new_head
                hash_table[curr] = head_curr
                curr = curr.next
            else:
                new = Node(curr.val)
                head_curr.next = new
                head_curr = new
                hash_table[curr] = head_curr
                curr = curr.next
        
        curr = head
        while curr:
            new = hash_table[curr]
            if curr.random == None:
                new.random = None
                curr = curr.next
            else:
                new_random = hash_table[curr.random]
                new.random = new_random
                curr = curr.next
        
        return new_head
        




        