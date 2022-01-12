# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        '''
        下列代码无法实现目标
        #DFS
        #左右子树都为空证明该节点为叶子节点
        if root is None:
            return []
        cnt = 1 
        re = []
        def DFS(root,re,cnt):
            
            if root.left is None and root.right is None:
                re.append((root.val,cnt))
                root = None
                return re
            DFS(root.left,re,cnt+1)
            DFS(root.right,re,cnt+1)
            if root is not None:
                re.append((root.val,cnt))
        DFS(root,re,cnt)
        print(re)
        '''
        re = {}
        #当前节点离叶子节点的高度是多少
        def DFS(root):
            if root is None:
                return 0
            left = DFS(root.left)#  left 代表左子树高度
            right = DFS(root.right)#    right 代表右子树高度
            depth = max(left,right) + 1 #因为是当前节点到左右子树的高度，所有这里要加1
            if depth not in re.keys():
                re[depth] = [root.val]
            else:
                re[depth].append(root.val)
            return depth
        DFS(root)
        print(re)
        return [value for key,value in re.items()]