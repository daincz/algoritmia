#! /usr/bin/python

########################################
## Codigos de Huffman con uso de heap ##
########################################
## Diana Cruz
## UART - UNPA

from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, freq):
	num = count()
	
	trees = list(zip(freq, num, seq))  #num asegura el orden valido

	heapify(trees)   ## min heap organizado por la frecuencia
	while len(trees)>1:
		fa, _, a = heappop(trees)  ## extract min
		fb, _, b = heappop(trees)  ## extract min
		n = next(num)
		heappush(trees, (fa+fb, n, [a, b]))  ## insert del nuevo nuevo combinado de a y b
	return trees[0][-1]


def isleaf(tree):
	return len(tree)==1 


def codes(s, tree):
	
	encoding = []
	current_branch = tree
	
	while not isleaf(current_branch):
		if s in current_branch[0]:
			encoding.append(0)
			current_branch = current_branch[0]
		elif s in current_branch[1]:
			encoding.append(1)
			current_branch = current_branch[1]
		elif not isleaf(current_branch[0]):
			encoding.append(0)
			current_branch = current_branch[0]
		elif not isleaf(current_branch[1]):
			encoding.append(1)
			current_branch = current_branch[1]

	return encoding
		
## Pruebas		
if __name__ == '__main__':		
	print "Datos de entrada del algoritmo"
	seq = "abcd"
	frq = [65, 3, 20, 37]
	print "simbolos:", seq
	print "frecuencias:", frq

	result = huffman(seq, frq)
	print result
	print "Codigos de Huffman"
	for i in range(len(seq)):
		print seq[i], codes(seq[i],result)
	
