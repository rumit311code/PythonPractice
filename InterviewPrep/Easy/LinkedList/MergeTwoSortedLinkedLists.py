"""
https://neetcode.io/problems/merge-two-sorted-linked-lists/question

Video: https://www.youtube.com/watch?v=XIdigk956u0

Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and
return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]

Example 2:
Input: list1 = [], list2 = [1,2]
Output: [1,2]

Example 3:
Input: list1 = [], list2 = []
Output: []

Constraints:

0 <= The length of the list <= 100.
-100 <= Node.val <= 100
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"val: {self.val}->next: {self.next.val if self.next else None}"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2: # O(n)
            if list1.val <= list2.val: # list1 val is smaller
                tail.next = list1
                list1 = list1.next
            else: # list2 val is smaller
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1: # add all remaining elements from list1.
            tail.next = list1
        elif list2: # add all remaining elements from list1.
            tail.next = list2

        return dummy.next # dummy.next is the head of the sorted linked list.

"""
n is length of the larger list.

Runtime: O(n). 
Space: O(n) to store dummy.
"""