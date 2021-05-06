import re
import sys
from math import sqrt, floor

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
            return non_numeric.sub("", element)


"""
Repita a lista de linhas do arquivo
se a linha começa com um valor numérico dentro da
gama da dimensão, mantemos o resto que são
as coordenadas de cada cidade
1 33.00 44.00 => 33.00 44.00
"""


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


def nearest_neighbor_tour(tsp):
    """Construct a tour through all cities in a TSP by following the nearest
neighbor heuristic"""
    nearest_neighbor_path = [1]
    current_city = 1
    cities_to_travel = set(range(2, int(detect_dimension(tsp)) + 1))

    while cities_to_travel:
        current_city = nearest_neighbor(tsp, cities_to_travel, current_city)
        nearest_neighbor_path.append(current_city)
        cities_to_travel.remove(current_city)
    return tour_from_path(nearest_neighbor_path)


def nearest_neighbor(tsp, untraveled_cities, current_city):
    """Given a set of city keys, find the key corresponding to the
closest city"""
    def distance_to_current_city(city): return calc_distance(
        tsp, current_city, city)
    return min(untraveled_cities, key=distance_to_current_city)


def calc_distance(tsp, city1_index, city2_index):
    """Calculate distance between cities by their (one-based) indices"""
    cities = city_tup(get_cities(tsp, detect_dimension(tsp)))
    return euc_2d_distance(cities[city1_index - 1], cities[city2_index - 1])


def euc_2d_distance(city1, city2):
    xd = city1[0] - city2[0]
    yd = city1[1] - city2[1]
    return round(sqrt(xd*xd + yd*yd),2)


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

"""
Juntando tudo
"""
def produce_final(file=str(sys.argv[2])):
    data = read_tsp_data(file)
    return to_init_graph(data, nearest_neighbor_tour(data))


if __name__ == '__main__':
    res = produce_final()
    print(res)