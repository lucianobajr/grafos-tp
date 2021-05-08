def cleanFiles():
    arq1 = open("../out/saida.txt", "a")
    arq1.truncate(0)
    arq1.close()
    arq2 = open("../out/arestas_retorno.txt", "a")
    arq2.truncate(0)
    arq2.close()