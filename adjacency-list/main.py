class AdjNode: 
    def __init__(self, data,weight): 
        self.vertex = data 
        self.weight = weight  
        self.next = None
  
  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest, weight): 
        # Adding the node to the source node 
        node = AdjNode(dest,weight) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src,weight) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
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
    Edge = 4
    count = 0 
    # como no arquivo iremos ler primeiro podemos contabilizar quantas linhas há antes de preencher 
    
    graph = Graph(V)    
    while(count <= Edge): 
        Vsrc = int(input("Src:")) 
        Vdst = int(input("Dst: ")) 
        Eweight = int(input("Weight: ")) 
        graph.add_edge(Vsrc, Vdst,Eweight)  
        count +=1   

        if count == 4: 
            break 
  
    graph.print_graph() 
  
# This code is contributed by Kanav Malhotra 