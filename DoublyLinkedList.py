class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextNode = None
        self.prevNode = None
        self.isEndNode = False

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.isEndNode = True
        self.tail.isEndNode = True

        self.head.nextNode = self.tail
        self.tail.prevNode = self.head

        self.length = 0

    def newNode(self, value):
        self.length += 1
        return Node(value)

    def addNodeAfter(self, node, value):
        leftNode = node
        rightNode = leftNode.nextNode
        
        newNode = self.newNode(value)

        leftNode.nextNode = newNode
        rightNode.prevNode = newNode

        newNode.prevNode = leftNode
        newNode.nextNode = rightNode
        
    def addFirst(self, value):
        self.addNodeAfter(self.head, value)

    def addLast(self, value):
        self.addNodeAfter(self.tail.prevNode, value)

    #INVARIANT : <LinkedList>.getNode(x).value = x
    def getNode(self, value):
        node = self.head.nextNode
        while node.nextNode != None:
            if node.value == value:
                return node
            node = node.nextNode
        raise Exception('No element with value {}'.format(value))

    def addAfter(self, newValue, searchValue):
        node = self.getNode(searchValue)
        self.addNodeAfter(node, newValue)

    def addBefore(self, newValue, searchValue):
        node = self.getNode(searchValue)
        self.addNodeAfter(node.prevNode, newValue)

    def removeNode(self, node):
        if node.isEndNode: raise Exception('No element to remove')

        leftNode  = node.prevNode
        rightNode = node.nextNode

        leftNode.nextNode = rightNode
        rightNode.prevNode = leftNode

        self.length -= 1

    def removeFirst(self):
        self.removeNode(self.head.nextNode)

    def removeLast(self):
        self.removeNode(self.tail.prevNode)

    def remove(self, value):
        node = self.getNode(value)
        self.removeNode(node)

    def __str__(self):
        node = self.head.nextNode
        outputList = []
        while not node.isEndNode:
            outputList.append(str(node.value))
            node = node.nextNode
        return str(outputList)
    
    def __repr__(self):
        return self.__str__()
