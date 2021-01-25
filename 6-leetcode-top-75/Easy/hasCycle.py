# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """Given head, the head of a linked list, 
    determine if the linked list has a cycle in it.
    
    https://leetcode.com/problems/linked-list-cycle/
    
    """

    def hasCycle(self, head: ListNode):
        hare = head
        turtle = head

        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next

            if turtle == hare:
                return True

        return False
