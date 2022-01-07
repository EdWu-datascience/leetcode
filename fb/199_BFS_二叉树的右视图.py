# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #使用层序遍历BFS(BFS基于迭代)，并且只保留每层的最后一个节点的值
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        re = []
        depth = 0
        queue = [[root,1]]#先进先出
        while queue:
            print(queue)
            temp = queue.pop(0)
            #判断是否是当前层的最后一个节点：
            #1：当队列为空时
            #2：当当前节点层级不等于下一个节点层级时
            if len(queue) == 0:
                re.append(temp[0].val)
            elif temp[1] != queue[0][1]:
                re.append(temp[0].val)

            if temp[0].left is not None:
                queue.append([temp[0].left,temp[1]+1])
            if temp[0].right is not None:
                queue.append([temp[0].right,temp[1]+1])
        print(re)
        return re 