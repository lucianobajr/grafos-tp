from collections import defaultdict 

class AdjNode: 
    def __init__(self, data,weight): 
        self.vertex = data 
        self.weight = weight  
        self.next = None
        self.visited = False
        
    

class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.order = vertices
        self.graph = [None] * self.V 
        self.numeroDeCompConex = 0
        
  
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

    # Function to get the order
    def get_order(self):
        print("The order is ", self.order, end=" ")
        print("")

# Python program to print connected
# components in an undirected graph
#   
    def DFSUtil(self, temp, v, visited): 
        # Mark the current vertex as visited
        visited[v] = True 
        # Store the vertex to list
        temp.append(v) 
        # Repeat for all vertices adjacent
        # to this vertex v

        aux = self.graph[v]
        while aux:
            print(aux[v].vertex)
        #for i in self.adj[v]:
            if visited[aux.vertex] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, aux.vertex, visited)
            aux = aux.next
            
        return temp 
    
    def connectedComponents(self):
        visited = []
        cc = []        
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                self.numeroDeCompConex+=1
                cc.append(self.DFSUtil(temp, v, visited))
        
        return cc


# Driver program to the above graph class 
if __name__ == "__main__": 
    size = 0
    with open("teste.txt", 'r') as file_input:  # arquivo de input
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
                    size = size_graphAux(size)
            except:
                print("Erro ao inserir Aresta")  
    
   
    
    graph.print_graph()

    graph.get_order()      

    cc = graph.connectedComponents()
    print("Following are connected components")
    print(cc)
    print(graph.numeroDeCompConex)
  
    

# This code is contributed by Kanav Malhotra 