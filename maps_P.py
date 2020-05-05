import numpy as np
from itertools import product
import analisis2

def maps(n, param, num_of_corr):
	r = analisis2.R(n, num_of_corr)
	
	map_P = np.zeros((param, 4**n, 4**n))
	print(r[10])
	for i in range(param): # se generan todos los posibles mapeos     2**(4**n-1)
		for j in range(4**n):
			map_P[i][j][j] = r[i][j] 
	
	print(map_P[10])
	print() 
	return map_P
