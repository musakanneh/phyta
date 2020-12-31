class SinglyLinkedListNode(self, node_data):
    def __init__(self, node):
        self.node = node
        self.next = None


class SinglyLinkedList(self):
    def __init__(self):
        self.head = head
        self.tail = None

    def insert_node(self, node_data):
        pass

    def insert_node_at_pos(self, head, data, position):
        if head == None:
            head = self.node
        else:
            temp = head
            count = 0
            while temp != None and count < position:
                temp = temp.next
                count += 1
            node.next = temp.next
            temp.next = self.node
        return head

    def sortedInsert(self, head, data):
        pass
