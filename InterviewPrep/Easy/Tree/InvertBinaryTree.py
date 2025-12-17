"""
https://neetcode.io/problems/invert-a-binary-tree/question

Invert Binary Tree

You are given the root of a binary tree root.
Invert the binary tree and return its root.

Example 1:
            1                               1
        ---------                       ---------
    |               |               |               |
    2               3       ->      3               2
    |               |               |               |
---------       ---------       ---------       ---------
4       5       6       7       7       6       5       4

Input: root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Example 2:
         3                 3
     ---------         ---------
    |        |   ->   |        |
    2        1        1        2

Input: root = [3,2,1]
Output: [3,1,2]

Example 3:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # invert children.
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left) # invert left subtree
        self.invertTree(root.right) # invert right subtree

        return root # return the root.