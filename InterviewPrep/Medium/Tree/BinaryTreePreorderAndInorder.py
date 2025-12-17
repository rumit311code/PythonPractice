"""
https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal/question

Video: https://www.youtube.com/watch?v=ihj4IQGZ2zc

Construct Binary Tree from Preorder and Inorder Traversal

You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree.
inorder is the inorder traversal of the same tree.

Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals
and return its root.

Example 1:

            1
    -----------------
    |               |
    2               3
    |               |
---------       ---------
null  null      null    4

Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]

Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

Constraints:
1 <= inorder.length <= 1000.
inorder.length == preorder.length
-1000 <= preorder[i], inorder[i] <= 1000
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first value in preorder is always the main root node.
        # first value in inorder is always the left most child node.
        # step1: get the first element from preorder as a root.
        # step2: find the index of the root (mid) in the inorder.
        #       -> all values left of it are in the left subtree of root.
        #       -> all values right of it are in the right subtree of root.
        # step3: create left subtree recursively.
        # step4: create right subtree recursively.

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0]) # find the index of the root

        # all elements left of root are part of left subtree
        root.left = self.buildTree(preorder[1:root_index + 1], inorder[:root_index])

        # all elements right of root are part of right subtree
        root.right = self.buildTree(preorder[root_index + 1:], inorder[root_index + 1:])

        return root


