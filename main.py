import json
from adjMatrix import *
from adjList import adjacencyList
from busca import busca
from CaminhoMinimo import *
import time

def loadGraph(fileName):
    try:
        with open(fileName, 'r') as graphFile:
            graph = json.load(graphFile)

            print('nome = ', graph["nome"])
            print('vertices = ', graph["vertices"])
            print('arestas = ', graph["arestas"])
            return graph
    except:
        print("Arquivo não encontrado. Aperte CTRL + C para sair do programa ou tente novamente.")
        return -1


graphObj = {}
fileNotLoaded = True
while fileNotLoaded:
    fileName = input("Digite o nome do arquivo com o grafo: ")
    graphObj = loadGraph(fileName)
    if graphObj != -1:
        fileNotLoaded = False

representationType = input(
    "Digite 0 para representar o grafo com uma lista de adjacencia, e 1 para representar o grafo por uma matriz de adjacencia: ")

if representationType == "0":
    adjList = adjacencyList(graphObj)
    print("Grafo carregado!")

if representationType == "1":
    adjMatrix = adjacencyMatrix(graphObj)
    print("Grafo carregado!")


running = True
while running:
    option = input("Digite a função a ser executada:\n" +
                   "1 - Imprimir o grafo\n" +
                   "2 - Adicionar um vertice\n" +
                   "3 - Remover um vertice\n" +
                   "4 - Adicionar uma Aresta\n" +
                   "5 - Remover uma Aresta\n" +
                   "6 - Imprimir os vizinhos de um vertice selecionado\n" +
                   "7 - O grafo é conexo?\n" +
                   "8 - O grafo possum um ciclo?\n" +
                   "9 - O grafo é uma floresta?\n" +
                   "10 - O grafo é uma árvore\n" +
                   "11 - O grafo é uma árvore usando ciclo e conexo\n" +
                   "12 - Testes de código\n" +
                   "13 - Caminho Minimo\n" +
                   "14 - Timer\n" +
                   "15 - Fechar o programa\n")

    if option == "1":
        if representationType == "0":
            adjList.printList()
        elif representationType == "1":
            adjMatrix.printMatrix()
    elif option == "2":
        newVertex = input("Entre com o nome do vertice: ")
        if representationType == "0":
            adjList.addVertex(newVertex)
        elif representationType == "1":
            adjMatrix.addVertex(newVertex)
    elif option == "3":
        vertexToRemove = input("Entre com o vertice a ser excluido: ")
        if representationType == "0":
            if not adjList.removeVertex(vertexToRemove):
                print(
                    "Ops! Um erro ocorreu na remoção do vertice. Tem certeza que o grafo possui este vertice?")
        elif representationType == "1":
            if not adjMatrix.removeVertex(vertexToRemove):
                print(
                    "Ops! Um erro ocorreu na remoção do vertice. Tem certeza que o grafo possui este vertice?")
    elif option == "4":
        newEdge = []
        newEdge.append(
            input("Entre com o nome do primeiro vértice da aresta: "))
        newEdge.append(
            input("Entre com o nome do segundo vértice da aresta: "))

        if representationType == "0":
            adjList.addEdge(newEdge)
        elif representationType == "1":
            adjMatrix.editEdge(newEdge, True)
    elif option == "5":
        edgeToRemove = []
        edgeToRemove.append(
            input("Entre com o nome do primeiro vértice da aresta: "))
        edgeToRemove.append(
            input("Entre com o nome do segundo vértice da aresta: "))

        if representationType == "0":
            if not adjList.removeEdge(edgeToRemove):
                print("Ops! Parece que a aresta selecionada é invalida.")
        elif representationType == "1":
            if not adjMatrix.editEdge(edgeToRemove, False):
                print("Ops! Parece que a aresta selecionada é invalida.")
    elif option == "6":
        selectedVertex = input("Entre com o nome do vertice: ")
        if representationType == "0":
            print("Vizinhos do vértice " + selectedVertex +
                  ": ", adjList.vertexNeighbours(selectedVertex))
        elif representationType == "1":
            print("Vizinhos do vértice " + selectedVertex + ": ",
                  adjMatrix.vertexNeighbours(selectedVertex))
    elif option == "7":
        print(busca(graphObj).ehConexo(graphObj))
    elif option == "8":
        print(busca(graphObj).temCiclo(graphObj))
    elif option == "9":
        print(busca(graphObj).ehFloresta(graphObj))
    elif option == "10":
        print(busca(graphObj).ehArvore(graphObj))
    elif option == "11":
        print(busca(graphObj).ehArvoreShort(graphObj))
    elif option == "12":
        instance = busca(graphObj)
        instance.buscaProfundidadeRec(graphObj, "1")

        print(instance.visitado)
        print(instance.explorado)
        print(instance.descoberto)
    elif option == "13":
        selected = input("Entre com o vertice selecionado: ")
        print(CaminhoMinimo(graphObj).dijkstra(selected))
        print("++++++++++++++++++++++++++++")
        CM = CaminhoMinimo(graphObj).floyd()
        for i in CM: print(i)
    elif option == "14":
        inicio5=0.0
        inicio6=0.0
        inicio9=0.0
        inicio10=0.0
        inicio11=0.0
        inicio12=0.0
        inicio13=0.0
        inicio17=0.0
        inicio26=0.0
        inicio27=0.0
        inicio57 = 0.0
        inicio62 = 0.0
        fim5=0.0
        fim6=0.0
        fim9=0.0
        fim10=0.0
        fim11=0.0
        fim12=0.0
        fim13=0.0
        fim17=0.0
        fim26=0.0
        fim27=0.0
        fim57=0.0
        fim62 = 0.0

        for i in range  (0,200):
            
            inicio5 += time.time()  
            busca(graphObj)
            fim5 += time.time()

            inicio6 += time.time()  
            busca(graphObj).buscaCompleta(graphObj)
            fim6 += time.time()

            inicio9 += time.time()  
            busca(graphObj).ehConexo(graphObj)
            fim9 += time.time()

            inicio10 += time.time()  
            busca(graphObj).temCiclo(graphObj)
            fim10 += time.time()

            inicio11 += time.time()  
            busca(graphObj).ehFloresta(graphObj)
            fim11 += time.time()

            inicio12 += time.time()  
            busca(graphObj).ehArvore(graphObj)
            fim12 += time.time()

            inicio13 += time.time()  
            busca(graphObj).ehArvoreShort(graphObj)
            fim13 += time.time()

            inicio17 += time.time()  
            busca(graphObj).obterFlorestaGeradora(graphObj)
            fim17 += time.time()

            #inicio26 += time.time()
            #instance = busca(graphObj)  
            #instance.buscaProfundidade(graphObj, "1")
            #fim26 += time.time()

            inicio27 += time.time()
            instance = busca(graphObj)  
            instance.buscaProfundidadeRec(graphObj, "1")
            fim27 += time.time()

            inicio57 += time.time()
            instance = busca(graphObj)  
            instance.buscaLargura(graphObj, "1")
            fim57 += time.time() 

            inicio62 += time.time()
            instance = busca(graphObj)  
            instance.determinarDistancias(graphObj, "1")
            fim62 += time.time()           


        print("Time Slide5:",(fim5 - inicio5)/200)
        print("Time Slide6:",(fim6 - inicio6)/200)
        print("Time Slide9:",(fim9 - inicio9)/200)
        print("Time Slide10:",(fim10 - inicio10)/200)
        print("Time Slide11:",(fim11 - inicio11)/200)
        print("Time Slide12:",(fim12 - inicio12)/200)
        print("Time Slide13:",(fim13 - inicio13)/200)
        print("Time Slide14:",(fim17 - inicio17)/200)
        #print("Time Slide26:",(fim26 - inicio26)/200)
        print("Time Slide27:",(fim27 - inicio27)/200)
        print("Time Slide57:",(fim57 - inicio57)/200)
        print("Time Slide62:",(fim62 - inicio62)/200)
        
    elif option == "15":
        running = False
    

