"""
https://neetcode.io/problems/reverse-a-linked-list

Reverse Linked List

Given the beginning of a singly linked list head, reverse the list,
and return the new beginning of the list.

Example 1:
Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:
Input: head = []
Output: []

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000
"""

# two approaches

# approach 1: two pointers
# start with current = first, prev = None
# change current.next = prev, second (next) = first (current), first (current) = prev -> repeat, at the end prev=head.
# 1 -> 2 -> 3 -> 4 -> None
# None <- 1 <- 2 <- 3 <-4

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

class Solution:
    def reverseList(self, head: Node) -> Node:
        # 1 -> 2 -> 3 -> None

        previous = None
        current = head
        while current:
            # input: 1 -> 2 -> 3 -> None
            #
            # loop 1 BEFORE, previous: None, current: 1, next: 2
            # loop 1 AFTER, previous: 1, current: 2, next: 3
            #   1 -> None
            #
            # loop 2 BEFORE, previous: 1, current: 2, next: 3
            # loop 2 AFTER, previous: 2, current: 3, next: None
            #   2 -> 1 -> None
            #
            # loop 3 BEFORE, previous: 2, current: 3, next: None
            # loop 3 AFTER, previous: 3, current: None, next: None
            #   3 -> 2 -> 1 -> None
            #
            # output: 3 -> 2 -> 1 -> None
            tmp_next = current.next  # tmp_next = 2, 3, None
            current.next = previous  # 1.next = None, 2.next = 1, 3.next = 2
            previous = current  # new previous = 1, 2, 3
            current = tmp_next  # new next = 2, 3, None
        return previous

"""
Run time: O(n) to loop the list once.
Space: O(1) to store the pointers.
"""

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()

l2head = Solution().reverseList(ll.head)

while l2head:
    print(l2head.data, end=' -> ')
    l2head = l2head.next
print('None')

# approach 2: recursive
class Solution2:
    def reverseList(self, head: Node) -> Node:
        if not head:
            return None

        new_head = head
        if head.next: # there is still a next node.
            new_head = self.reverseList(head.next)
            head.next.next = head # actual reversing the node.
        head.next = None # set the first node's next to None.

        return new_head

"""
Run time: O(n) to loop the list once.
Space: O(n) to store the pointers.
"""