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
    
    def compare(self, parent, child):
        if parent == None or child == None:
            return True
        else:
            return parent.key <= child.key

    def insert(self, key, value):
        index = len(self.data)
        newNode = Node(key, value, index)
        self.data.append(newNode)
        self.heapifyUp(newNode)

    def heapifyUp(self, node):  
        while not self.compare(self.getParent(node), node):
            self.swap(node, self.getParent(node))
            #print(self.getParent(node))
       
    #def heapifyDown(self, node):
    #    while True:

    def extract(self, node):
        root = self.data[0]
        last = self.data.pop()
        self.data[0] = last

        ##heapify down

        return root.value


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

h = BinaryHeap()

h.insert(1, "A") #1,1
h.insert(2, "B") #1,2

h.insert(4, "C") #2,1
h.insert(5, "D") #2,2  
h.insert(1, "E") #root

print(h)
root = h.data[0]
print(root)
print(h.getParent(root))

