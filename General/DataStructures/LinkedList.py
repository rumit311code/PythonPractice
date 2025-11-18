class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        current = self.head
        prev = None

        # If the head needs to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print(f"Node with value {key} not found.")
            return

        # Remove the node
        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()
print("Before deletion:")
ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> None
ll.delete_node(3)
print("After deletion of 3:")
ll.display()  # Output: 1 -> 2 -> 4 -> None
ll.delete_node(1)
print("After deletion of 1:")
ll.display()  # Output: 2 -> 4 -> None