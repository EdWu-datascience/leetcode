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
        if head is None:
            return None
        p = head
        #创建一个新的dict存储链表
        dic_node = {}
        while p:
            new_node = Node(p.val,None,None)
            dic_node[p] = new_node
            p = p.next 
        p = head
        while p:
            if p.next:
                dic_node[p].next = dic_node[p.next]
            if p.random:
                dic_node[p].random = dic_node[p.random]
            p = p.next
        return dic_node[head]