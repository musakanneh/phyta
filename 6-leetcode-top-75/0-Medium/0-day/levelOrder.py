#!/usr/bin/python3
"""Binary Tree Level Order Traversal"""

"""Given a binary tree, return the level order traversal of
its nodes' values. (ie, from left to right, level by level).

https://leetcode.com/problems/binary-tree-level-order-traversal/

"""




from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        if root is None:
            return ans

        q = deque([root])

        while q:
            n = len(q)
            temp = []

            for i in range(0, n):
                f = q.popleft()
                temp.append(f.val)

                if f.left is not None:
                    q.append(f.left)
                if f.right is not None:
                    q.append(f.right)

            if len(temp) > 0:
                ans.append(temp[:])
                temp.clear()

        return ans
