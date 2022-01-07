
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #最近公共祖先的定义：
        #设节点root为p和q的某一公共祖先，若其左节点root.left 和其右节点root.right
        #都不是p和q的公共祖先，则root为p和q的“最近公共祖先”
        #思路1：
        #找到节点p的所有的祖先
        #找到节点q的所有的祖先
        #但是每个祖先节点的深度？
        #思路2：
        #回溯，即从底网上查找
        #后序遍历(有递归和非递归两种算法)就是典型的回溯
        if root is None:
            return None
        if root == p or root == q:
            return root 
        left = self.lowestCommonAncestor(root.left,p,q)

        right = self.lowestCommonAncestor(root.right,p,q)
        if left is None and right is not None:
            return right
        elif left is not None and right is None:
            return left
        elif left is not None and right is not None:
            return root 