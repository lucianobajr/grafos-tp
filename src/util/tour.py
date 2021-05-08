import sys

from package.nn import Optimal_NN,nearest_neighbor_tour
from package.fn import Optimal_FN,furthest_neighbor_tour 
from tools.tsp import final_distance,tour_from_path

def util_final_tour(tsp, flag):  
    if flag == 1 : # nn
        f = open("../out/%s-NN.txt"%str(sys.argv[3])[12:-4], "w") 
    
        Best_final_path =  []  
        Best_final_length = final_distance(tsp,nearest_neighbor_tour(tsp))
        for i in range (30):      
            Aux_final_path, Aux_final_lenght = Optimal_NN(tsp)  
            f.write("Simulation: {} LENGHT: {}\n".format(i,Aux_final_lenght))
            if Aux_final_lenght < Best_final_length: 
                Best_final_length = Aux_final_lenght 
                Best_final_path = Aux_final_path.copy()
    
        f = open("../out/%s-FN.txt"%str(sys.argv[3])[12:-4], "w") 
        print("BEST LENGHT:",Best_final_length)
        print(Best_final_path[:])   
        f.close()
        
        return tour_from_path(Best_final_path) 
    elif flag == 2: #fn 
        f = open("../out/%s-FN.txt"%str(sys.argv[3])[12:-4], "w")
    
        Best_final_path =  []  
        Best_final_length = final_distance(tsp,furthest_neighbor_tour(tsp))
        for i in range (30):      
            Aux_final_path, Aux_final_lenght = Optimal_FN(tsp)  
            f.write("Simulation: {} LENGHT: {}\n".format(i,Aux_final_lenght))
            if Aux_final_lenght < Best_final_length: 
                Best_final_length = Aux_final_lenght 
                Best_final_path = Aux_final_path.copy()
    
        f.write("BEST LENGHT {}\n".format(Best_final_length))
        print("BEST LENGHT:",Best_final_length)
        print(Best_final_path[:])   
        f.close()
        
        return tour_from_path(Best_final_path) 