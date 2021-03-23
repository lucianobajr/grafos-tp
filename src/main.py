import sys
import networkx as nx 
import matplotlib.pyplot as plt   

class AdjNode: 
    def __init__(self, data,weight): 
        self.vertex = data 
        self.weight = weight  
        self.next = None 
        self.marked = False # use in DFS  
        self.explored = False
     

class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.G = nx.Graph()
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph  
    # é melhor chamar de neighbor por ser um grafo nao direcionado
    def add_edge(self, Neighbor1, Neighbor2, weight): 
        # Adding the node to the source node 
        node = AdjNode(Neighbor2,weight) 
        node.next = self.graph[Neighbor1] 
        self.graph[Neighbor1] = node 
  

        node = AdjNode(Neighbor1,weight) 
        node.next = self.graph[Neighbor2] 
        self.graph[Neighbor2] = node  

        self.G.add_node(Neighbor1) 
        self.G.add_node(Neighbor2) 
        self.G.add_edge(Neighbor1,Neighbor2,weight=weight)
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -- {} W: {} || ".format(temp.vertex, temp.weight), end="") 
                temp = temp.next
            print(" \n") 
    
    # Percorre cara nó e verifica se o vertice em questão indice nele
    def findDegree(self,ver):
        degree = 0
        for i in range(self.V):
            temp = self.graph[i]
            while temp: 
                if(temp.vertex == ver):
                    degree+=1
                temp = temp.next
        return degree 
#_________________________________________________________________________________#    
    def Neighbor_by_vertex(self, vertex): 
        findFlag = False
        for i in range(self.V): 
            if i == vertex:
                print("Lista de vizinhos do vertice {}\n ".format(i), end="") 
                temp = self.graph[i] 
                findFlag = True
                while temp: 
                    print(" -- {} W: {} || ".format(temp.vertex, temp.weight), end="") 
                    temp = temp.next
                print(" \n")  
        if findFlag == False:
            print("O vertice digitado nao possui vizinhos no grafo inserido\n")
#_________________________________________________________________________________#
    def Unmark_All(self):  
        for i in range (0,self.V):
            temp = self.graph[i] 
            while temp:  
                temp.marked = False    
                temp.explored = False
                temp = temp.next
 #_________________________________________________________________________________#
    def Intern_DFS(self, vertex):          
        temp = self.graph[vertex] 
        while temp:  
            if temp.marked == False:  
                temp.explored = True   
                temp.marked = True
                print("{} - {}".format(vertex, temp.vertex)) 
                aux_temp = self.graph[temp.vertex]  
                while aux_temp:  
                    if aux_temp.vertex == vertex: 
                        aux_temp.marked = True
                    aux_temp = aux_temp.next
            
                self.Intern_DFS(temp.vertex)
            else:   
                if temp.explored == False:  
                    #file = open('aresta_retorno.txt','w')  
                    arq=open("teste.txt","w")
                    if temp.explored == True :  
                        #aux = '{} - {}\n'.format(vertex,temp.vertex)
                        #print("{} - {}".format(vertex, temp.vertex)) 
                        arq.write("%d %d\n"%(vertex,temp.vertex))
                    arq.close()
                        #file.write(aux) 
                        #file.close()

            temp = temp.next 



 #_________________________________________________________________________________#    
    def DFS(self, vertex):   
        
        self.Unmark_All()  
       # self.graph[vertex].marked = True
        self.Intern_DFS(vertex) 

def size_graphAux(size):
    size +=1
    return size

def print_size(size):
    print("O tamanho do grafo é", size) 

def NbV():  
    while True:
        vertex = int(input("Entre com vertice (-1 para sair): ")) 
        if vertex == -1 : 
            break
        graph.Neighbor_by_vertex(vertex)

#______________________________________Driver___________________________________________                        
if __name__ == "__main__": 
    size = 0
    with open(str(sys.argv[2]), 'r') as file_input:  # arquivo de input
        V = file_input.readline()
        graph = Graph(int(V)+1) 
        while True:
            try:
                file_line = file_input.readline()
                if not file_line:
                    break
                else:
                    item = file_line.split(" ")
                    graph.add_edge(int(item[0]),int(item[1]),int(item[2]))
                    size = size_graphAux(size)
            except:
                print("Erro ao inserir Aresta")
           
   
    #graph.print_graph()
    print_size(size) 
    NbV()  
    vertex = int(input("Entre com vertice (DFS): "))
    #chama busca profunda 
    graph.DFS(vertex)  
     #garante a posicao randomica 
    pos=nx.random_layout(graph.G) 
    #define resolucao da imagem 
    fig = plt.figure(figsize=(40, 40), dpi= 70)  
    #nao haver sobreposicao
    plt.clf() 
    #parametros do desenho
    nx.draw_networkx(graph.G,pos,node_color='yellowgreen') 
    #colocar peso nas arestas 
    labels = nx.get_edge_attributes(graph.G,'weight') 
    # desenha 
    nx.draw_networkx_edge_labels(graph.G,pos,edge_labels=labels) 
    #abre arquivo externo
    plt.show() 