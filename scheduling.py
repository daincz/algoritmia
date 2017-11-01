#! /usr/bin/python

####################################
## Scheduling - Estrategia Greedy ##
####################################
## Diana Cruz
## UART - UNPA


from heapq import heapify, heappush, heappop

def sheduling_optimal(P):
	heapify(P);      # min heap organizado por tiempos
	solution = []
	tmin = 0
	n = len(P)
	print n
	for i in range(len(P)):
		x = heappop(P)
		k = i + 1
		tmin += ((n-k+1)*x[0])
		solution.append(x)
	return tmin, solution

## Pruebas
if __name__ == '__main__':
	## T=[(ti, i)]  ti tiempo requerido por el cliente i 
	T = [(5,1),(10,2),(3,3)]   ## ejemplo analizado en Brassard

	print "Un sistema presenta la siguiente planificacion de atencion"
	for i in range(len(T)):
		print "Cliente ", T[i][1], ": ", T[i][0]
		
	toptimo, Pnew = sheduling_optimal(T)
	print "Planificacion optima con un tiempo total de atencion de", toptimo
	print "Orden	Cliente	Tiempo"
	for i in range(len(Pnew)):
		print i+1, "	", Pnew[i][1], "	", Pnew[i][0] 
		
