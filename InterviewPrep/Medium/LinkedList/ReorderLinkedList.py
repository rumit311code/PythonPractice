"""
https://neetcode.io/problems/reorder-linked-list/question

Video: https://www.youtube.com/watch?v=S5bfdUTrKLM

Reorder Linked List

You are given the head of a singly linked-list.

The positions of a linked list of length = 7
for example, can initially be represented as: [0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n
the nodes are reordered to be in the following order: [0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes,
but instead you must reorder the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1->2->3->4->5
        # slow = 1, fast = 2
        slow, fast = head, head.next

        while fast and fast.next: # O(n)
            slow = slow.next
            fast = fast.next.next
        # slow = 3, fast = None
        # after this loop, slow will be at the half point of the list.
        # slow.next will be the head of the 2nd half.

        second = slow.next # second = 4
        slow.next = None # 3.next = None
        prev = None
        # reverse second half of the list.
        # change 4->5->None to 5->4->None
        while second: # O(n)
            tmp = second.next # tmp = 5, None
            second.next = prev # 4.next = None, 5.next = 4
            prev = second # prev = 4, 5
            second = tmp # second = 5, None

        # new head of the second half = prev = 5.
        # merge two halves
        first, second = head, prev # first=1, second=5
        while second: # O(n)
            tmp1, tmp2 = first.next, second.next
            # tmp1 = 2,3,None
            # tmp2 = 5,4,None
            first.next = second
            # 1.next = 5
            # 2.next = 4
            # 3.next = None
            second.next = tmp1
            # 5.next = 2
            # 4.next = 3
            first, second = tmp1, tmp2
            # first = 2,3,None
            # second = 5,4,None

        # final: 1->5->2->4->3->None
