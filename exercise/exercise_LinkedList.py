

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.node_count = 0
        
        self.head = Node(None)
        self.tail = Node(None)

        self.head.prev = None
        self.head.next = self.tail

        self.tail.prev = self.head
        self.tail.next = None

    def __repr__(self):
        if self.node_count == 0:
            return "LinkedList is Empty!"

        comment = ""
        cur = self.head
        while cur.next.next:
            cur = cur.next
            comment += repr(cur.data)
            if cur.next.next is not None:
                comment += "->"

        return comment