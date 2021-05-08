import sys
import re
import json
import networkx as nx
import matplotlib.pyplot as plt
from math import floor
from menu import simpleMenu, pause 
from Class.bcolors import bcolors
from Class.Graph import Graph
from util.tour import util_final_tour

from tools.rules import cleanFiles
from tools.tsp import *
sys.setrecursionlimit(10**6)

# ------------------------------------TSP Files------------------------------------
#  Abrimos o arquivo TSP e colocamos cada linha sem espaços
#  e caracteres de nova linha em uma lista      

def produce_final(file=str(sys.argv[3])):
    data = read_tsp_data(file)
    
    if str(sys.argv[2])[1:]=='nn':
        return to_init_graph(data, util_final_tour(data,1))
    else:
        return to_init_graph(data, util_final_tour(data,2))
    
# ______________________________________Driver___________________________________________
if __name__ == "__main__":
    cleanFiles()
    if((str(sys.argv[3])[8:].split(".")[1] == "txt") or (str(sys.argv[3])[8:].split(".")[1] == "json")):
        with open(str(sys.argv[3]), 'r') as file_input:
            V = 0
            read_file = None
            if str(sys.argv[3])[8:].split(".")[1] == "txt":
                V = file_input.readline()
            else:
                read_file = json.load(file_input)
                V = read_file['data']['nodes']['length']

            graph = Graph(int(V)+1)

            if str(sys.argv[3])[8:].split(".")[1] == "txt":
                while True:
                    try:
                        file_line = file_input.readline()
                        if not file_line:
                            break
                        else:
                            item = file_line.split(" ")
                            graph.add_edge(int(item[0]), int(
                                item[1]), float(item[2]))
                    except:
                        print("Erro ao inserir Aresta")
            else:
                lines = read_file['data']['edges']['_data']
                for i in range(len(lines)):
                    line = lines["{}".format(i+1)]
                    graph.add_edge(int(line['from']), int(
                        line['to']), float(line['label']))
    else:
        res = produce_final()
        V=len(res)
        graph = Graph(V+1)

        for item in res:
            try:
                graph.add_edge(item[0], item[1], item[2])
            except:
                print("Erro ao inserir Aresta")
    
    def option_1(): 
        arq = open("../out/saida.txt","a")       
        arq.write("\n--------------------------------------------------\n")
        arq.write("\nO grafo tem ordem {}\n".format(graph.get_order())) 
        arq.close()
        print("\nO grafo tem ordem {}\n".format(graph.get_order()))
        pause()

    def option_2(): 
        arq = open("../out/saida.txt","a")      
        arq.write("\n--------------------------------------------------\n")
        arq.write("\nO grafo tem tamanho {}\n".format(graph.sizeOfGraph())) 
        arq.close()
        print("\nO grafo tem tamanho {}\n".format(graph.sizeOfGraph()))
        pause()

    def option_3():
        vertex = int(input("Digite o vertice: "))
        graph.Neighbor_by_vertex(vertex)
        pause()

    def option_4():
        vertex = int(input("Digite o vertice: "))
        arq = open("../out/saida.txt","a")      
        print("\nO vértice {} tem grau {}\n".format(vertex, graph.findDegree(vertex)))  
        arq.write("\n--------------------------------------------------\n")
        arq.write("\nO vértice {} tem grau {}\n".format(vertex, graph.findDegree(vertex))) 
        arq.close()
        pause()

    def option_5():
        vertex = int(input("Digite o vertice (DFS): "))
        graph.DFS(vertex)
        pause()

    def option_6():
        print(graph.connectedComponents())
        print("\nO número de componentes conexas é: {} \n".format(len(graph.connectedComponents())))
        arq = open("../out/saida.txt","a")
        arq.write("\n--------------------------------------------------\n")
        arq.write("Componentes conexos do grafo: {}".format(graph.connectedComponents()))
        arq.write("\nO número de componentes conexas é: {} \n".format(len(graph.connectedComponents())))
        pause()

    def option_7():
        vertex = int(input("Digite o vertice: "))
        graph.findArtpoint(vertex)
        pause()

    def option_8():
        u = int(input("Digite um vértice (u): "))
        v = int(input("Digite um vértice (v): "))
        m = [u,v]
        response =  graph.findBridges(m)

        if response: 
            arq = open("../out/saida.txt","a")
            arq.write("\n--------------------------------------------------\n")    
            arq.write("{}-{} é uma ponte.".format(u,v)) 
            arq.close()
            print("A aresta é ponte!")
        else:
            print("A aresta não é ponte!") 
            arq = open("../out/saida.txt","a")
            arq.write("\n--------------------------------------------------\n")    
            arq.write("A aresta inserida não é uma ponte.") 
            arq.close()
        pause() 

    def option_9():
        pos=nx.random_layout(graph.G) 
        fig = plt.figure(figsize=(40, 40), dpi= 70)  
        plt.clf() 
        nx.draw_networkx(graph.G,pos,node_color='yellowgreen') 
        labels = nx.get_edge_attributes(graph.G,'weight') 
        nx.draw_networkx_edge_labels(graph.G,pos,edge_labels=labels) 
        plt.show() 
    
    def option_10(): 
        graph.print_graph() 
        pause()

    sMenu = simpleMenu(f'{bcolors.Branco}TRABALHO GRAFOS{bcolors.Reset}')
    sMenu.spacing = [ '0','d' ]
    sMenu.menu_option_add(option_1,'Retornar a ordem do grafo')
    sMenu.menu_option_add(option_2,'Determinar o tamanho do grafo')
    sMenu.menu_option_add(option_3,'Retornar os vizinhos de um vértice fornecido')
    sMenu.menu_option_add(option_4,'Determinar o grau de um vértice fornecido')
    sMenu.menu_option_add(option_5,'Determinar a sequência de vértices visitados na busca em profundidade e informar a(s) aresta(s) de retorno')
    sMenu.menu_option_add(option_6,'Determinar o número de componentes conexas do grafo e os vértices de cada componente')
    sMenu.menu_option_add(option_7,'Verificar se um vértice é articulação')
    sMenu.menu_option_add(option_8,'Verificar se uma aresta á ponte')
    sMenu.menu_option_add(option_9,'Visualizar o grafo') 
    sMenu.menu_option_add(option_10,'printar grafo na linha de comando') 
    
    sMenu.menu_start() 