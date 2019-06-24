class vertexObj:
    def __init__(self, vertexName):
        self.vertexName = vertexName
        self.next = None

class adjacencyList:
    def __init__(self, graph):
        self.adjList = {}

        for n in graph["vertices"]:
            self.addVertex(n)

        for m in graph["arestas"]:
            if not self.addEdge(m) : print("aresta não existe")

    def addNeighbour(self, vertex, neighbour):
        neighbour = vertexObj(neighbour)
        if self.adjList[vertex] is None:
            self.adjList[vertex] = neighbour
            return

        currentNode = self.adjList[vertex]
        while True:
            if currentNode.next is None: 
                currentNode.next = neighbour 
                break
            currentNode = currentNode.next

    def removeNeighbour(self, vertex, neighbour):
        if self.adjList[vertex] is None:  return False

        if self.adjList[vertex].vertexName == neighbour:
            self.adjList[vertex] = self.adjList[vertex].next
            return True
        
        currentNode = self.adjList[vertex]
        while True:
            if currentNode.next is None:
                return True
            elif currentNode.next.vertexName == neighbour:
                currentNode.next = currentNode.next.next
                return True

            currentNode = currentNode.next

    def addEdge(self, edge):
        if edge[0] not in self.adjList or edge[1] not in self.adjList:  return False
        
        self.addNeighbour(edge[0], edge[1])
        self.addNeighbour(edge[1], edge[0])

        return True

    def removeEdge(self, edge):
        if edge[0] not in self.adjList or edge[1] not in self.adjList:  return False

        return self.removeNeighbour(edge[0], edge[1]) and self.removeNeighbour(edge[1], edge[0])
    
    def addVertex(self, vertex):
        self.adjList[vertex] = None

    def removeVertex(self, vertex):
        if vertex not in self.adjList: return False

        if self.adjList[vertex] is None:
            self.adjList.pop(vertex)
            return True

        ok = True

        currentNode = self.adjList[vertex]
        while currentNode is not None:
            if ok: 
                ok = self.removeNeighbour(currentNode.vertexName, vertex)
                currentNode = currentNode.next
            else:
                self.removeNeighbour(currentNode.vertexName, vertex)
                currentNode = currentNode.next

        self.adjList.pop(vertex)
        return ok

    def vertexNeighbours(self, vertex):
        neighbours = []
        if vertex not in self.adjList:  return neighbours

        if self.adjList[vertex] is None:  return neighbours

        currentNode = self.adjList[vertex]
        while True:
            if currentNode.next is None:
                neighbours.append(currentNode.vertexName)
                return neighbours
            else:
                neighbours.append(currentNode.vertexName)
                currentNode = currentNode.next

    def printList(self):
        for key, value in self.adjList.items():
            print('vertice = ' + key)

            currentNode = value
            while currentNode is not None:
                print('    vizinho de ' + key + ' = ' + currentNode.vertexName)
                currentNode = currentNode.next