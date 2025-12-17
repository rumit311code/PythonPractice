"""
https://neetcode.io/problems/depth-of-binary-tree/question

Video: https://www.youtube.com/watch?v=hTM3phVI6YQ

Maximum Depth of Binary Tree

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes
along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [1,2,3,null,null,4]

    1
---------
|       |
2       3
        |
        4

Output: 3

Example 2:
Input: root = []
Output: 0

Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100
"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    #### DFS recursive ####
    #
    # find max depth for each child node recursively.
    #
    # node 1 -> 1 + max(depth of 2, depth of 3)
    #   1-> 1 + (1,2) -> 1+2 -> max depth of node 1 is 3.
    # node 2 -> 1 + max(depth of left child = null = 0, depth of right child = null = 0).
    #   2 -> 1 + (max(0,0) -> max depth of node 2 is 1.
    # node 3 -> 1 + max(depth of 4, depth of right child = null = 0).
    #   3 -> 1 + (max(depth of 4,0) -> 1 + 1 -> max depth of node 3 is 2.
    # node 4 -> 1 + max(depth of left child = null = 0, depth of right child = null = 0).
    #   4 -> 1 + (max(0,0) -> max depth of node 4 is 1.
    def maxDepth_DFS_Recursive(self, root: Optional[TreeNode]) -> int:
        print(f"calling maxDepth with root: |{root}|")
        if not root:
            print(f"-----current node is NULL: {root}. returning 0.")
            return 0
        print(f"----- non-null root: |{root.val}|{root.left}|{root.right}")
        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        print(f"----- -----current depth: {depth}")
        return depth

    #### BFS iterative ####
    #
    # use queue.
    #
    # count the number of levels (depths).
    # queue: [1]    -> level 1
    # queue: [2, 3] -> level 2
    # queue: [4]    -> level 3
    def maxDepth_BFS_Iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            print(f"-----current node is NULL: {root}. returning 0.")
            return 0

        queue = deque([root])
        levels = 0

        # queue will be empty when all nodes have been traversed.
        while queue:
            # check all nodes at the current level and add their children if any.
            for i in range(len(queue)):
                # remove the first inserted node (parent of left and right).
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels += 1 # increase the level
        return levels

    #### DFS iterative ####
    #
    # use stack. -> preorder DFS.
    #
    # count the depth at each node iteratively.
    # node1 -> depth 1
    # node2 -> depth 2
    # node3 -> depth 2
    # node4 -> depth 3
    # the max depth up to node4 is 3.
    def maxDepth_DFS_Iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [[root, 1]]
        res = 0
        while stack:
            # get the last inserted node and its depth
            node, depth = stack.pop()

            # this condition takes care of stopping at null nodes.
            if node:
                res = max(res, depth) # get max depth of any children so far.
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res

"""
Runtime: TBD
Space: TBD
"""