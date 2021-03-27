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
        self.Time = 0
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
    
    def AP(self): 

		# Mark all the vertices as not visited 
		# and Initialize parent and visited, 
		# and ap(articulation point) arrays 
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 
        ap = [False] * (self.V) #To store articulation points 

        # Call the recursive helper function 
        # to find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if visited[i] == False: 
                self.APUtil(i, visited, ap, parent, low, disc) 

        aux = []
        for index, value in enumerate (ap): 
            if value == True: 
                aux.append(index)
        return aux 

    def APUtil(self,u, visited, ap, parent, low, disc): 

        #Count of children in current node 
        children =0

        # Mark the current node as visited and print it 
        visited[u]= True

        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1

        #Recur for all the vertices adjacent to this vertex 
        temp = self.graph[u]
        while temp:
        #for v in self.graph[u]: 
        #    print("ok")
            # If v is not visited yet, then make it a child of u 
            # in DFS tree and recur for it 
            if visited[temp.vertex] == False : 
                parent[temp.vertex] = u 
                children += 1
                self.APUtil(temp.vertex, visited, ap, parent, low, disc)

                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                low[u] = min(low[u], low[temp.vertex]) 

                # u is an articulation point in following cases 
                # (1) u is root of DFS tree and has two or more chilren. 
                if parent[u] == -1 and children > 1: 
                    ap[u] = True
 
                #(2) If u is not root and low value of one of its child is more 
                # than discovery value of u. 
                if parent[u] != -1 and low[temp.vertex] >= disc[u]: 
                    ap[u] = True	
                  
                # Update low value of u for parent function calls	 
            elif temp.vertex != parent[u]: 
            	low[u] = min(low[u], disc[temp.vertex])
            temp = temp.next

    def findArtpoint(self, num):
        artpoint = self.AP()
        if(num in artpoint):
            print(num," é um ponto de articulação.")
        else:
            print(num, "não é um ponto de articulação.")

def size_graphAux(size):
    size +=1
    return size

def print_size(size):
    print("O tamanho do grafo é", size)
                            
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    size = 0
    with open("teste2.txt", 'r') as file_input:  # arquivo de input
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
    graph.findArtpoint(3)
    #print("Pontos de articulação:")
    #graph.AP()
