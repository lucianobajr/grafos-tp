import sys

class AdjNode: 
    def __init__(self, data,weight): 
        self.vertex = data 
        self.weight = weight  
        self.next = None
    

class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 

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
                            
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    with open(str(sys.argv[2]), 'r') as file_input:  # arquivo de input
        V = file_input.readline()
        graph = Graph(int(V)) 
        while True:
            try:
                file_line = file_input.readline()
                if not file_line:
                    break
                else:
                    item = file_line.split(" ")
                    graph.add_edge(int(item[0]),int(item[1]),int(item[2]))
            except:
                print("Erro ao inserir Aresta")
           
   
    graph.print_graph()


    '''
    V= 5
    graph = Graph(V) 
    
    graph.add_edge(0,1,1) 
    graph.add_edge(0,4,2) 
    graph.add_edge(1,2,3) 
    graph.add_edge(1,3,4) 
    graph.add_edge(1,4,2) 
    graph.add_edge(2,3,5) 
    graph.add_edge(3,4,6) 

    graph.print_graph()

    print("Vertice 0 tem grau {}".format(graph.findDegree(0)))
    print("Vertice 1 tem grau {}".format(graph.findDegree(1)))
    print("Vertice 2 tem grau {}".format(graph.findDegree(2)))
    print("Vertice 3 tem grau {}".format(graph.findDegree(3)))
    print("Vertice 4 tem grau {}".format(graph.findDegree(4)))

    # This code is contributed by Kanav Malhotra 
    '''