"""
https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree/question

Video: https://www.youtube.com/watch?v=gs2LMfuOR9k

Lowest Common Ancestor in Binary Search Tree

Given a binary search tree (BST) where all node values are unique,
and two nodes from the tree p and q, return the lowest common ancestor (LCA)
of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node
in a tree T such that both p and q as descendants.
The ancestor is allowed to be a descendant of itself.

Example 1:
            5
    -----------------
    |               |
    3               8
    |               |
---------       ---------
1       4       7       9
|
2


Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 8
Output: 5

Example 2:
            5
    -----------------
    |               |
    3               8
    |               |
---------       ---------
1       4       7       9
|
2

Input: root = [5,3,8,1,4,7,9,null,2], p = 3, q = 4
Output: 3
Explanation: The LCA of nodes 3 and 4 is 3, since a node can be a descendant of itself.

Constraints:
2 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
p != q
p and q will both exist in the BST.
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # if p and q are less and more than the root, they are in different subtrees.
    # for example, if p < root -> p is in the left subtree
    # for example, if q > root -> p is in the right subtree
    # whenever split occurs for p and q such that one of them is in left subtree
    # and another is in right subtree, that is the LCA of p and q.

    def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursive solution.

        # p and q both more than root. search right subtree.
        if p.val > cur.val and q.val > cur.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # p and q both less than root. search left subtree.
        elif p.val < cur.val and q.val < cur.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else: # either split case OR p or q or both equal to root.
            return root

    def lowestCommonAncestor2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # iterative solution.

        cur = root
        while cur:
            # p and q both more than root. search right subtree.
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # p and q both less than root. search left subtree.
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: # either split case OR p or q or both equal to root.
                return cur

"""
Runtime: O(log n) -> runtime to traverse BST.
Space: O(1) -> no data structure needed to store the result.
"""



