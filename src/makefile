INPUT_TXT=../data/txt/teste3.txt
INPUT_JSON=../data/json/grafo.json
INPUT_SALESMAN=../data/tsp/ulysses16.tsp

MAIN = main.py

all:
	python3 $(MAIN) -o -normal $(INPUT_TXT) 

nn:
	python3 $(MAIN) -o -nn $(INPUT_SALESMAN)

fn:
	python3 $(MAIN) -o -fn $(INPUT_SALESMAN) 

windows:
	python $(MAIN) -o -normal $(INPUT_TXT)

windows_nn:
	python $(MAIN) -o -nn $(INPUT_SALESMAN)

windows_fn:
	python $(MAIN) -o -fn $(INPUT_SALESMAN)