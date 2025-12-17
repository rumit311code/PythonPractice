"""
https://neetcode.io/problems/same-binary-tree/question

Video: https://www.youtube.com/watch?v=vRbbcKXCxOw

Same Binary Tree

Given the roots of two binary trees p and q,
return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same
structure and the nodes have the same values.

Example 1:
    1               1
---------       ---------
2       3       2       3

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
    4               4
---------      ---------
7    null      null    7

Input: p = [4,7], q = [4,null,7]
Output: false

Example 3:
    1               1
---------       ---------
2       3       3       2

Input: p = [1,2,3], q = [1,3,2]
Output: false

Constraints:
0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print(f"checking p|{p}|, q|{q}|")

        if not p and not q:
            print(f"----TRUE: both nodes are null.")
            return True

        if not p or not q or p.val != q.val:
            print(f"----FALSE: only one of the nodes is null or values don't match.")
            return False

        # both nodes are non-null and their values match.
        # now check their left and right children.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)