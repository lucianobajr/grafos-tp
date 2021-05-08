import random
import sys

from tools.tsp import detect_dimension,calc_distance,tour_from_path
from package.k2opt import Improver


def Optimal_FN(tsp): 
    K2opt = Improver()  
    dim = int(detect_dimension(tsp))
    # tour , tamanho 
    furthest_neighbor_path = furthest_neighbor_tour(tsp)
    return K2opt.driver2opt(str(sys.argv[3]),dim,furthest_neighbor_path)

    
def furthest_neighbor_tour(tsp):
    """Construct a tour through all cities in a TSP by following the nearest
neighbor heuristic"""
    furthest_neighbor_path = [1]
    current_city =  random.randint(1,int(detect_dimension(tsp)))
    cities_to_travel = set(range(2, int(detect_dimension(tsp)) + 1))

    while cities_to_travel:
        current_city = furthest_neighbor(tsp, cities_to_travel, current_city)
        furthest_neighbor_path.append(current_city)
        cities_to_travel.remove(current_city)
    return tour_from_path(furthest_neighbor_path)

def furthest_neighbor(tsp, untraveled_cities, current_city):
    """Given a set of city keys, find the key corresponding to the
closest city"""
    def distance_to_current_city(city): return calc_distance(
        tsp, current_city, city)
    return max(untraveled_cities, key=distance_to_current_city)