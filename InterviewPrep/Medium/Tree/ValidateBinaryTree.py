"""
https://neetcode.io/problems/valid-binary-search-tree/question

Video: https://www.youtube.com/watch?v=s6ATEkipzow

Valid Binary Search Tree

Given the root of a binary tree, return true if it is a valid binary search tree,
otherwise return false.

A valid binary search tree satisfies the following constraints:
- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees are also binary search trees.

Example 1: TRUE

            2
    -----------------
    |               |
    1               3

Input: root = [2,1,3]
Output: true

Example 2: FALSE

            1
    -----------------
    |               |
    2               3

Input: root = [1,2,3]
Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is
greater than 1 (root node's value).

Constraints:
1 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            # root is null.
            if not node:
                return True

            # core condition of binary tree is false.
            if not (node.val < right and node.val > left):
                return False

            return (
                    # check if left subtree is valid.
                    # every value in left subtree must be less than root (node.val)
                    valid(node.left, left, node.val)

                    and

                    # check if right subtree is valid.
                    # every value in right subtree must be more than root (node.val)
                    valid(node.right, node.val, right)
            )

        # for root, left value could be negative infinity and right could be positive infinity.
        return valid(root, float("-inf"), float("inf"))