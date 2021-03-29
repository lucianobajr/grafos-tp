import sys
import networkx as nx 
import matplotlib.pyplot as plt   
import json
from ipython_genutils.py3compat import xrange
from menu import simpleMenu, pause 
sys.setrecursionlimit(10**6) 

class bcolors:
    Preto = '\033[1;30m'
    Vermelho = '\033[1;31m'
    Verde = '\033[1;32m'
    Amarelo = '\033[1;33m'
    Azul = '\033[1;34m'
    Magenta = '\033[1;35m'
    Cyan = '\033[1;36m'
    CinzaC = '\033[1;37m'
    CinzaE = '\033[1;90m'
    VermelhoC = '\033[1;91m'
    VerdeC = '\033[1;92m'
    AmareloC = '\033[1;93m'
    AzulC = '\033[1;94m'
    MagentaC = '\033[1;95m'
    CyanC = '\033[1;96m'
    Branco = '\033[1;97m'
    Negrito = '\033[;1m'
    Inverte = '\033[;7m'
    Reset = '\033[0;0m'

class AdjNode:
    def __init__(self, data, weight):
        self.vertex = data
        self.weight = weight
        self.next = None
        self.explored = False

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.G = nx.Graph()
        self.Time = 0
        self.graph = [None] * self.V

    def add_edge(self, Neighbor1, Neighbor2, weight):
        node = AdjNode(Neighbor2, weight)
        node.next = self.graph[Neighbor1]
        self.graph[Neighbor1] = node

        node = AdjNode(Neighbor1, weight)
        node.next = self.graph[Neighbor2]
        self.graph[Neighbor2] = node

        self.G.add_node(Neighbor1)
        self.G.add_node(Neighbor2)
        self.G.add_edge(Neighbor1, Neighbor2, weight=weight)

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -- {} W: {} || ".format(temp.vertex, temp.weight), end="")
                temp = temp.next
            print(" \n")

#_____________FUNÇÕES DO TP_____________#

#_________________________________________________________________________________#
    # Retornar a ordem do grafo
    def get_order(self):
        return self.V - 1
#_________________________________________________________________________________#
    # Determinar o tamanho
    def sizeOfGraph(self):
        size = 0
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                size += 1
                temp = temp.next
        return size // 2
#_________________________________________________________________________________#
    # Retornar os vizinhos de um vértice fornecido

    def Neighbor_by_vertex(self, vertex):
        
        findFlag = False
        for i in range(self.V):
            if i == vertex:
                print("Lista de vizinhos do vertice {}\n ".format(i), end="")
                arq=open("../out/saida.txt","a") 
                arq.write("\n--------------------------------------------------\n")
                arq.write("\nLista de vizinhos do vertice {}".format(i))    
                arq.close()      

                temp = self.graph[i]
                findFlag = True
                while temp:
                    print(" -- {} W: {} || ".format(temp.vertex, temp.weight), end="") 
                    arq=open("../out/saida.txt","a")
                    arq.write(" -- {} W: {} || ".format(temp.vertex, temp.weight))  
                    arq.close()      

                    temp = temp.next
                print(" \n")
        if findFlag == False:
            print("O vertice digitado nao possui vizinhos no grafo inserido\n")
#_________________________________________________________________________________#
    # Determinar o grau de um vértice fornecido

    def findDegree(self, ver):
        degree = 0
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                if(temp.vertex == ver):
                    degree += 1
                temp = temp.next
        return degree

