from numpy       import array   
import numpy as np   
from collections import deque
import matplotlib.pyplot as plt   
import time

class EUC_2D: 
    def __init__(self,id,x1,y1):  
        self.id = id 
        self.x = x1  
        self.y = y1  
   
class Improver:  
    def __init__(self): 
        self.NNpath = []
        self.path = []  
        self.coordinates = [] 

    def driver2opt(self, path, dimension, tour): 
        count = 0  

        tspfile = open(path,'r')  
        for i in range(1,7): 
            line  = tspfile.readline()
        for n in range(1, dimension+1):
             
             line  = tspfile.readline()
             words = line.split()
             id = int(words[0]) 
             x = float(words[1]) 
             y = float(words[2])
             self.coordinates.append(EUC_2D(id,x,y))
            
        tspfile.close()  
        # for i in self.coordinates: 
        #     print(i.id, i.x, i.y)  
        
        return self.init_path(tour)

    def distance(self,x1,y1,x2,y2): 
        distance = np.hypot(x1-x2, y1-y2) 
        return float(distance)
   

    def get_distance(self,a,b):  
        Xa=Ya=Xb=Yb = 0 
        for i in self.coordinates: 
            if(i.id == a): 
                Xa = i.x   
                Ya  = i.y   
            if(i.id == b): 
                Xb = i.x   
                Yb  = i.y    
        return self.distance(Xa,Ya,Xb,Yb) 


 

    
    #total distance
    def tour_from_path_kopt(self, path):  
  
        path.append(path[0])
        return path 

    def path_length(self, path):  
        #count if recursion 

        if len(path) == 1: 
            return 0 
        else: 
            start_node = path.pop()
            next_node = path[-1] 
            return self.get_distance(start_node,next_node) + self.path_length(path)

    
    def calc_k2opt(self, path): 
        aux_path = [] 
        aux_path = path.copy()
        return self.path_length(aux_path)

    def init_path(self, tour): 
        print("Init path from 2opt")

       
        self.path = tour.copy() 
        self.NNpath = tour.copy()   
        print(self.NNpath[:])
       
        self.NNdistance = self.calc_k2opt(self.NNpath)
        
        print("Lenght construtive heuristic calc:",self.NNdistance)  
        
        return self.improvement_solution() 

    
        
    def Swap(self, path, x, y): 
        path[x + 1: y+1] = path[x + 1: y+1][::-1]
        return path   

    def LS_2opt(self, path): 
        min_cost = 0  
        tam = len(path)   


        for i in range(tam - 2): 
            for j in range(i+2, tam -1): 
                #print("loop")
                actual_cost = self.get_distance(path[i],path[i+1]) + self.get_distance(path[j],path[j+1])   
                new_cost =  self.get_distance(path[i],path[j]) + self.get_distance(path[i+1],path[j+1]) 
                change = new_cost - actual_cost  
                if change < min_cost: 
                    min_cost = change  
                    min_i = i  
                    min_j = j  
        if min_cost < 0:  
                #path[min_i + 1: min_j+1] = path[min_i + 1: min_j+1][::-1]
                self.Swap(path, min_i, min_j)

        return  path



    def improvement_solution(self): 
        initial_time = time.time() 

        final_solution_enhanced = self.NNpath.copy()
        change = 1 
        flag = False    
        count = 0 
          
        while flag == False:    

            elapsed = time.time() -  initial_time
            initial = self.calc_k2opt(final_solution_enhanced)    
            final_solution_enhanced = self.LS_2opt(final_solution_enhanced)   
            final = self.calc_k2opt(final_solution_enhanced) 
            print("inicial: {} | final: {}".format(initial,final))
            change = np.abs(final - initial) 
              
            if( change == 0 ):  
                count +=1    
            total_time = elapsed/ 180  
            if count == 9 or  total_time >= 3: 
                flag = True
            
        return final_solution_enhanced, final