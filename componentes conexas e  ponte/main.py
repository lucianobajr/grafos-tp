import sys
sys.setrecursionlimit(1000000)

class AdjNode: 
    def __init__(self, data,weight): 
        self.vertex = data 
        self.weight = weight  
        self.next = None
    

class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.numConectedComp = 0
        self.graph = [None] * self.V 
        self.Time = 0
  
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

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(1,self.V+1):
            visited.append(False)
        for v in range(1,self.V):
            if visited[v] == False:
                temp = []
                self.numConectedComp+=1
                cc.append(self.DFSUtil(temp, v, visited))                
        return cc

    def DFSUtil(self, temp, v, visited):
 
        # Mark the current vertex as visited
        visited[v] = True
 
        # Store the vertex to list
        temp.append(v)
 
        # Repeat for all vertices adjacent
        # to this vertex v

        aux = self.graph[v]
        while aux:
        #for i in self.adj[v]:
            if visited[aux.vertex] == False:
 
                # Update the list
                temp = self.DFSUtil(temp, aux.vertex, visited)                
            aux = aux.next  
                
        return temp

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(1,self.V+1):
            visited.append(False)
        for v in range(1,self.V):
            if visited[v] == False:
                temp = []
                self.numConectedComp+=1
                cc.append(self.DFSUtil(temp, v, visited))
                
        return cc


    # DFS based function to find all bridges. It uses recursive
   
    def bridgeUtil(self,u, visited, parent, low, disc):
  
        # Mark the current node as visited and print it
        visited[u]= True
  
        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
  
        #Recur for all the vertices adjacent to this vertex
        aux = self.graph[u]
        while aux:
            # If v is not visited yet, then make it a child of u
            # in DFS tree and recur for it
            if visited[aux.vertex] == False :
                parent[aux.vertex] = u
                self.bridgeUtil(aux.vertex, visited, parent, low, disc)
  
                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                low[u] = min(low[u], low[aux.vertex])  
  
                ''' If the lowest vertex reachable from subtree
                under v is below u in DFS tree, then u-v is
                a bridge'''
                if low[aux.vertex] > disc[u]:
                    print ("%d %d" %(u,aux.vertex))                    
                    #aux = aux.next
                      
            elif aux.vertex != parent[u]: # Update low value of u for parent function calls.
                low[u] = min(low[u], disc[aux.vertex])
            aux = aux.next
    def bridge(self):
    
        # Mark all the vertices as not visited and Initialize parent and visited, 
            # and ap(articulation point) arrays
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
    
        # Call the recursive helper function to find bridges
        # in DFS tree rooted with vertex 'i'
        for i in range(self.V):
            if visited[i] == False:
                self.bridgeUtil(i, visited, parent, low, disc)


def size_graphAux(size):
    size +=1
    return size

def print_size(size):
    print("O tamanho do grafo é", size)
                            
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    size = 0
    with open("teste3.txt", 'r') as file_input:  # arquivo de input
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
           
   
    graph.print_graph()
    print_size(size)
        
    cc = graph.connectedComponents()
    print("Following are connected components")
    print(cc)
    print("entrou eponte")
    print(graph.numConectedComp)

    ePonte = graph.bridge()
    
    