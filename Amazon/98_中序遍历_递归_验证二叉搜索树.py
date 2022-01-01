# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #中序遍历(递归DFS)
        print(root)

        def order(root,L,R):

            if root is None:
                return True
            l = order(root.left,L,root.val)
            if root.val <= L or root.val >= R:
                return False
            r = order(root.right,root.val,R)
            return l and r 



        L = -(2**31)-1
        R = 2**31  
        return order(root,L,R)