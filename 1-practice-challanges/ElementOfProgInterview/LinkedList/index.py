class ListNode:
    def __init__(self, data=0, next_node=0):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, head):
        self.head = None

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.data)
            temp_node = temp_node.next

    def delete_node(self, node, position):
        node.next = node.next.next
        return node

    def search_list(self, head, key):
        while head and head.data != key:
            head = head.next
        return head

    def insert_node_after(self, node, new_node):
        node_node = node.next
        node.next = new_node

    def delete_node(self, node):
        node.next = node.next.next

    def merge_two_sorted_list(self, list_one, list_two):
        temp_head = tail = ListNode()
        while list_one and list_two:
            if list_one.data < list_two.data:
                tail.next, list_one = list_one, tail.next
            else:
                tail.next, list_two = list_two, tail.next
            tail = tail.next
        tail.next = list_one or list_two
        return temp_head.next


if __name__ == '__main__':
    _linked_list1 = LinkedList()
    _linked_list.head = ListNode(1)
    _linked_list.head.next = ListNode(6)
    _linked_list.head.next.next = ListNode(7)
    _linked_list.print_list(ListNode)
