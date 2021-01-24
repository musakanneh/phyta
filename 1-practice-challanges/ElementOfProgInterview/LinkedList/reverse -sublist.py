class ListNode:
    def __init__(self, head):
        self.head = head
        self.next = None


class ReverseSublist(object):
    def __init__(self):
        pass

    def reverse_sublist(self, start, finish):
        """
        Extract the sublist, reverse it, and splice it back in. 
        To ensure a single pass, we combine the indentifications of the sublist
        with its reversal, by using an interaction to the sth node and its 
        it predecessor. Once we reach the sth node, we stop the reversion procese
        and linked the reverted section with the unreverted section.
        """
        temp_head = sublist_head = ListNode(0, l_list)
        for _ in range(1, start):
            sublist_head = sublist_head.next
        sublist_itr = sublist_head.next
        for _ in range(finish - start):
            temp_node = sublist_itr.next
            sublist_itr.next = temp_node.next
            temp_node.next = sublist_head.next
            sublist_head.next = temp_node
        return temp_head.next

    def reverse_singly_linkedlist(self, head):
        """
        """
        pass

    def reverse_doubly_linkedlist(self, head):
        """
        """
        while head.next != None:
            head.next, head.prev, head = head.prev, head.next, head.next
        head.next, head.prev = head.next, None
        return head


l_list = ReverseSublist()
print(l_list)
