class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    # Insert node In Tree
    def add_node(self, val):
        if self.data == val:
            return
        if val < self.data:
            if self.left:
                self.left.add_node(val)
            else:
                self.left = Node(val)
        else:
            if self.right:
                self.right.add_node(val)
            else:
                self.right = Node(val)

    # Searching Node
    def search_node(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            if self.left:
                return self.left.search_node(value)
            else:
                return False
        elif self.right:
            return self.right.search_node(value)
        else:
            return False

    # Delete node

    def delete_node(self, value):
        # Return if the tree is empty
        if self is None:
            return self

        # Find the node to be deleted
        if value < self.data:
            self.left = self.left.delete_node(value)
        elif (value > self.data):
            self.right = self.right.delete_node(value)
        else:
            # If the node is with only one child or no child
            if self.left is None:
                temp=self.right
                self=None
                return temp

            elif self.right is None:
                temp=self.left
                self=None
                return temp

            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            minval = self.right.find_min()

            self.data = minval

            # Delete the inorder successor
            self.right = self.right.delete_node(minval)

        return self

    def find_max(self):
        if self.right:
            self.right.find_min()
        return self.right.data

    def find_min(self):
        if self.left:
            self.left.find_min()
        return self.left.data


if __name__ == '__main__':
    numbers = [8, 4, 10, 1, 6, 14, 7]

    tree = Node(8)
    for i in numbers:
        tree.add_node(i)

    print("Search Node with value 9:", tree.search_node(9))
    print("Search Node with value 55:", tree.search_node(55))
    print("Search Node with value 5:", tree.search_node(5))

    print("Search Node with value 10:", tree.search_node(10))
    tree.delete_node(10)
    print("Deleted node 10 Search Node with value 10 :", tree.search_node(10))

'''
Search Node with value 9: False
Search Node with value 55: False
Search Node with value 5: False
Search Node with value 10: True
Deleted node 10 Search Node with value 10 : False
'''