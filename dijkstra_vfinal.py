#!/usr/bin/env python

####################################
## Dijkstra - Greedy con min heap ##
####################################
## Diana Cruz
## UART - UNPA
## version 2

from heapq import heappush, heappop, heapify

oo = 10000    #infinito
    
def dijkstra(src, graph):
    n = len(graph)
    dist = [oo] * n
    heap = []   # min heap organizado por node.d
    
    heappush(heap, [0, src])  # se inserta el nodo inicial al heap vacio
    p = range(n) # visitados
    print p
    while not len(heap) == 0:  # heap no es vacio
		node = heappop(heap) 
		if node[0] > dist[node[1]]: continue
		  
		dist[node[1]] = node[0] 
		p[node[1]] = -1 # nodo visitado
		for i in p:
			if i == -1: continue
			if dist[i] > dist[node[1]] + graph[node[1]][i]:
				heappush(heap, [dist[node[1]] + graph[node[1]][i], i])
    return dist

if __name__ == '__main__':
	v = ['a','b','c','d','e','f','g','h','i','j']
	graph = [[oo, 10, 15, oo, 17, oo, oo, oo, oo, oo],
			 [10, oo, oo, 21, oo, oo, oo, oo, oo, oo],
			 [15, oo, oo,  3, oo, oo, 20, oo, oo, oo],
			 [oo, 21,  3, oo, oo, oo, oo, oo, oo, oo],
			 [17, oo, oo, oo, oo, 12, oo, 13, 10, oo],
			 [oo, oo, oo, oo, 12, oo,  7,  8, oo, 12],
			 [oo, oo, 20, oo, oo,  7, oo, oo, oo, 17],
			 [oo, oo, oo, oo, 13,  8, oo, oo,  5,  9],
			 [oo, oo, oo, oo, 10, oo, oo,  5, oo, oo],
			 [oo, oo, oo, oo, oo, 12, 17,  9, oo, oo]]
	#print dijkstra(0, graph)
	
	for i in range(len(graph)):
		print "Distancia desde vertice", v[i]
		print dijkstra(i, graph)
	
