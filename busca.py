from adjList import adjacencyList
from collections import deque
import sys

class busca:
    def lerAresta(self, a):
        return str(a[0]) + str(a[1])

    def __init__(self, grafo):
        self.visitado = {}
        self.explorado = {}
        self.descoberto = {}
        self.distancia = {}

        for v in grafo["vertices"]:
            self.visitado[v] = False
            self.distancia[v] = False
            for w in grafo["vertices"]:
                self.explorado[v + w] = False
                self.descoberto[v + w] = False

    def busca(self, grafo, vertice):
        self.visitado[vertice] = True

        for a in grafo["arestas"]:
            if self.visitado[a[0]] and not self.explorado[self.lerAresta(a)]:
                self.explorado[self.lerAresta(a)] = True
                if not self.visitado[a[1]]:
                    self.visitado[a[1]] = True
                    self.descoberto[self.lerAresta(a)] = True

    def buscaUnica(self, grafo):
        for v in grafo["vertices"]:
            self.visitado[v] = False

        for a in grafo["arestas"]:
            self.explorado[self.lerAresta(a)] = False
            self.descoberto[self.lerAresta(a)] = False

        self.busca(grafo, grafo["vertices"][1])

    def buscaCompleta(self, grafo):
        for v in grafo["vertices"]:
            if not self.visitado[v]:
                self.busca(grafo, v)

    def ehConexo(self, grafo):
        self.buscaUnica(grafo)
        for v in grafo["vertices"]:
            if not self.visitado[v]:
                return False
        return True

    def temCiclo(self, grafo):
        self.buscaCompleta(grafo)
        for a in grafo["arestas"]:
            if not self.descoberto[self.lerAresta(a)]:
                return True
        return False

    def ehFloresta(self, grafo):
        return not self.temCiclo(grafo)

    def ehArvore(self, grafo):
        self.buscaUnica(grafo)
        for v in grafo["vertices"]:
            if not self.visitado[v]:
                return False
        for a in grafo["arestas"]:
            if not self.descoberto[self.lerAresta(a)]:
                return False
        return True

    def ehArvoreShort(self, grafo):
        return self.ehConexo(grafo) and not self.temCiclo(grafo)

    def obterFlorestaGeradora(self, grafo):
        t = {}

        t["vertices"] = grafo["vertices"]
        t["arestas"] = []

        self.buscaCompleta(grafo)

        for a in grafo["arestas"]:
            if self.descoberto[self.lerAresta(a)]:
                t["arestas"].append(a)

        return t

    def primeiroVizinho(self, grafo, vertice):
        neighbours = adjacencyList(grafo).vertexNeighbours(vertice)
        return neighbours[0]

    def proximoVizinho(self, grafo, vertice, vizinhoAtual):
        neighbours = adjacencyList(grafo).vertexNeighbours(vertice)
        return neighbours[neighbours.index(vizinhoAtual) + 1]

    def buscaProfundidade(self, grafo, vertice):
        pilha = []
        self.visitado[vertice] = True
        pilha.append(vertice), pilha.append(self.primeiroVizinho(grafo, vertice))

        while len(pilha) > 0:
            w = pilha.pop() if pilha else False
            v = pilha.pop() if pilha else False

            if w is not False:
                pilha.append(v), pilha.append(self.proximoVizinho(grafo, v, w))
                if self.visitado[w]:
                    if not self.explorado[v + w]:
                        self.explorado[v + w] = True
                else:
                    self.explorado[v + w], self.descoberto[v + w], self.visitado[w] = True, True, True
                    pilha.append(w), pilha.append(self.primeiroVizinho(grafo, w))
                    
    def buscaProfundidadeRec(self, grafo, vertice):
        self.visitado[vertice] = True
        neighbours = adjacencyList(grafo).vertexNeighbours(vertice)

        for w in neighbours:
            if self.visitado[w]:
                if not self.explorado[vertice + w]:
                    self.explorado[vertice + w] = True
            else:
                self.explorado[vertice + w], self.descoberto[vertice + w] = True, True
                self.buscaProfundidadeRec(grafo, w)

    def buscaLargura(self, grafo, vertice):
        fila = deque()
        self.visitado[vertice] = True
        fila.append(vertice)

        while len(fila) > 0:
            v = fila.popleft()
            neighbours = adjacencyList(grafo).vertexNeighbours(v)

            for w in neighbours:
                if self.visitado[w]:
                    if not self.explorado[vertice + w]:
                        self.explorado[v + w] = True
                else:
                    self.explorado[vertice + w], self.descoberto[vertice + w], self.visitado[w] = True, True, True
                    fila.append(w)

    def determinarDistancias(self, grafo, vertice):
        fila = deque()                    
        self.visitado[vertice] = True
        self.distancia[vertice] = sys.maxsize
        fila.append((vertice, 1))

        while len(fila) > 0:
            value = fila.popleft()
            v = value[0] 
            niv = value[1]
            neighbours = adjacencyList(grafo).vertexNeighbours(v)

            for w in neighbours:
                if self.visitado[w]:
                    if not self.explorado[vertice + w]:
                        self.explorado[vertice + w] = True
                else:
                    self.explorado[vertice + w], self.descoberto[vertice + w] = True, True
                    self.visitado[w], self.distancia[w] = True, niv
                    fila.append((w, niv + 1))
