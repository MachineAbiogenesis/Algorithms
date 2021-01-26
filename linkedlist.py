class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add_node_front(self, val):
        new_node = Node(val)                # create new node with value
        new_node.next = self.head           # point new node next to existing node (adding at start )
        self.head = new_node                # move head pointer to start of list as new node is first node

    def add_node_back(self, val):
        new_node = Node(val)
        current = self.head                 # do not change head of list create new pointer
        while current.next is not None:     # and traverse list till last node
            current = current.next
        current.next = new_node  # assign last node next to new node


link = LinkedList()

link.add_node_front("First")
link.add_node_front("Second")
link.add_node_front("Third")

link.add_node_back("Secondback")

link.show()
