# Biblioteca CCF 331 - TEORIA E MODELO DE GRAFOS

## Problema do Caixeiro Viajante

Problema do Caixeiro Viajante (PCV) mundialmente conhecido
como Travelling Salesman Problem (TSP) consiste em um
problema de determinação de rota com o menor custo para um
vendedor cujo proposito é visitar um conjunto finito de cidades.
Para tal, deve-se determinar a menor rota para percorrer tais
cidades (visitando uma única vez cada uma delas) e retornando
à cidade de origem. No domı́nio da teoria dos grafos (Figura
4), cada cidade é identificada com um nó (ou vértice) e as rotas
que ligam cada par de nós são os arcos/arestas. Cada uma das
arestas terá como peso associado a distância correspondente.
Desde que seja possı́vel ir diretamente de uma cidade para qual-
quer outra, o gráfico diz-se completo. Uma viagem que passe
por todas as cidades corresponde a um ciclo Hamiltoniano, rep-
resentado por um conjunto especı́fico de linhas.

![1](https://user-images.githubusercontent.com/45442173/117540093-d9b6b980-afe3-11eb-9de8-e8ea8fb8b0e4.jpeg)    


## Integração do algoritmo com o https://github.com/lucianobajr/grafos-tp/tree/tp-01

![Untitled](https://user-images.githubusercontent.com/45442173/117540099-dfac9a80-afe3-11eb-9e1c-d6c7b4cc325a.png)

### A estruturação da biblioteca segue o esquema a seguir:


    ├── __test__                  # testes da aplicação
    ├── data                      # arquivos de teste
    │   ├── json                    # diretório com arquivos .json
    │   ├── txt                     # diretório com arquivos .txt
    │   ├── tsp                     # diretório com arquivos .tsp    
    │   ├── generateTeste.py        # programa para gerar .txts para testes
    ├── doc                       # Documentação
    ├── out                       # resultados
    │   ├── saida.txt               # informações obtidas do grafo durante a execução   
    │   ├── teste.txt               # arestas de retorno do DFS   
    │   ├── metrics.py              # gera as métricas de cada heurística
    ├── src                       # códigos fonte
    │   ├── Class                   # Classes da aplicação    
    │   ├── package                 # Heurísticas da aplicação
    │   ├── tools                   # Ferramentas da aplicação
    │   ├── util                    # Função que gera os resultados das Heurísticas 
    │   ├── menu.py                 # menu da aplicação 
    │   ├── makefile                # makefile para compilar a aplicação 
    │   ├── main.py                 # arquivo principal da aplicação
    │   