#_________________________________________________________________________________#
    ''' Determinar a sequência de vértices visitados na busca em profundidade e informar
    a(s) aresta(s) de retorno '''

    def Unmark_All(self,marked):
        for i in xrange (0,self.V):
            temp = self.graph[i] 
            marked.append(False)
            while temp:     
                temp.explored = False
                temp = temp.next 

    def Intern_DFS(self, vertex,marked):
        temp = self.graph[vertex]  
        marked[vertex] = True
        while temp:  
            if marked[temp.vertex] == False:  
                temp.explored = True  
                print("{} - {}".format(vertex, temp.vertex))  
                arq=open("../out/saida.txt","a") 
                arq.write("%d %d\n"%(vertex,temp.vertex))    
                arq.close()
                aux_temp = self.graph[temp.vertex]  
                while aux_temp:  
                    if aux_temp.vertex == vertex: 
                        aux_temp.explored = True 
                    aux_temp = aux_temp.next
            
                self.Intern_DFS(temp.vertex,marked)
            else:   
                if temp.explored == False:   
                    #exploração 
                    temp.explored = True

                    aux_temp = self.graph[temp.vertex]   
                    while aux_temp:   
                        if aux_temp.vertex == vertex: 
                            arq=open("../out/arestas_retorno.txt","a") 
                            arq.write("%d %d\n"%(vertex,temp.vertex))     
                            arq.close()         
                            aux_temp.explored = True 
                        aux_temp = aux_temp.next
            

            temp = temp.next

    def DFS(self, vertex):
        marked = []
        self.Unmark_All(marked) 
        arq=open("../out/saida.txt","a") 
        arq.write("\n--------------------------------------------------\n")
        arq.write("Sequencia de vertices vizitados na DFS\n")
        arq.close()
        self.Intern_DFS(vertex,marked)

#_________________________________________________________________________________#
    '''Determinar o número de componentes conexas do grafo e os vértices de cada componente'''

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(1, self.V+1):
            visited.append(False)
        for v in range(1, self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    def DFSUtil(self, temp, v, visited):
        visited[v] = True

        temp.append(v)

        aux = self.graph[v]
        while aux:
            if visited[aux.vertex] == False:

                temp = self.DFSUtil(temp, aux.vertex, visited)
            aux = aux.next

        return temp

 #_________________________________________________________________________________#
    # Verificar se um vértice é articulação
    def AP(self):
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V) 

        for i in range(self.V):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)

        aux = []
        for index, value in enumerate(ap):
            if value == True:
                aux.append(index)
        return aux 

    def APUtil(self, u, visited, ap, parent, low, disc):
        children = 0

        visited[u] = True

        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        temp = self.graph[u]
        while temp:
            if visited[temp.vertex] == False:
                parent[temp.vertex] = u
                children += 1
                self.APUtil(temp.vertex, visited, ap, parent, low, disc)

                low[u] = min(low[u], low[temp.vertex])

                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[temp.vertex] >= disc[u]:
                    ap[u] = True

            elif temp.vertex != parent[u]:
                low[u] = min(low[u], disc[temp.vertex])
            temp = temp.next

    def findArtpoint(self, num):
        artpoint = self.AP()
        if(num in artpoint): 
            arq = open("../out/saida.txt","a")
            arq.write("\n--------------------------------------------------\n")    
            print(num," é um ponto de articulação.") 
            arq.write("{} é um ponto de articulação.".format(num)) 
            arq.close()
        else:
            print(num, "não é um ponto de articulação.") 
            arq = open("../out/saida.txt","a")
            arq.write("\n--------------------------------------------------\n")    
            arq.write("O vértice inserido não é um ponto de articulação.") 
            arq.close()
#_________________________________________________________________________________#
    # Verificar se uma aresta á ponte
    def bridgeUtil(self,u, visited, parent, low, disc,bridges):
  
        visited[u]= True
  
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
  
        aux = self.graph[u]

        while aux:
            if visited[aux.vertex] == False :
                parent[aux.vertex] = u
                self.bridgeUtil(aux.vertex, visited, parent, low, disc,bridges)
  
                low[u] = min(low[u], low[aux.vertex])  
                auxVector = [ ]
                if low[aux.vertex] > disc[u]:
                    auxVector.append(u)
                    auxVector.append(aux.vertex)
                bridges.append(auxVector)                          
            
            elif aux.vertex != parent[u]:
                low[u] = min(low[u], disc[aux.vertex])
            aux = aux.next

    def bridge(self):
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)

        bridges = []

        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc,bridges)

        return bridges
                

    def findBridges(self,m):
        bridges = self.bridge()
        response  = False
        for bridge in bridges:
            if m == bridge or m == bridge[::-1]:
                response = True

        return response
                 


        '''
        artpoint = self.AP()
        if(num in artpoint):
            print(num," é um ponto de articulação.")
        else:
            print(num, "não é um ponto de articulação.")
        '''

