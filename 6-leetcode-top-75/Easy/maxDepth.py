# Definition for a binary tree node.
class TreeNode:
    """Maximum Depth of Binary Tree
    Given the root of a binary tree, return its maximum depth.
    https://leetcode.com/problems/maximum-depth-of-binary-tree/
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        if(root.left is None and root.right is None):
            return 1

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right)+1
