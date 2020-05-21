"""
[LeetCode] - 112. Path Sum

https://leetcode.com/problems/path-sum/
"""
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


# Function to insert nodes in level order
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root


def inOrder(arr):
    for i, e in enumerate(arr):
        print(e, end=" ")
        if i in [0,2,6,14]:
            print()

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

if __name__ == '__main__':
    arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    # arr = [1,2,3,4,5,6,7]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    inOrder(arr)

    s = Solution()


    s.hasPathSum(root,22)

# graph = [5,4,8,11,None,13,4,7,2,None,None,None,1]
# s = 22
# graph = TreeNode(graph)
# print(graph)
# hasPathSum(graph, s)