#给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
#question:
#give a listnode, exchange the place of two adjacent nodes
#just simply change the values of nodes, but the actual node exchange 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #head = head.next 
        if head is None:
            return None
        if head.next == None:
            return head 
        listnode = [] 
        i = 0
        temp = []
        #this while loop get all pair of listnode into list
        #each element in list represent a sublist contains two node
        while head is not None:
            temp.append(head)
            head = head.next 
            if len(temp) == 2:
                listnode.append(temp)
                temp = []
        if len(temp) == 1:
            listnode.append(temp)
        flag = []
        #this for loop get each pair of node connect with each other 
        for node in listnode:
            if len(node)==2:
                front = node[0]
                node[1].next = node[0]
                node[0].next = None
                flag.append(node[1])
            else:
                node[0].next = None
                flag.append(node[0])
        print(flag)
        F = flag[0]
        head = F 
        #this for loop connect all the element by order 
        for i in flag[1:]:
            F.next.next = i
            F = i
        print(head)
        return head  