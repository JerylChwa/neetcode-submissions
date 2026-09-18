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
        if head == None:
            return None

        hashy = {}

        # old node to new node
        original = head
        curr = original

        while curr:
            hashy[curr] = Node(curr.val)
            curr = curr.next

        #print(hashy)

        second_pass = original
        
       
        while second_pass:
            if second_pass.next != None:
                hashy[second_pass].next = hashy[second_pass.next]
            if second_pass.random != None:
                hashy[second_pass].random = hashy[second_pass.random]
            second_pass = second_pass.next
            
            
        return hashy[original]
        
        