#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
#(i.e., from left to right, then right to left for the next level and alternate between).










# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        stack = [root]
        re = []
        depth = 0
        while stack:
            temp = []
            next_level = []
            for node in stack:
                if node is not None:
                    temp.append(node.val)
                else:
                    temp.append(None)
                
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            stack = next_level
            if depth%2 == 0:
                re.append(temp)
            else:
                re.append(temp[::-1])
            depth += 1 
        print(re)
        return re 
'''
        count = 0 
        depth = 0
        temp = []
        while len(stack) != 0 and len([x for x in stack if x is not None]) != 0:
            A = stack.pop()
            if A is not None:
                if 2**depth == len(temp):
                    #re.append(A.val)
                    if None in temp:
                        re.append(temp[::-1])
                    else:
                        re.append(temp)
                    temp = []
                    depth += 1 
                    temp.append(A.val)
                else:
                    temp.append(A.val)
            else:
                if 2**depth == len(temp):
                    #re.append(None)
                    if None in temp:
                        re.append(temp[::-1])
                    else:
                        re.append(temp)
                    temp = []
                    depth += 1 
                    temp.append(None)
                else:
                    temp.append(None)
            if A is not None:
                if count%2 == 0:
                    stack.insert(0,A.right)
                    stack.insert(0,A.left)
                else:
                    stack.insert(0,A.left)
                    stack.insert(0,A.right)
            else:
                stack.insert(0,None)
                stack.insert(0,None)
            count += 1 
        if len([x for x in stack if x is not None]) == 0:
            if None in temp:
                re.append(temp[::-1])
            else:
                re.append(temp)
        print(re)
        for L in re:
            while None in L:
                L.remove(None)
        print(re)
        return re 

'''
            

        
