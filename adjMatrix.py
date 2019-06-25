class adjacencyMatrix:
    def __init__(self, graph):
        self.vertices = graph["vertices"]
        self.n = len(self.vertices)    
        self.adjMatrix = [[0 for x in range(self.n)] for y in range(self.n)]  #iniciando uma matriz n x n com zeros

        for m in graph["arestas"]:
            edge1, edge2 = m[0], m[1]
            i, j = self.vertices.index(edge1), self.vertices.index(edge2)
            self.adjMatrix[i][j] = self.adjMatrix[j][i] = 1

    def addVertex(self, vertex):
        if vertex in self.vertices:
            return False
                
        self.vertices.append(vertex)
        self.n = len(self.vertices)

        for n in self.adjMatrix: n.append(0)
        self.adjMatrix.append([0 for x in range(self.n)])
        return True

    def removeVertex(self, vertex):
        if vertex not in self.vertices:
            return False

        index = self.vertices.index(vertex)
        self.vertices.remove(vertex)
        self.n = len(self.vertices)

        for n in self.adjMatrix:
            n.pop(index)
        self.adjMatrix.pop(index)

        return True

    def editEdge(self, edge, add): #se add == true, adiciona a aresta, caso contrário a funcão remove a mesma aresta
        if edge[0] not in self.vertices or edge[1] not in self.vertices:
            return False
        
        i, j = self.vertices.index(edge[0]), self.vertices.index(edge[1])

        self.adjMatrix[i][j] = self.adjMatrix[j][i] = 1 if add else 0

        return True

    def vertexNeighbours(self, vertex):
        neighbours = []
        if vertex not in self.vertices:
            return neighbours

        i = self.vertices.index(vertex)
        for j in range(len(self.adjMatrix[i])):
            if self.adjMatrix[i][j] == 1: neighbours.append(self.vertices[j])

        return neighbours

    def printMatrix(self):
        print(self.vertices)
        for i in self.adjMatrix: print(i)
            
