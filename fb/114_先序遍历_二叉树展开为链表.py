# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        #先序遍历：首先访问根节点，然后访问左子树，最后访问右子树
        #DFS
        #下列方法没有在root本身上面进行更改，而是占用了新的空间，最后将root指向
        #了新占用的空间
        if root is None:
            return None
        elif root.left is None and root.right is None:
            return root   
        re = []
        def DFS(root,re):
            if root is None:
                return root
            print(root.val)
            re.append(root.val)
            DFS(root.left,re)
            DFS(root.right,re)
        DFS(root,re)
        head = TreeNode(0)
        flag = head 
        for index,value in enumerate(re):
            head.val = value
            if index != len(re)-1:
                temp = TreeNode(0)
                head.right = temp
                head = head.right
        root = None
        root = flag 
        print(root)
        '''
        #思路：
        #存储当前节点的右子树temp
        #将当前节点的左子树放到右子树的位置上
        #找到当前节点右子树的最右边的节点point
        #将temp作为最右节点的右子树
        #将当前节点指向其右子树，重复上属过程
        #终止条件：
        #当前节点的右子树为空
        if root is None:
            return 
        head = root
        cur = head
        while cur:
            temp = cur.right
            cur.right = cur.left
            cur.left = None
            rightmost = cur
            while rightmost.right is not None:
                rightmost = rightmost.right
            rightmost.right = temp 
            cur = cur.right
        print(head)