"""
https://neetcode.io/problems/valid-tree/question

Video: https://www.youtube.com/watch?v=bXsUuownnoQ

Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:
Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
Output:
true

Example 2:
Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
Output:
false

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""

# Definition of a Tree
#   - there is no loop
#   - each node is connected to at least one other node
#
# maintain a visited and prev nodes
#   - "visit" set to check if all nodes are visited and to check if there is a loop.
#   - "prev" set to avoid visiting the parent node.


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n = 5
        # edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        #   0: -> 1,2,3
        #   1: -> 4

        if not n: # if no nodes, return true
            return True

        # [
        #   0:[],
        #   1:[],
        #   2:[],
        #   3:[],
        #   4:[]
        # ]
        adjacency = {i: [] for i in range(n)}

        for n1, n2 in edges:
            # 0: [1,2,3]
            # 1: [0,4]
            # 2: [0]
            # 3: [0]
            # 4: [1]
            # add adjacency for node and edge both because edges are bidirectional
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)

        print(f"====adjacency: {adjacency}")

        # visited = (0, 1, 2, 3, 4)
        visited = set()
        def dfs(i, prev): # O(nodes)
            print(f"==== ==== DFS start with i:{i}, prev:{prev}, visited:{visited}")
            if i in visited: # loop detected
                return False

            visited.add(i)
            print(f"==== ==== ====updated visited:{visited}")

            # for each neighbour of i ->
            print(f"==== ==== ====loop for adjacency[i]:{adjacency[i]}")

            # j = [1,2,3], [0,4], [0], [0], [1]
            # O(edges)
            for j in adjacency[i]:
                print(f"==== ==== ==== ====j:{j}, prev:{prev}")
                if j == prev: # parent node is already visited.
                    print("==== ==== ==== ==== ====prev already visited")
                    continue

                # i is the prev node for j.
                print(f"==== ==== ==== ==== ====running NEW DFS for i:{j}, prev:{i}")
                if not dfs(j, i): # if False, there is a loop detected.
                    print(f"==== ==== ==== ==== ====returning FALSE for i:{j}, prev:{i}")
                    return False

            # no loops detected at node i.
            print(f"==== ==== returning TRUE for i:{i}, prev:{prev}, visited:{visited}")
            return True

        # dfs -> no loops
        # n == len(adjacency) -> all nodes are connected
        # 0 is the starting node so no prev. so set to -1.
        return dfs(0, -1) and n == len(visited)

print(Solution().validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])) # True
print(Solution().validTree(n=3, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])) # Exception. not handled in the program.
print(Solution().validTree(n=4,edges=[[0,1],[2,3]]))
"""
n: number of nodes, e: is the number of edges.
Runtime: O(n+e) to iterate through visited set + each edge.
Space: O(n+e) to store visited set and edges.
"""