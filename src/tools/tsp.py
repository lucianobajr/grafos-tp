import re
from math import sqrt
"""
Repita a lista de linhas do arquivo
se a linha começa com um valor numérico dentro da
gama da dimensão, mantemos o resto que são
as coordenadas de cada cidade
1 33.00 44.00 => 33.00 44.00
"""
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
            return non_numeric.sub("", element)

def get_cities(list, dimension):
    dimension = int(dimension)
    array1 = []
    for item in list:
        for num in range(1, dimension + 1):
            if item.startswith(str(num)):
                index, space, rest = item.partition(' ')
                if rest not in array1:
                    array1.append(rest)
    return array1

"""
Quebra cada coordenada 33.00 44.00 para uma tupla ('33.00' ,'44.00')
"""

def city_tup(list):
    array = []
    for item in list:
        first_coord, space, second_coord = item.partition(' ')
        array.append(
            (float(first_coord.strip()), float(second_coord.strip())))
    return array


def tour_from_path(path):
    """Append the first city in a path to the end in order to obtain a tour"""
    path.append(path[0])
    return path


def euc_2d_distance(city1, city2):
    xd = city1[0] - city2[0]
    yd = city1[1] - city2[1]
    return round(sqrt(xd*xd + yd*yd),2)

def final_distance(tsp,list): 
    return distance_tour(to_init_graph(tsp,list)) 

def calc_distance(tsp, city1_index, city2_index):
    """Calculate distance between cities by their (one-based) indices"""
    cities = city_tup(get_cities(tsp, detect_dimension(tsp)))
    return euc_2d_distance(cities[city1_index - 1], cities[city2_index - 1])

def distance_tour(list):
    distance = 0

    for item in list:
        distance += item[2]

    return distance

def to_init_graph(tsp, list):
    array = []

    cities = city_tup(get_cities(tsp, detect_dimension(tsp)))

    for item in list:

        if list.index(item)<len(list)-2:
            city1 = cities[item-1]
            city2 = cities[(list[list.index(item)+1])-1]
            #array.append((item, list[list.index(item)+1],city1,city2,euc_2d_distance(city1, city2)))
            array.append((item, list[list.index(item)+1],euc_2d_distance(city1, city2)))
        else:
            city1 = cities[item-1]
            city2 = cities[(list[len(list)-1])-1]
            #array.append((item, list[list.index(item)+1], city1,city2,euc_2d_distance(city1, city2)))
            array.append((item, list[list.index(item)+1],euc_2d_distance(city1, city2)))
       
    array.pop(len(array)-1)

    return array     

def to_init_graph(tsp, list):
    array = []

    cities = city_tup(get_cities(tsp, detect_dimension(tsp)))

    for item in list:

        if list.index(item)<len(list)-2:
            city1 = cities[item-1]
            city2 = cities[(list[list.index(item)+1])-1]
            #array.append((item, list[list.index(item)+1],city1,city2,euc_2d_distance(city1, city2)))
            array.append((item, list[list.index(item)+1],euc_2d_distance(city1, city2)))
        else:
            city1 = cities[item-1]
            city2 = cities[(list[len(list)-1])-1]
            #array.append((item, list[list.index(item)+1], city1,city2,euc_2d_distance(city1, city2)))
            array.append((item, list[list.index(item)+1],euc_2d_distance(city1, city2)))
       
    array.pop(len(array)-1)

    return array