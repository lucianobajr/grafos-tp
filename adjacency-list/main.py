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
  
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1,1) 
    graph.add_edge(0, 4,2) 
    graph.add_edge(1, 2,3) 
    graph.add_edge(1, 3,4) 
    graph.add_edge(1, 4,2) 
    graph.add_edge(2, 3,5) 
    graph.add_edge(3, 4,6) 
  
    graph.print_graph()
  
# This code is contributed by Kanav Malhotra 