import re
import sys
from math import sqrt,floor

class AdjNode:
    def __init__(self, data):
        self.vertex = data
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
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
 
        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
 
    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# 1462,2976

# É usado um regex aqui para limpar caracteres e manter apenas números
cities_set = []
cities_tups = []

#  Abrimos o arquivo TSP e colocamos cada linha sem espaços
#  e caracteres de nova linha em uma lista
def read_tsp_data(tsp_name):
	tsp_name = tsp_name
	with open(tsp_name) as f:
		content = f.read().splitlines()
		cleaned = [x.lstrip() for x in content if x != ""]
		return cleaned

"""
Verifique a linha DIMENSION no arquivo e mantenha o valor numérico
"""
def detect_dimension(in_list):
	non_numeric = re.compile(r'[^\d]+')
	for element in in_list:
		if element.startswith("DIMENSION"):
			return non_numeric.sub("",element)

"""
Repita a lista de linhas do arquivo
se a linha começa com um valor numérico dentro da
gama da dimensão, mantemos o resto que são
as coordenadas de cada cidade
1 33.00 44.00 => 33.00 44.00
"""
def get_cities(list,dimension):
	dimension = int(dimension)
	for item in list:
		for num in range(1, dimension + 1):
			if item.startswith(str(num)):
				index, space, rest = item.partition(' ')
				if rest not in cities_set:
					cities_set.append(rest)
	return cities_set


"""
Quebra cada coordenada 33.00 44.00 para uma tupla ('33.00' ,'44.00')
"""
def city_tup(list):
	for item in list:
		first_coord, space, second_coord = item.partition(' ')
		cities_tups.append(
            (first_coord.strip(),
             second_coord.strip(),
             float( sqrt( 
                 float(first_coord.strip())*float(first_coord.strip())
                 +
                 float(second_coord.strip())*float(second_coord.strip())))))
	return cities_tups


"""
Juntando tudo
"""
def produce_final(file=str(sys.argv[2])):
	data = read_tsp_data(file)
	dimension = detect_dimension(data)
	cities_set = get_cities(data,dimension)
	cities_tups = city_tup(cities_set)
	

if __name__ == '__main__':
    produce_final()
    print(cities_tups)
    '''  
     V = len(cities_tups)
    graph = Graph(V*2)
    
    for i in range (len(cities_tups)):  
        line0 = (float(cities_tups[i][0]))
        line1 = floor(float(cities_tups[i][1]))
        graph.add_edge(int(line0),int(line1))

    graph.print_graph()
    '''