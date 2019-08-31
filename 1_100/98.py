# 98 Validate binary search tree 验证二叉搜索树

__author__ = 'Yang Xuan (jumpthepig@gmail.com)'


import sys
sys.path.append('.')
from schema import BinaryTree, time_it
from schema import TreeNode


class Solution:
    @classmethod
    @time_it
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        中序遍历， 看此节点是否比上一节点的值大，使用全局变量存储上一节点的值
        '''
        global temp
        temp = float("-inf")
        return self._isValidBST(root)
        pass

    @classmethod
    def _isValidBST(self, root):
        global temp
        if not root:
            return True

        flag = self._isValidBST(root.left)

        if root.val <= temp:
            flag = False
        else:
            temp = root.val

        return flag and self._isValidBST(root.right)


case1 = BinaryTree([5, 1, 4, None, None, 3, 6])
assert not Solution.isValidBST(case1.root)
case2 = BinaryTree([2, 1, 3])
assert Solution.isValidBST(case2.root)
case3 = BinaryTree([10, 5, 15, None, None, 6, 20])
assert not Solution.isValidBST(case3.root)
