class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        if not current:
            return
        # Move to the end of the list
        while current.next:
            current = current.next
        # Traverse backwards
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage:
dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_end(4)
dll.insert_at_end(5)
dll.traverse_forward()    # Output: 2 <-> 3 <-> 4 <-> 5 <-> None
dll.traverse_backward()   # Output: 5 <-> 4 <-> 3 <-> 2 <-> None
