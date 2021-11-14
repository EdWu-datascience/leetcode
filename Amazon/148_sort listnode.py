#给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

#进阶：

#你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#归并排序链表
#主要有两个环节：1分割cut环节，2merge排序环节
        def sortFunc(head,tail):
            if head is None: # 递归终止的条件是当前链表的节点数小于等于1
                return head
            if head.next == tail:
                head.next = None
                return head 
            slow = fast = head # slow每次移动一个node，fast每次移动两个node，当fast移动到尾端时，slow指向的应该刚好是中间节点
            while fast != tail:
                slow = slow.next
                fast = fast.next 
                if fast != tail:
                    fast = fast.next 
            mid = slow 
            return mergeFunc(sortFunc(head,mid),sortFunc(mid,tail))
        def mergeFunc(head1,head2):
            dummyHead = ListNode(0)
            temp,temp1,temp2 = dummyHead,head1,head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:#该while循环是对temp1和temp2进行遍历排序，直到至少其中一方到头为止
                    temp.next = temp1
                    temp = temp.next 
                    temp1 = temp1.next 
                else:
                    temp.next = temp2
                    temp2 = temp2.next 
                    temp = temp.next 
            if temp1:#这两个if是因为可能存在其中一个链表还没有遍历到头而另一个遍历到头
                temp.next = temp1
            if temp2:
                temp.next = temp2
            return dummyHead.next 
        return sortFunc(head,None)
        '''
#该方法是将listnode拆分成字典，key是node本身，value是node的val，然后sorted是根据val进行排序
#该方法超时
        if head is None:
            return head
        temp = head
        count = {}
        while temp is not None:
            temp1 = temp.next 
            temp.next = None
            count[temp] = temp.val
            temp = temp1
        a = sorted(count.items(),key = lambda item : item[1])
        temp = a[0][0]
        a[0][0].next = None
        head = temp
        #for i in range(1,len(a)):
        #    a[i][0].next = None
        for i in range(1,len(a)):
            temp.next = a[i][0]
            temp = temp.next 
        print(head)
        return head
        '''
