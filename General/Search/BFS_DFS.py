from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
"""
        A
    ---------
    |       |  
    B       C
--------    |
|       |   |
D       E---F
"""

# Iterative BFS (queue)
def bfs_iterative(graph, start):
    visited = set()
    queue = deque(start) # FIFO
    while queue:
        node = queue.popleft() # pop first inserted element.
        if node not in visited:
            print(node, end="-")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

print("Iterative BFS:", end=' ')
bfs_iterative(graph, 'A')  # A B C D E F

# Iterative DFS (stack)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start] # LIFO. In python stack = list.
    while stack:
        node = stack.pop() # pop last inserted element.
        if node not in visited:
            print(node, end="-")
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

print("")
print("Iterative DFS:", end=' ')
dfs_iterative(graph, 'A')  # A C F E B D (stack order)

# Recursive DFS (most common recursive form)
def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    if start not in visited:
        print(start, end="-")
        visited.add(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_recursive(graph, neighbor, visited)

print("")
print("Recursive DFS:", end=' ')
dfs_recursive(graph, 'A')  # A B D E F C (call stack order)

# Recursive BFS (less common, uses recursion + queue parameter)
def bfs_recursive(graph, start, queue=None, visited=None):
    if queue is None:
        queue = deque([start])
    if visited is None:
        visited = set()

    if not queue:
        return

    node = queue.popleft()
    if node not in visited:
        print(node, end="-")
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
        bfs_recursive(graph, start, queue, visited)

print("")
print("Recursive BFS:", end=' ')
bfs_recursive(graph, 'A')  # A B C D E F

"""
Recursive DFS dominates in practice due to simplicity.
BFS stays iterative for memory efficiency.

BFS
    Pro: Finds shortest path in unweighted graphs; guarantees completeness if branching factor is finite
    Con: Consumes more memory (stores entire level); slower if solution is deep
    Best: Finding shortest paths; shallow graphs

DFS
    Pro: Uses less memory overall; good for deep searches; can be implemented recursively or iteratively
    Con: May not find shortest path; can get stuck in deep or infinite branches without depth limit
    Best: Exploring deep or complex graphs; topological sort; cycle detection
    
Iterative BFS
    Shortest path guarantee; no recursion limit
    High memory (O(w) width)
    Space: O(V+E)

Recursive BFS (LESS COMMON)
    Shortest path guarantee; no recursion limit
    Recursion depth = path length; rare usage
    Space: O(V) recursion + O(w) queue

Iterative DFS
    No recursion limit; simulates recursion
    Stack management manual
    Space: O(V) worst case

Recursive DFS
    Simple, elegant code
    Risk of stack overflow (depth >1000)
    Space: O(V) recursion depth
"""