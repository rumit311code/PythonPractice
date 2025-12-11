# A queue follows the First-In-First-Out (FIFO) principle.
# In Python, you can use collections.deque for efficient queue operations.

from collections import deque

# Create queue
queue = deque()

# Insert (enqueue)
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)

# [10, 20, 30, 40, 50]
print("Queue BEFORE dequeue:", list(queue))

# Retrieve (peek front)
front_item = queue[0] if queue else None
print("Front item:", front_item) # Front item: 10

# Delete (dequeue)
# popleft: removes left most item and returns it
dequeued_item = queue.popleft() if queue else None
print("Dequeued item:", dequeued_item) # Dequeued item: 10
print("Queue AFTER dequeue:", list(queue)) # [20, 30, 40, 50]

# pop: removes right most item and returns it
dequeued_item2 = queue.pop() if queue else None
print("Dequeued item2:", dequeued_item2) # Dequeued item2: 50
print("Queue AFTER dequeue:", list(queue)) # [20, 30, 40]
"""
Queue (FIFO: First In First Out)
Use when you want to process items in the exact order they arrive
such as task scheduling or breadth-first traversal.

Practical examples
- Scheduling processes in operating systems
- Managing requests in printer or task queues
- Breadth-first search (BFS) in graphs
- Customer service lines

Pros
- Maintains order of arrival
- Efficient enqueue and dequeue operations (O(1) using linked lists or deque)

Cons
- No random access to middle elements
- Slightly more complex implementation than stack if array resizing needed

"""