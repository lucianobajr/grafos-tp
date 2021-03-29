#codigo pra gerar testes  

import random 
n = int(input("Entre com o tamanho do grafo"))   
count = 0 
name = 'teste{}.txt'.format(n)
fl = open(name,'w+') 
fl.write("%d\n"%(n))
while count <= n+n: 
    node1 = random.randint(0,n) 
    node2 = random.randint(0,n) 
    while(node1 == node2): 
        node1 = random.randint(0,n) 
        node2 = random.randint(0,n)
    weight = random.int(0,20) 

    fl.write("%d %d %d\n"%(node1,node2,weight))   
    count+=1
    
