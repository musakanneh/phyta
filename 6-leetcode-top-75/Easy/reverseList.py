# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Reverse a singly linked list.
    https://leetcode.com/problems/reverse-linked-list/
    """

    def reverseList(self, head: ListNode):
        node = None

        while head is not None:
            next = head.next
            head.next = node
            node = head
            head = next

        return node
