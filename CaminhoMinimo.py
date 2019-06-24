from adjList import adjacencyList
import sys

class CaminhoMinimo:
    def __init__(self, grafo):
        self.graphList = adjacencyList(grafo)
        self.grafo = grafo

    def dijkstra(self, selectedVertex):
        vertices = self.grafo["vertices"].copy()
        weight = self.grafo["pesos"]
        distance = {}
        path = {}

        for v in vertices:
            distance[v] = sys.maxsize
            path[v] = None
        distance[selectedVertex] = 0

        while vertices:
            u = self.minDistance(distance, vertices)
            vertices.remove(u)

            for v in self.graphList.vertexNeighbours(u):
                selectedWeight = weight.get(v + u) or weight.get(u + v)
                if distance[v] > selectedWeight + distance[u]:
                    distance[v] = selectedWeight + distance[u]
                    path[v] = u
        return path, distance

    def floyd(self):
        CM = [[sys.maxsize for x in range(len(self.grafo["vertices"]))] for y in range(len(self.grafo["vertices"]))]

        for v in self.grafo["vertices"]: CM[self.translate(v)][self.translate(v)] = 0
        
        for e in self.grafo["arestas"]: 
            selectedWeight = self.grafo["pesos"].get(e[0] + e[1]) or self.grafo["pesos"].get(e[1] + e[0])
            CM[self.translate(e[0])][self.translate(e[1])] = selectedWeight
            CM[self.translate(e[1])][self.translate(e[0])] = selectedWeight

        for k in self.grafo["vertices"]:
            for i in self.grafo["vertices"]:
                if CM[self.translate(i)][self.translate(k)] < sys.maxsize:
                    for j in self.grafo["vertices"]:
                        CM[self.translate(i)][self.translate(j)] = min(CM[self.translate(i)][self.translate(j)], CM[self.translate(i)][self.translate(k)] + CM[self.translate(k)][self.translate(j)])
        return CM

    def minDistance(self, distance, vertices):
        vertexSelected = ''
        vertexWeightSelected = sys.maxsize
        for v in distance:
            if v in vertices and distance[v] <= vertexWeightSelected:
                vertexSelected = v
                vertexWeightSelected = distance[v]

        return vertexSelected

    def translate(self, value):
        return int(value) - 1