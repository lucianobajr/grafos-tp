class AdjNode: 
    def __init__(self, data,weight): 
        self.vertex = data 
        self.weight = weight  
        self.next = None
  

#def new_graph(size):
#    ref_arquivo = open("entrada01.txt","r")
#    V = int(ref_arquivo.readline())
#    graph = Graph(V)

#    for linha in (ref_arquivo):
#        size = size_graphAux(size)
#        valores = linha.split()
#        Value01 = int(valores[0])
#        Value02 = int(valores[1])
#        Weight = float(valores[2])
#        graph.add_edge(Value01,Value02,Weight)

#   return size
    
def size_graphAux(size):
    size +=1
    return size

def print_size(size):
    print("O tamanho do grafo é ",size)

# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Functi'on to add an edge in an undirected graph  
    # é melhor chamar de neighbor por ser um grafo nao direcionado
    def add_edge(self, Neighbor1, Neighbor2, weight): 
        # Adding the node to the source node 
        node = AdjNode(Neighbor2,weight) 
        node.next = self.graph[Neighbor1] 
        self.graph[Neighbor1] = node 
  

        node = AdjNode(Neighbor1,weight) 
        node.next = self.graph[Neighbor2] 
        self.graph[Neighbor2] = node 
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -- {} W: {} || ".format(temp.vertex, temp.weight), end="") 
                temp = temp.next
            print(" \n") 
    
    
# Driver program to the above graph class 
if __name__ == "__main__": 
    
    size = 0
    ref_arq = open("entrada01.txt","r")
    V = int(ref_arq.readline())
    graph = Graph(V)

    for linha in (ref_arq):
        size = size_graphAux(size)
        Values = linha.split()
        Value01 = int(Values[0])
        Value02 = int(Values[1])
        Weight = float(Values[2])
        graph.add_edge(Value01,Value02,Weight)
    
    print_size(size)
    graph.print_graph()

    #V = 5
    #graph = Graph(V) 
    #graph.add_edge(0, 1,1) 
    #graph.add_edge(0, 4,2) 
    #graph.add_edge(1, 2,3) 
    #graph.add_edge(1, 3,4) 
    #graph.add_edge(1, 4,2) 
    #graph.add_edge(2, 3,5) 
    #graph.add_edge(3, 4,6) 
    #graph new_graph()
    #graph.print_graph()
    
    #graph.size_graph()
  
# This code is contributed by Kanav Malhotra 