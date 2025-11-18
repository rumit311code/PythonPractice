# A stack follows the Last-In-First-Out (LIFO) principle.
# In Python, you can use a list for stack operations.

# Create a stack
stack = []

# Insert (push)
stack.append(10)
stack.append(20)
print("Stack BEFORE pop:", stack)

# Retrieve (peek top)
# -1 -> last item, -2 -> second to the last item...
top_item = stack[-1] if stack else None
print("Top item:", top_item)

# Delete (pop) # removes last inserted item
popped_item = stack.pop() if stack else None
print("Popped item:", popped_item)
print("Stack AFTER pop:", stack)

"""
Stack (LIFO: Last In First Out)
Use when you need the most recent item first or reverse order processing
such as managing function calls or undo functionality.

Practical examples
- Function call management and recursion (call stack)
- Undo/redo operations in software
- Expression evaluation and syntax parsing
- Backtracking algorithms

Pros
- Simple push and pop operations (O(1))
- Useful in managing nested structures or reversing order

Cons
- No access to older elements except from top
- Not suitable when order preservation is required
"""