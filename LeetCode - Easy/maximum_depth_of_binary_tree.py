# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def fn(root):
            if root is None:
                return 0

            left = fn(root.left)
            right = fn(root.right)

            return 1 + max(left, right)

        return fn(root)
        