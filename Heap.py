class Node:
    def __init__(self, key, value, index):
        self.key = key
        self.value = value
        self.index = index

    def __str__(self):
        return str((self.key, self.value, self.index))

    def __repr__(self):
        return self.__str__()

class BinaryHeap:
    def __init__(self):
        self.data = []
        self.comparator = lambda parent, child : parent <= child
    
    def compare(self, parent, child):
        if parent == None or child == None:
            return True
        else:
            return self.comparator(parent.key, child.key)

    def insert(self, key, value):
        index = len(self.data)
        newNode = Node(key, value, index)
        self.data.append(newNode)
        self.heapifyUp(newNode)

    def heapifyUp(self, node):  
        while not self.compare(self.getParent(node), node):
            self.swap(node, self.getParent(node))
       
    def heapifyDown(self, node):
        while True:
            leftChild = self.getLeftChild(node)
            rightChild = self.getRightChild(node)

            leftNodeValid = self.compare(node, self.getLeftChild(node))
            rightNodeValid = self.compare(node, self.getRightChild(node))

            if leftChild == None:
                break
            elif rightChild == None and leftNodeValid:
                break
            elif rightChild == None and not leftNodeValid:
                self.swap(node, leftChild)
            elif leftNodeValid and rightNodeValid:
                break
            else:
                if self.compare(leftChild, rightChild):
                    self.swap(node, leftChild)
                else:
                    self.swap(node, rightChild)

    def extract(self):
        root = self.data[0]
        last = self.data[-1]
        self.swap(root, last)
        significantNode = self.data.pop()

        self.heapifyDown(last)

        return significantNode.value


    def swap(self, node1, node2):
        node1Index = node1.index
        node2Index = node2.index

        node1.index = node2Index
        node2.index = node1Index

        self.data[node1.index] = node1
        self.data[node2.index] = node2

    def getLeftChild(self, node):
        i = 2 * node.index + 1
        return self.getNode(i)

    def getRightChild(self, node):
        i = 2 * node.index + 2
        return self.getNode(i)

    def getNode(self, index):
        if 0 <= index and index < len(self.data):
            return self.data[index]
        else:
            return None

    def getParent(self, node):
        i = (node.index - 1) // 2
        return self.getNode(i)

    def __str__(self):
        return str([str(node) for node in self.data])
    
    def __repr__(self):
        return self.__str__()
