#! /usr/bin/python

##################################
## Storage -- Estrategia Greedy ##
##################################
## Diana Cruz
## UART - UNPA

from heapq import heapify, heappush, heappop

def storage_optimal(P, Cmax):
	'''
	 P lista de espacio de almacenamiento requerido por cada programa
	 C Capacidad maxima del disco
	'''
	
	heapify(P)  # min heap organizado por espacios de almacenamiento
	solution = []
	stotal = 0
	pcounter = 0
	while len(P)>0 and stotal < Cmax:
		x = heappop(P)    # estract min 
		if(stotal + x[0] <= Cmax):
			stotal += x[0]
			pcounter+=1
			solution.append(x)
		else:
			break
			
	return pcounter, stotal, solution		 
	
## Pruebas
if __name__ == '__main__':

	P = [(650, 'Prog 1'), (196, 'Prog 2'), (156, 'Prog 3'), (592, 'Prog 4'), (87, 'Prog 5'), (498, 'Prog 6'), (241, 'Prog 7')]
	D = 1500

	print "Se requieren almacenar los siguientes programas:"
	print P
	print "La capacidad maxima del Disco es de", D, "kilobytes\n\n"


	cant, s, Pnew = storage_optimal(P, D)

	print "Almacenamiento Optimo maximizando el numero de programas"
	print "---------------------"
	print "Cantidad maxima: ", cant, "programas" 
	print "Lista de programas elegidos:", Pnew 
	print "Capacidad utilizada:", s, "kilobytes"
	print "Capacidad libre:", D-s, "kilobytes"
	
	
