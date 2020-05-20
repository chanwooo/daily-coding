"""
[LeetCode] - 112. Path Sum

https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def dfs(self, node, total):
        if not node:
            return

        total -= node.val

        if not node.left and not node.right and total == 0:
            self.ans = True
        self.dfs(node.left, total)
        self.dfs(node.right, total)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.ans = False

        self.dfs(root, sum)
        return self.ans
