import json 
from adjMatrix import * 
from adjList import * 
 
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
 
 
fileNotLoaded = True 
while fileNotLoaded: 
        fileName = input("Digite o nome do arquivo com o grafo: ") 
        graphObj = loadGraph(fileName) 
        if graphObj != -1: 
                fileNotLoaded = False 
 
representationType = input("Digite 0 para representar o grafo com uma lista de adjacencia, e 1 para representar o grafo por uma matriz de adjacencia: ") 
 
if representationType == "0": 
        adjList = adjacencyList(loadGraph(fileName)) 
        print("Grafo carregado!") 
 
if representationType == "1": 
        adjMatrix = adjacencyMatrix(loadGraph(fileName)) 
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
                        "7 - Fechar o programa\n") 
 
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
                        if not adjList.removeVertex(vertexToRemove): print("Ops! Um erro ocorreu na remoção do vertice. Tem certeza que o grafo possui este vertice?") 
                elif representationType == "1": 
                        if not adjMatrix.removeVertex(vertexToRemove): print("Ops! Um erro ocorreu na remoção do vertice. Tem certeza que o grafo possui este vertice?") 
        elif option == "4": 
                newEdge = [] 
                newEdge.append(input("Entre com o nome do primeiro vértice da aresta: ")) 
                newEdge.append(input("Entre com o nome do segundo vértice da aresta: ")) 
 
                if representationType == "0": 
                        adjList.addEdge(newEdge) 
                elif representationType == "1": 
                        adjMatrix.editEdge(newEdge, True) 
        elif option == "5": 
                edgeToRemove = [] 
                edgeToRemove.append(input("Entre com o nome do primeiro vértice da aresta: ")) 
                edgeToRemove.append(input("Entre com o nome do segundo vértice da aresta: ")) 
 
                if representationType == "0": 
                        if not adjList.removeEdge(edgeToRemove): print("Ops! Parece que a aresta selecionada é invalida.") 
                elif representationType == "1": 
                        if not adjMatrix.editEdge(edgeToRemove, False):  print("Ops! Parece que a aresta selecionada é invalida.") 
        elif option == "6": 
                selectedVertex = input("Entre com o nome do vertice: ") 
                if representationType == "0": 
                        print("Vizinhos do vértice "+ selectedVertex + ": ", adjList.vertexNeighbours(selectedVertex)) 
                elif representationType == "1": 
                         print("Vizinhos do vértice "+ selectedVertex + ": ", adjMatrix.vertexNeighbours(selectedVertex)) 
        elif option == "7": 
                running = False 
