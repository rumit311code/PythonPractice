"""
https://neetcode.io/problems/linked-list-cycle-detection/question

Linked List Cycle Detection

Given the beginning of a linked list head, return true if
there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list can be visited
again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists.
The tail node of the list will set it's next pointer to the index-th node.
If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:
Input: head = [1,2,3,4], index = 1 -> basically, 4's next is 2.
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], index = -1 -> basically 2's next is null.
Output: false

Constraints:

1 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"val: {self.val}->next: {self.next.val if self.next else None}"

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1 -> 2 -> 3 -> 4 -> 2 # True
        # 1 -> 2 -> None # False

        if not head:
            return False

        visited = set()
        current = head
        while current: # O(n) loop.
            print(f"visited: {visited}")
            if current.next in visited: # loop detected.
                print(f"loop detected at {current.next.val}")
                return True
            else:
                visited.add(current)
            current = current.next
        return False # no loops detected.

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1 -> 2 -> 3 -> 4 -> 2 # True
        # 1 -> 2 -> None # False
        # slow -> jumps one node
        # fast -> jumps two nodes
        # Floyd's Tortoise and Hare algorithm.
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # when fast matches slow, it's a loop.
                return True
        return False # no loops detected.
"""
Run time: O(n) to loop the list once.
Space: O(n) to store the visited set.
"""