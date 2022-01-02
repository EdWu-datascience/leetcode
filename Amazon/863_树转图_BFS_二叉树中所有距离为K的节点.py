# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #树转图
        #将树的信息存入字典中，每个key代表一个节点，value存储所有和该节点直接相连的其他节点
        from collections import defaultdict
        graph = defaultdict(set)
        def dfs(node):
            if node.left:
                graph[node.val].add(node.left.val)
                graph[node.left.val].add(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].add(node.right.val)
                graph[node.right.val].add(node.val)
                dfs(node.right)
        dfs(root)
        print(graph)
        cur = [target.val]
        seen = {target.val}
        while k:#先找到所有与target相距为1的点，然后用这些相距为1的点找到这些点相距为1的点，即与
        #target相距为2的点...
            next_time = []
            while cur:
                temp = cur.pop()
                for node in graph[temp]:
                    if node not in seen:
                        next_time.append(node)
                        seen.add(node)
            cur = next_time
            k -= 1
        print(cur)
        return cur 
'''
        #先用DFS遍历整棵树，记录每个节点的父节点
        father = {}
        father[root] = None#树的根节点没有父节点，因此初始化为None
        
        def DFS(father,node):

            if node is None:
                return None
            temp = node 
            son1 = DFS(father,node.left)
            father[son1] = temp
            son2 = DFS(father,node.right)
            father[son2] = temp            
            return node
        DFS(father,root)
        father.pop(None)
        
        
        
        #分两步计算到target距离为k的点
        #1：找到target，然后深度优先遍历找到其距离为2的子节点
        #2：遍历father字典，找到key为target的位置，遍历其value(父节点)，从父节点往上找另外的距离
        #为k的点
        cnt = 0
        re = []
        def findson(node,cnt,re):
            
            if node is None:
                return 
            if cnt == k:
                re.append(node.val)
            findson(node.left,cnt+1,re)
            findson(node.right,cnt+1,re)

        findson(target,cnt,re)

'''
'''
        temp = None

        def findbrother(node,cnt,re,key):
            if node is None or node == key:
                return 
            if cnt == k:
                re.append(node.val)
            findbrother(node.left,cnt+1,re,key)
            findbrother(node.right,cnt+1,re,key)

        for key,value in father.items():
            if key == target:
                #print('value is : ')
                #print(value)
                temp = value 
                findbrother(temp,1,re,key)


        print(re)
        print(father)
        return re 
'''