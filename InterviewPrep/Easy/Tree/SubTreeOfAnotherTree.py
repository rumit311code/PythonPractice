"""
https://neetcode.io/problems/subtree-of-a-binary-tree/question

Video: https://www.youtube.com/watch?v=E36O5SWp-LE

Subtree of Another Tree

Given the roots of two binary trees root and subRoot,
return true if there is a subtree of root with
the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all
of this node's descendants.
The tree could also be considered as a subtree of itself.

Example 1: TRUE

          ROOT
            1
     ---------
    |         |         SUB-ROOT
    2         3     ->     2
    |                      |
---------              ---------
4       5              4       5

Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2: FALSE

       ROOT
        1
    ---------
    |       |          SUB-ROOT
    2       3    ->       2
    |                     |
---------             ---------
4       5             4       5
|
6

Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:
1 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if the subRoot is null then it's always a sub root of the root.
        if not subRoot:
            return True

        # root is null but subRoot is not null.
        if not root:
            return False

        # root and subRoot are non-null. compare them.
        if self.sameTree(root, subRoot):
            # the current root and subRoot are same trees.
            return True

        # root and subRoot are not same.
        return (
            # compare root's left and subroot
            self.isSubtree(root.left, subRoot)

            or

            # compare root's right and subroot
            self.isSubtree(root.right, subRoot)
        )

    # this function determines if both root and subRoot are same.
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # both root and subroot nodes are null
        if not root and not subRoot:
            return True

        # both roots are non-null and their values match.
        if root and subRoot and root.val == subRoot.val:
            return (
                # compare left nodes
                self.sameTree(root=root.left, subRoot=subRoot.left)

                and

                # compare right nodes
                self.sameTree(root=root.right, subRoot=subRoot.right)
            )

        # either only one of the roots is null OR their values don't match.
        return False


