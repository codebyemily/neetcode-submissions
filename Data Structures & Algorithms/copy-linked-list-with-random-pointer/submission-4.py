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
        curr = head
        oldToNew = {} # oldNode to copy

        # make a copy using a dict 
        while curr: 
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        # connect pointers 
        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.random = oldToNew.get(curr.random)
            copy.next = oldToNew.get(curr.next)

            curr = curr.next 
        return oldToNew.get(head)

