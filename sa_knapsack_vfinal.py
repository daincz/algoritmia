#! /usr/bin/python

#####################################
## Knapsack -- Simulated Annealing ##
#####################################
## Diana Cruz
## UART - UNPA
## version final

import random
import math

COOLING_FRACTION = 0.995

def init_solution(weight_cost, max_weight):

    ## generacion de solucion inicial aleatoria mientras sea menor que el max_weight

	solution = [0]*len(weight_cost)
	allowed_positions = range(len(weight_cost))
	while len(allowed_positions) > 0:
		idx = random.randint(0, len(allowed_positions) - 1)
		selected_position = allowed_positions.pop(idx)
		solution_new = [x for x in solution]
		solution_new[selected_position] = solution_new[selected_position] + 1
		if get_weight_and_cost(solution_new, weight_cost)[0] <= max_weight:
			solution = [x for x in solution_new]
		else: 
			break
	return solution

def get_weight_and_cost(solution, weight_cost):
	cost, weight = 0, 0
	for item in range(len(solution)):
		k = solution[item]
		weight += (k*weight_cost[item][0])
		cost += (k*weight_cost[item][1])
	return weight, cost

def neigborn_random(solution, weight_cost, C):
	snew = [x for x in solution]
	idx = random.randint(0, len(weight_cost) - 1)
	snew[idx] = 1			
	'''
	si con el nuevo objeto insertado en la mochila supera la capacidad
	se saca intercambia por otro objeto que esta en la mochila
	'''
	if (get_weight_and_cost(snew, weight_cost)[0] > C):  
		
		seleccionado = False
		isel=0
		wcurrent = get_weight_and_cost(snew, weight_cost)[0]
		p = range(len(weight_cost))
		
		p.remove(idx)
		while  not seleccionado and len(p)!=0:
			isel = random.choice(p)
			'''
			si al sacar un objeto existente en la mochila permite
			que el nuevo objeto no supere la capacidad de la mochila
			entonces selecciona objeto a eliminar de la solucion anterior
			'''
			if (snew[isel] != 0) and (wcurrent - weight_cost[isel][0] <= C):
				seleccionado = True
			p.remove(isel)
		if len(p) == 0:
			snew[idx] = 0
		else:
			snew[isel] = 0
	
	return snew
	


def SA_Knapsack(A, C, imax=200):
	
	sa = [0]*len(A)
	#sa = init_solution(A, C)  # solucion inicial aleatoria
	print "solucion aleatoria inicial:", sa, "peso total:", get_weight_and_cost(sa, A)[0], "costo total:", get_weight_and_cost(sa, A)[1]
	#sb = sa
	sb = [x for x in sa]
	best_cost = get_weight_and_cost(sb, A)[1]
	Ta = C
	wactual = 0
	
	for i in range(imax):
		
		# se selecciona de forma aleatoria una solucion vecina a sa
		snew = neigborn_random(sa, A, C)  
		
		if get_weight_and_cost(snew, A)[1] >= best_cost:
			sa = [x for x in snew]
			sb = [x for x in sa]
			best_cost = get_weight_and_cost(sb, A)[1]
			print i, "mejor soluc: ", sb, best_cost
			
		else:
			delta = get_weight_and_cost(sa, A)[1] - get_weight_and_cost(snew, A)[1]
			aleat = random.random()
			if math.exp(float(delta) / float(Ta)) > aleat:
				sa = [x for x in snew]

		Ta *= COOLING_FRACTION  # nueva temperatura
		
	best_weight, best_cost = get_weight_and_cost(sb, A)

	return best_weight, best_cost, sb
	

if __name__ == '__main__':
		
	C = 100
	# A = [(w, v)]  w:weight  v:value
	A = [(10, 20), (20, 30), (30, 66), (40, 40), (50, 60)]
	print "Problema de la Mochila:"
	print "-----------------------"
	print "Capacidad Maxima:", C
	print "Elementos:", A
	weight, cost, result = SA_Knapsack(A, C, 30)
	
	print "\nSolucion optima obtenida con metodo Simulated Annealing"
	print "---------------------------------------------------------"
	print "Elementos en la Mochila: ", result
	print "Costo total de Elementos en mochila: ", cost
	print "Capacidad utilizada: ", weight
	print "Capacidad libre: ", C - weight
	
