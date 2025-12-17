"""
https://neetcode.io/problems/level-order-traversal-of-binary-tree/question

Video: https://www.youtube.com/watch?v=6ZnyEApgFYg

Binary Tree Level Order Traversal

Given a binary tree root, return the level order traversal of it as a nested list,
where each sublist contains the values of nodes at a particular level in the tree,
from left to right.

Example 1:
            1
        ---------
    |               |
    2               3
    |               |
---------       ---------
4       5       6       7



Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []

        queue = deque([root])

        # queue will be empty when all nodes have been traversed.
        while queue:
            # check all nodes at the current level and add their children if any.
            level_nodes = []
            for i in range(len(queue)):
                # remove the first inserted node (parent of left and right).
                node = queue.popleft()

                if node:
                    level_nodes.append(node.val) # add the current level node value
                    queue.append(node.left) # add left child to the queue.
                    queue.append(node.right) # add right child to the queue.

            if level_nodes:
                res.append(level_nodes)
        return res

"""
Runtime: O(n) to traverse all nodes.
Space: O(n) to store all node values.
"""