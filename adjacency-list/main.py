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
  
  
 #_________________________________________________________________________________# 
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



 #______________________________________Driver___________________________________________#
def NbV():  
    while True:
        vertex = int(input("Entre com vertice (-1 para sair): ")) 
        if vertex == -1 : 
            break
        graph.Neighbor_by_vertex(vertex)

if __name__ == "__main__": 


    V = 7
    graph = Graph(V) 
    graph.add_edge(0, 1,1)  
    graph.add_edge(0, 4,2)   
    graph.add_edge(1, 2,3) 
    graph.add_edge(1, 3,4) 
    graph.add_edge(1, 4,2) 
    graph.add_edge(2, 3,5) 
    graph.add_edge(2, 5,6)  
    graph.add_edge(1, 5,6)  
    graph.add_edge(0, 5,6)   
    graph.add_edge(5, 6,6)   
     

    
    NbV()  
    vertex = int(input("Entre com vertice (DFS): "))
    graph.DFS(vertex)  
    
    # nx.drawing.layout.circular_layout(graph.G)
    # nx.draw(graph.G, with_labels=True, node_color='yellowgreen') 
    
    pos=nx.circular_layout(graph.G) # pos = nx.nx_agraph.graphviz_layout(G)
    nx.draw_networkx(graph.G,pos,node_color='yellowgreen')
    labels = nx.get_edge_attributes(graph.G,'weight')
    nx.draw_networkx_edge_labels(graph.G,pos,edge_labels=labels) 
    plt.show()
    
  