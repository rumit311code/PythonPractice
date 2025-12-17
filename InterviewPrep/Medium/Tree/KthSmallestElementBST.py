"""
https://neetcode.io/problems/kth-smallest-integer-in-bst

Video: https://www.youtube.com/watch?v=5LUXSvjmGCw

Kth Smallest Integer in BST

Given the root of a binary search tree, and an integer k,
return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:
- The left subtree of every node contains only nodes with keys less than the node's key.
- The right subtree of every node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees are also binary search trees.

Example 1:
            2
    -----------------
    |               |
    1               3

Input: root = [2,1,3], k = 1
Output: 1

Example 2:
            4
    -----------------
    |               |
    3               5
    |
    2


Input: root = [4,3,5,2,null], k = 4
Output: 5

Constraints:
1 <= k <= The number of nodes in the tree <= 1000.
0 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse BST inorder
        # in-order traversal
        #   1. visit the left most child first
        #   2. keep traversing back up to the root
        #   3. now visit the right child of the root and repeat from 1.
        n = 0
        stack = []
        cur = root

        # iterate until stack is empty OR the farthest child is reached.
        while cur or stack:
            while cur: # go to the left most child.
                stack.append(cur)
                cur = cur.left

            cur = stack.pop() # process the element
            n += 1 # increment the count.
            if n == k:
                return cur.val # return the kth value.

            cur = cur.right # move to the right subtree.
