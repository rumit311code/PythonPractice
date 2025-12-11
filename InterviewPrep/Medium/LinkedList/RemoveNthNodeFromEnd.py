"""
https://neetcode.io/problems/remove-node-from-end-of-linked-list/question

Video: https://www.youtube.com/watch?v=XVuQxVej6y8

Remove Node From End of Linked List

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]

Example 2:
Input: head = [5], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 2
Output: [2]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4 -> 5 -> None
        # n=2 (remove 4)
        dummy = ListNode(0, head) # dummy.next -> 1

        # go to the end of the linked list
        left = dummy # left = 0
        right = head # right = 1
        while right and n > 0: # O(len(linked list) - n)
            right = right.next
            n -= 1

        # left=0, right=2 before the loop
        while right: # O(n)
            left = left.next
            right = right.next
        # left=3, right=None after the loop

        # Left = 3 after both while loops. So left.next.next = 5
        # 1 -> 2 -> 3 -> 5 -> None
        left.next = left.next.next # 4 removed.
        return dummy.next # points to 1.

"""
Runtime: O(len(linked list)) - O(n) + O(n) = O(len(linked list)) to iterate over entire list
Space: O(n) to store dummy
"""