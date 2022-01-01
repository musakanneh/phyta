#!/usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def has_cycle(self, head):
        hare = head
        turtle = head
        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                return True
        return False


head = [1, 2]
print(Solution().has_cycle(head))
