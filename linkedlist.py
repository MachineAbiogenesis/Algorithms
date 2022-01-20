# Linked List
# node will give address of current node
# node.data will give current node data
# node.next will give address of next node

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None

    # insert Node at end
    def insertNode(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            currentNode = self.head
            while (currentNode.next):
                currentNode = currentNode.next
            currentNode.next = newNode

    # Insert Node At Begin
    def insertAtbegin(self, newNode):
        newNode.next = self.head
        self.head = newNode

    # print Current Linked list
    def dispayList(self):
        currentPoint = self.head
        while currentPoint:
            print(str(currentPoint.data), end="-->")
            currentPoint = currentPoint.next
        print()

    # delete after specific node
    def insert_after_specific_node(self, nodeVal, newNode):
        cureentNode = self.head
        while cureentNode:
            if cureentNode.data == nodeVal:
                newNode.next = cureentNode.next
                cureentNode.next = newNode
                break
            cureentNode = cureentNode.next

    # delete at beginning
    def delete_at_begin(self):
        self.head = self.head.next

    # delete at end:
    def delete_at_end(self):
        current_node = self.head
        while (current_node.next):
            prev_node = current_node
            current_node = current_node.next
        prev_node.next = None

    # delete after specific node
    def del_after_spec(self, val):
        currentNode = self.head
        while currentNode:
            if currentNode.data == val:
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                break
            else:
                currentNode = currentNode.next


newList = linkedList()
newList.insertNode(node(9))
newList.insertNode(node(10))
newList.insertNode(node(11))
newList.insertNode(node(12))
newList.insertNode(node(13))
newList.insertNode(node(14))
newList.dispayList()
print("Insert At Beginning ")
newList.insertAtbegin(node(15))
newList.dispayList()

print("\ninsert_after_specific_node 11 ")
newList.insert_after_specific_node(11, node(11.5))
newList.dispayList()

print("\ndelete_at_begin ")
newList.delete_at_begin()
newList.dispayList()

print("\ndelete_at_end ")
newList.delete_at_end()
newList.dispayList()

print("\ndel_after_spec node 11 ")
newList.del_after_spec(11)
newList.dispayList()

"""
9-->10-->11-->12-->13-->14-->
Insert At Beginning 
15-->9-->10-->11-->12-->13-->14-->

insert_after_specific_node 11 
15-->9-->10-->11-->11.5-->12-->13-->14-->

delete_at_begin 
9-->10-->11-->11.5-->12-->13-->14-->

delete_at_end 
9-->10-->11-->11.5-->12-->13-->

del_after_spec node 11 
9-->10-->11-->12-->13-->

"""
