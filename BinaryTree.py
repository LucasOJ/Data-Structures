class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inOrderTraverse(self, node, visited):
        if not (node is None):
            self.inOrderTraverse(node.leftChild, visited)
            visited.append(node.value)
            self.inOrderTraverse(node.rightChild, visited)

    def inOrderTraversal(self):
        visited = []
        self.inOrderTraverse(self.root, visited)
        return visited

class BinarySearchTree(BinaryTree):
    def __init__(self):
        super().__init__()

    def insertTraverse(self, value, node):
        if node is None:
            return Node(value)
        
        if value < node.value:
            node.leftChild = self.insertTraverse(value, node.leftChild)
        elif value > node.value:
            node.rightChild = self.insertTraverse(value, node.rightChild)
        
        return node
        
    def insert(self, value):
        self.root = self.insertTraverse(value, self.root)

    def searchTraverse(self, value, node) :
        if node is None: return False

        if node.value == value:  return True
        
        elif value < node.value: return self.searchTraverse(value, node.leftChild)
        elif value > node.value: return self.searchTraverse(value, node.rightChild)
    
    def search(self, value):
        return self.searchTraverse(value, self.root)

a = BinarySearchTree()
a.insert(4)
a.insert(2)
a.insert(5)
a.insert(7)
a.insert(1)
print(a.inOrderTraversal())
print(a.search(3))
print(a.search(7))