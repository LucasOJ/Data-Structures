class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail
        self.length = 0

    def display(self):
        node = self.head.next
        values = []
        while node.next != None:
            values.append(node.value)
            node = node.next
        return values
    
    def enqueue(self, value):
        first = self.head.next
        
        newNode = Node(value, self.head, first)
        
        self.head.next = newNode
        first.prev = newNode

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise Exception("Queue empty - nothing to dequeue")
        nodeValue = self.tail.prev.value
        prevNode = self.tail.prev.prev

        prevNode.next = self.tail
        self.tail.prev = prevNode
        
        self.length -=1 

        return nodeValue

    def isEmpty(self):
        return self.length == 0

class Stack:
    def __init__(self):
        self.values = []
    
    def push(self, value):
        self.values.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack empty - nothing to pop")
        return self.values.pop()
    
    def isEmpty(self):
        return len(self.values) == 0

class Graph:
    def __init__(self, vertexNum=0):
        self.adjList = [[] for i in range(vertexNum)]
        self.vertexNum = vertexNum

    def addDirectedEdge(self,fromVertex, toVertex):
        self.adjList[fromVertex].append(toVertex)

    def addEdge(self, vertexA, vertexB):
        self.addDirectedEdge(vertexA, vertexB)
        self.addDirectedEdge(vertexB, vertexA)

    def getNeighbors(self, vertex):
        return self.adjList[vertex]

    def BFS(self, startVertex):
        self.visited = [False for i in range(self.vertexNum)]
        visitList = []
        queue = Queue()
        queue.enqueue(startVertex)
        while not queue.isEmpty():
            node = queue.dequeue()
            if not self.visited[node]:
                visitList.append(node)
                self.visited[node] = True
                for neighbor in self.getNeighbors(node):
                    if not self.visited[neighbor]:
                        queue.enqueue(neighbor)

        return visitList

    #Proccesses in reverse adjacency list order
    def DFS(self, startVertex):
        visited = [False for i in range(self.vertexNum)]
        visitList = []
        stack = Stack()
        stack.push(startVertex)
        while not stack.isEmpty():
            node = stack.pop()
            if not visited[node]:
                visitList.append(node)
                visited[node] = True
                for neighbor in self.getNeighbors(node):
                    if not visited[neighbor]:
                        stack.push(neighbor)

        return visitList

    def rDFSCore(self, vertex, visited, path):
        visited[vertex] = True
        path.append(vertex)
        for neighbor in self.getNeighbors(vertex):
            if not visited[neighbor]:
                self.rDFSCore(neighbor, visited, path)

    #Processes in adjacency list order
    def rDFS(self, startVertex): 
        path = []
        initialVisited = [False for i in range(self.vertexNum)]
        self.rDFSCore(startVertex, initialVisited, path)
        return path

    def connectedComponents(self):
        visited = [False for i in range(self.vertexNum)]
        components = []
        for node in range(self.vertexNum):
            if not visited[node]:
                component = self.DFS(node)
                for node in component: visited[node] = True
                components.append(component)

        return components

    def cycleTraverse(self, vertex, state):
        state[vertex] = "GREY"

        for neighbor in self.getNeighbors(vertex):
            if state[neighbor] == "GREY":
                return True
            elif state[neighbor] == "WHITE" and self.cycleTraverse(neighbor, state):
                return True

        state[vertex] = "BLACK"

        return False

    def containsCycle(self):
        state = ["WHITE" for i in range(self.vertexNum)]
        for vertex in range(self.vertexNum):
            if state[vertex] == "WHITE":
                if self.cycleTraverse(vertex, state):
                 
                    return True
        return False


g = Graph(10)
g.addEdge(1,2)
g.addEdge(0,3)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(4,6)
g.addEdge(1,0)

print(g.adjList)
print(g.connectedComponents())

