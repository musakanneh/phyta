class LinkedList:
    def __init__(self, data=0, next_node=0):
        self.data = data
        self.next_node = next_node

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
        """
        Reverse e
        """
        pass


new_node = LinkedList("M")
