import random
import sys

from tools.tsp import detect_dimension,calc_distance,tour_from_path
from package.k2opt import Improver

def Optimal_NN(tsp): 
    K2opt = Improver()  
    dim = int(detect_dimension(tsp))
    # tour , tamanho 
    nearest_neighbor_path = nearest_neighbor_tour(tsp)
    return K2opt.driver2opt(str(sys.argv[3]),dim,nearest_neighbor_path)

def nearest_neighbor_tour(tsp):
    """Construct a tour through all cities in a TSP by following the nearest
neighbor heuristic""" 

    nearest_neighbor_path = [1]
    current_city = random.randint(1,int(detect_dimension(tsp)))
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