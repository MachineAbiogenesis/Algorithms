# Binary Tree With Inorder , PreOrder , Post order  Traversal
class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, val):
        if self.data == val:
            return

        if self.data > val:
            if self.left:
                self.left.add_child(val)
            else:
                self.left = BinarySearchTree(val)

        else:
            if self.right:
                self.right.add_child(val)
            else:
                self.right = BinarySearchTree(val)

    def inorder_traversal(self):
        elements = []
        # visit Left Tree
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()

        return elements
    
    def preorder_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.preorder_traversal()

        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def postorder_traversal(self):
        elements = []

        if self.left:
            elements += self.left.postorder_traversal()

        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements


if __name__ == '__main__':
    numbers = [55, 3, 5, 7, 3, 6, 8, 9, 4, 31, 12, 1231, 6, 76]
    tree = BinarySearchTree(numbers[0])
    # Build Tree
    for i in range(1, len(numbers)):
        tree.add_child(numbers[i])

    inorderTraversal = tree.inorder_traversal()
    print("Inorder Traversal", inorderTraversal)

    preorderTraversal = tree.preorder_traversal()
    print("Preorder Traversal", preorderTraversal)

    postorderTraversal = tree.postorder_traversal()
    print("Postorder Traversal", postorderTraversal)

'''
Inorder Traversal [3, 4, 5, 6, 7, 8, 9, 12, 31, 55, 76, 1231]
Preorder Traversal [55, 3, 5, 4, 7, 6, 8, 9, 31, 12, 1231, 76]
Postorder Traversal [4, 6, 12, 31, 9, 8, 7, 5, 3, 76, 1231, 55]

'''