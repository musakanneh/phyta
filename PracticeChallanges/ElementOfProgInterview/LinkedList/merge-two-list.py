class ListNode:
    def __init__(self, head):
        self.head = head
        self.next = None


class MergeTwoLists(object):
    def __init__(self):
        pass

    def merge_two_list(self, head1, head2):
        def node_count(head):
            """
            Gets the count of node  in the list
            """
            count = 0
            while head != None:
                head = head.next
                count += 1
            return count

        def common_node(d, head1, head2):
            """
            Finds the list intersection
            and returns the common data
            """
            for i in range(d):
                head1 = head1.next
            while head1 and head2:
                if head1 == head2:
                    return head1.data
                head1 = head1.next
                head2 = head2.next

            c1 = node_count(head1)
            c2 = node_count(head2)
            
            if c1 > c2:
                return common_node(c1 - c2, head1, head2)
            return common_node(c2 - c1, head2, head1)


l_list = MergeTwoLists()
print(l_list)
