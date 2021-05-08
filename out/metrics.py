import scipy.stats
import sys
import numpy as np
from functools import reduce  
import statistics
path = str(sys.argv[2])

def extract_length(source): 
    for i,w in enumerate(words): 
            if w == "LENGHT:":  
                return words[i+1] 

def confident_interval_data(X, confidence = 0.95, sigma = -1):
    def S(X): #funcao para calcular o desvio padrao amostral
        s = 0
        for i in range(0,len(X)):
            s = s + (X[i] - np.mean(X))**2
        s = np.sqrt(s/(len(X)-1))
        return s
    n = len(X) # numero de elementos na amostra
    Xs = np.mean(X) # media amostral
    s = S(X) # desvio padrao amostral
    zalpha = abs(scipy.stats.norm.ppf((1 - confidence)/2))
    if(sigma != -1): # se a variancia eh conhecida
        IC1 = Xs - zalpha*sigma/np.sqrt(n)
        IC2 = Xs + zalpha*sigma/np.sqrt(n)
    else: # se a variancia eh desconhecida
        if(n >= 50): # se o tamanho da amostra eh maior do que 50
            # Usa a distribuicao normal
            IC1 = Xs - zalpha*s/np.sqrt(n)
            IC2 = Xs + zalpha*s/np.sqrt(n)
        else: # se o tamanho da amostra eh menor do que 50
            # Usa a distribuicao t de Student
            talpha = scipy.stats.t.ppf((1 + confidence) / 2., n-1)
            IC1 = Xs - talpha*s/np.sqrt(n)
            IC2 = Xs + talpha*s/np.sqrt(n)
    return  talpha*s/np.sqrt(n), np.mean(X), statistics.stdev(X)
 
all_values = []   
count = 0 
with open(path,'r') as f:
    for line in f:  
        words = line.split() 
        if "Simulation:" in words:    
            aux = float(extract_length(words))
            all_values.append(aux)  
            if count == 0: 
                bgt = aux 
                sml = aux   
                count+=1
            if aux > bgt: 
                bgt = aux 
            if aux < sml: 
                sml = aux
                       
#print(all_values[:])
conf_interval, media, desvio_padrao  = confident_interval_data(all_values,0.95) 
print(bgt) 
print(sml)
print(conf_interval) 
print(media) 
print(desvio_padrao) 
print("roun__") 
print(round(bgt,2)) 
print(round(sml,2))
print(round(conf_interval,2)) 
print(round(media,2)) 
print(round(desvio_padrao,2))