class node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doubly_list:

    def __init__(self):
        self.head = None

    def insert_head(self, new_node):
        self.head = new_node
        self.head.next = new_node.next
        self.head.prev = new_node.prev

    # Insert At end
    def insert_at_begin(self, new_node):
        if self.head == None:
            self.insert_head(new_node)

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert Node at end
    def insert_at_end(self, new_node):
        if self.head == None:
            self.insert_head(new_node)
        else:
            current_node = self.head
            while (current_node.next):
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    # insert after specific node

    def insert_after_spec_node(self, val, new_node):
        current_node = self.head
        while current_node.data != val:
            current_node = current_node.next
        if current_node.next==None:
            self.insert_at_end(new_node)
            return
        next_node = current_node.next
        current_node.next = new_node
        new_node.next = next_node

        next_node.prev = new_node
        new_node.prev = current_node

    # delete_at_beginning
    def delete_at_beginning(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
            self.head.prev = None

    # delete at end
    def del_at_end(self):
        current_node = self.head
        while (current_node.next):
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None
        current_node.prev = None

    # delete node having given data
    def del_spec_node(self, data):
        current_node = self.head
        prev_node = current_node
        next_node = None
        while current_node:
            if current_node.data == data:
                if current_node.prev == None:
                    self.delete_at_beginning()
                    break

                if current_node.next == None:
                    self.del_at_end()
                    break

                next_node = current_node.next
                prev_node.next = next_node
                next_node.prev = prev_node
                break
            else:
                prev_node = current_node
                current_node = current_node.next

    def display(self):
        current_node = self.head
        print("Forward dir :", end="")
        while (current_node):
            print(current_node.data, end='-->')
            prev_node = current_node
            current_node = current_node.next
        print()



doubly_linkedlist = doubly_list()
print("Insert At Begin")
doubly_linkedlist.insert_at_begin(node(13))
doubly_linkedlist.insert_at_begin(node(12))
doubly_linkedlist.insert_at_begin(node(11))
doubly_linkedlist.insert_at_begin(node(10))
doubly_linkedlist.display()

print("\ninsert_at_end")
doubly_linkedlist.insert_at_end(node(14))
doubly_linkedlist.display()

print("\ninsert_after_spec_node")
doubly_linkedlist.insert_after_spec_node(11, node(11.5))
doubly_linkedlist.display()

print("\n delete at beginning ")
doubly_linkedlist.delete_at_beginning()
doubly_linkedlist.display()

print("\n delete node having given data")
doubly_linkedlist.del_spec_node(11.5)
doubly_linkedlist.display()

'''
Insert At Begin
Forward dir :10-->11-->12-->13-->

insert_at_end
Forward dir :10-->11-->12-->13-->14-->

insert_after_spec_node
Forward dir :10-->11-->11.5-->12-->13-->14-->

 delete at beginning 
Forward dir :11-->11.5-->12-->13-->14-->

 delete node having given data
Forward dir :11-->12-->13-->14-->

'''