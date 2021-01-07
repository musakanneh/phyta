class ListNode:
    def __init__(self, head):
        self.head = head
        self.next = None


class MergeSortedList(object):
    def __init__(self):
        pass

    def merge_sorted_list(self, list_1, list_2):
        """
        Traverse the list; always choose the
        node containing the smaller key to 
        continue traversing 
        """
        temp_head = tail = ListNode()
        while list_1 and list_2:
            if list_1.data < list_2.data:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next
            tail = tail.next
        tail.next = list_1 or list_2
        return temp_head

    def merger_doubly_linkedlist(self, list_1, list_2):
        pass


l_list = MergeSortedList()
print(l_list)
