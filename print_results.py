import numpy as np
from numpy import linalg as la
from itertools import product

a = [0,1]
r = np.array(list(product(a, repeat=(4**n - 1))))

def print_results(n, param, M_dinamica):
	f = open(str(n)+'_cc.'+str(param), mode = 'w', encoding='utf-8')
	for i in range(param):
		smallest_eig = chop(np.linalg.eigh(M_dinamica[i])[0])[0]
		if np.array_equal(M_dinamica[i],M_dinamica[i].transpose()) == True and smallest_eig >= 0:
			cantidad_CC = cantidad_CC + 1
			f.write(str(r[i]) + '\n')
			#f.write(str(map_P[i]) + '\n\n')
			#f.write(str(map_C[i]) + '\n\n')
			#f.write(str(M_dinamica[i]) + '\n\n\n')
	
	data_file.write('Canales cuánticos que borran '+str(param)+' corr. = '+str(cantidad_CC))
	data_file.close()
	return
