INPUT_TXT=../data/txt/teste3.txt
INPUT_JSON=../data/json/grafo.json
INPUT_SALESMAN=../data/tsp/ulysses16.tsp
INPUT_METRICS=../out/berlin52-FN.txt

MAIN = main.py
METRICS = ../out/metrics.py

all:
	python3 $(MAIN) -o -normal $(INPUT_TXT) 

nn:
	python3 $(MAIN) -o -nn $(INPUT_SALESMAN)

fn:
	python3 $(MAIN) -o -fn $(INPUT_SALESMAN)

metrics:
	python3 $(METRICS) -o $(INPUT_METRICS)

windows:
	python main.py -o -normal ../data/txt/teste3.txt

windows_nn:
	python main.py -o -nn ../data/tsp/ulysses16.tsp

windows_fn:
	python main.py -o -fn ../data/tsp/ulysses16.tsp

windows_metrics:
	python3 ../out/metrics.py -o ../out/berlin52-FN.txt