# ______________________________________Driver___________________________________________
if __name__ == "__main__":
    with open(str(sys.argv[2]), 'r') as file_input:
        V=0
        read_file = None
        if str(sys.argv[2])[8:].split(".")[1]=="txt":
            V = file_input.readline()
        else:
            read_file = json.load(file_input)
            V = read_file['data']['nodes']['length']

        graph = Graph(int(V)+1)

        if str(sys.argv[2])[8:].split(".")[1]=="txt":
            while True:
                try:
                    file_line = file_input.readline()
                    if not file_line:
                        break
                    else:
                        item = file_line.split(" ")
                        graph.add_edge(int(item[0]), int(item[1]), float(item[2]))
                except:
                    print("Erro ao inserir Aresta")
        else:
            lines = read_file['data']['edges']['_data']
            for i in range (len(lines)):
                line = lines["{}".format(i+1)]
                graph.add_edge(int(line['from']), int(line['to']), float(line['label']))

    def option_1(): 
        arq = open("../out/saida.txt","a")       
        arq.write("\n--------------------------------------------------\n")
        arq.write("\nO grafo tem ordem {}\n".format(graph.get_order())) 
        arq.close()
        print("\nO grafo tem ordem {}\n".format(graph.get_order()))
        pause()

    def option_2(): 
        arq = open("../out/saida.txt","a")      
        arq.write("\n--------------------------------------------------\n")
        arq.write("\nO grafo tem tamanho {}\n".format(graph.sizeOfGraph())) 
        arq.close()
        print("\nO grafo tem tamanho {}\n".format(graph.sizeOfGraph()))
        pause()

    def option_3():
        vertex = int(input("Digite o vertice: "))
        graph.Neighbor_by_vertex(vertex)
        pause()

    def option_4():
        vertex = int(input("Digite o vertice: "))
        arq = open("../out/saida.txt","a")      
        print("\nO vértice {} tem grau {}\n".format(vertex, graph.findDegree(vertex)))  
        arq.write("\n--------------------------------------------------\n")
        arq.write("\nO vértice {} tem grau {}\n".format(vertex, graph.findDegree(vertex))) 
        arq.close()
        pause()

    def option_5():
        vertex = int(input("Digite o vertice (DFS): "))
        graph.DFS(vertex)
        pause()

    def option_6():
        print(graph.connectedComponents())
        pause()

    def option_7():
        vertex = int(input("Digite o vertice: "))
        graph.findArtpoint(vertex)
        pause()

    def option_8():
        u = int(input("Digite um vértice (u): "))
        v = int(input("Digite um vértice (v): "))
        m = [u,v]
        response =  graph.findBridges(m)

        if response: 
            arq = open("../out/saida.txt","a")
            arq.write("\n--------------------------------------------------\n")    
            arq.write("{}-{} é uma ponte.".format(u,v)) 
            arq.close()
            print("A aresta é ponte!")
        else:
            print("A aresta não é ponte!") 
            arq = open("../out/saida.txt","a")
            arq.write("\n--------------------------------------------------\n")    
            arq.write("A aresta inserida não é uma ponte.") 
            arq.close()

        pause()


    def option_9():
        pos=nx.random_layout(graph.G) 
        fig = plt.figure(figsize=(40, 40), dpi= 70)  
        plt.clf() 
        nx.draw_networkx(graph.G,pos,node_color='yellowgreen') 
        labels = nx.get_edge_attributes(graph.G,'weight') 
        nx.draw_networkx_edge_labels(graph.G,pos,edge_labels=labels) 
        plt.show()
        
    
    
    sMenu = simpleMenu(f'{bcolors.Branco}TRABALHO GRAFOS{bcolors.Reset}')
    sMenu.spacing = [ '0','d' ]
    sMenu.menu_option_add(option_1,'Retornar a ordem do grafo')
    sMenu.menu_option_add(option_2,'Determinar o tamanho do grafo')
    sMenu.menu_option_add(option_3,'Retornar os vizinhos de um vértice fornecido')
    sMenu.menu_option_add(option_4,'Determinar o grau de um vértice fornecido')
    sMenu.menu_option_add(option_5,'Determinar a sequência de vértices visitados na busca em profundidade e informar a(s) aresta(s) de retorno')
    sMenu.menu_option_add(option_6,'Determinar o número de componentes conexas do grafo e os vértices de cada componente')
    sMenu.menu_option_add(option_7,'Verificar se um vértice é articulação')
    sMenu.menu_option_add(option_8,'Verificar se uma aresta á ponte')
    sMenu.menu_option_add(option_9,'Visualizar o grafo')
    sMenu.menu_start() 





     