"""
https://neetcode.io/problems/count-connected-components/question

Video: https://www.youtube.com/watch?v=8f1XPm4WOUc

Number of Connected Components in an Undirected Graph

There is an undirected graph with n nodes. There is also an edges array,
where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:
Input:
n=3
edges=[[0,1], [0,2]]
Output:
1

Example 2:
Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]
Output:
2

Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""

# Union Find algorithm
#
# 2 arrays
#   - parent -> [0....n] -> [0,1,2,3,4] -> start with max num of connections.
#   - rank -> [1.....1] -> [1,1,1,1,1] -> num of nodes for a parent.
#   -> keep finding root parent, each time a parent-child node is found, perform union and reduce the rank.
#   -> iterate over number of edges.
#   -> num - (total unions performed) = answer.

class Solution:
    def numConnectedComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)] # root parent for each node.
        rank = [1] * n # number of connected nodes from the root parent.

        print(f"parent: {parent}, rank: {rank}")
        def find(fn1): # find root parent of the node
            print(f"===== =====Find root parent for: {fn1}")
            res1 = fn1

            print(f"===== ===== =====Current parent: {parent[res1]}, grand parent: {parent[parent[res1]]}")
            while res1 != parent[res1]:
                print(f"===== ===== ===== =====While loop: parent: {parent[res1]}, grand parent: {parent[parent[res1]]}")
                # if there is a grandparent, use that.
                parent[res1] = parent[parent[res1]] # this is optional.
                res1 = parent[res1]
                print(f"===== ===== ===== =====Updated res1: {res1}, parent: {parent[res1]}, grand parent: {parent[parent[res1]]}")

            print(f"===== ===== =====Root parent for {fn1} is {res1}.")
            print(f"===== ===== =====Find update: parent: {parent}, rank: {rank}")
            return res1 # return root parent

        def union(un1, un2):
            print(f"=====Union with n1: {un1} and n2: {un2}")
            p1, p2 = find(un1), find(un2) # find root parents for each node.

            print(f"===== =====p1: {p1} and p2: {p2}")
            if p1 == p2: # both have same parents.
                return 0 # no union performed.

            print(f"===== =====Ranks before update: p1: {rank[p1]} and p2:{rank[p2]}")
            if rank[p2] > rank[p1]: # p2 is the parent of p1
                parent[p1] = p2 # update root parent
                rank[p2] += rank[p1] # increase parent's rank
            else: # p1 is the parent of p2
                parent[p2] = p1 # update root parent
                rank[p1] += rank[p2]  # increase parent's rank
            print(f"===== =====Updated ranks: p1: {rank[p1]} and p2:{rank[p2]}")
            print(f"===== =====Union update: parent: {parent}, rank: {rank}")
            return 1 # union performed.

        res = n
        for n1, n2 in edges:
            print(f"Running nodes n1: {n1} and n2: {n2}, res:{res}")
            res -= union(n1, n2)
            print(f"Updated res {res}, rank: {rank}")

        return res

print(Solution().numConnectedComponents(n=6, edges=[[0,1], [1,2], [2,3], [4,5]]))
"""
n: num of nodes, e: num of edges
Runtime: O(n + e)
Space:
"""
