#!/usr/bin/python3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        curr = ListNode(0)
        ans = curr

        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next

            curr = curr.next

        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next

        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

        return ans.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
print(Solution().mergeTwoLists(l1, l2))
