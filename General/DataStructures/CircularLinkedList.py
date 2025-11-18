class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.last = None

    def add_to_empty(self, data):
        if self.last is not None:
            return self.last
        new_node = Node(data)
        self.last = new_node
        self.last.next = self.last
        return self.last

    def add_front(self, data):
        if self.last is None:
            return self.add_to_empty(data)
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node
        return self.last

    def add_end(self, data):
        if self.last is None:
            return self.add_to_empty(data)
        new_node = Node(data)
        new_node.next = self.last.next
        self.last.next = new_node
        self.last = new_node
        return self.last

    def add_after(self, data, item):
        if self.last is None:
            return None
        new_node = Node(data)
        current = self.last.next
        while True:
            if current.data == item:
                new_node.next = current.next
                current.next = new_node
                if current == self.last:
                    self.last = new_node
                return self.last
            current = current.next
            if current == self.last.next:
                print(f"{item} not found in the list")
                break
        return self.last

    def delete_node(self, key):
        if self.last is None:
            return None
        # Single node case
        if self.last.data == key and self.last.next == self.last:
            self.last = None
            return self.last
        current = self.last.next
        prev = self.last
        while current.data != key:
            if current == self.last:
                print("Node with key not found")
                return self.last
            prev = current
            current = current.next
        # Node to delete is found
        if current == self.last:
            prev.next = current.next
            self.last = prev
        else:
            prev.next = current.next
        return self.last

    def traverse(self):
        if self.last is None:
            print("The list is empty")
            return
        current = self.last.next
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.last.next:
                break
        print("(back to start)")

# Example usage:
cll = CircularLinkedList()
cll.add_to_empty(6)
cll.add_end(8)
cll.add_front(2)
cll.add_after(10, 2)
cll.traverse()  # Expected output: 2 -> 10 -> 6 -> 8 -> (back to start)
cll.delete_node(8)
cll.traverse()  # Expected output: 2 -> 10 -> 6 -> (back to start)
