import maps_P
import ChofB_PtoC
import D_matrix
import verify_CP
import analisis2
import numpy as np
from itertools import product
import sys

np.set_printoptions(threshold=sys.maxsize)

n = 3
param = 39711
num_of_corr = 3

MAP = maps_P.maps(n, param, num_of_corr)
print('ya calculé los mapeos en la base de P')
MAP_C = ChofB_PtoC.change_of_basis(n, param, MAP)
print('ya hice el cambio de base')
D = D_matrix.D(n, param, MAP_C)
print('ya calculé la matriz dinámica')

print(MAP_C[10])
print()
print(D[10])

r = analisis2.R(n, num_of_corr)


cantidad_CC = 0

#rho = np.array([4,2-2j,2-2j,-2j,2+2j,0,2,0,2+2j,2,0,0,2j,0,0,0])

f = open(str(n)+'qbits_new.QC', mode = 'w', encoding='utf-8')

index = []
for i in range(param):
	if verify_CP.CP(D[i]) == True:
		cantidad_CC = cantidad_CC + 1
		index.append(i)
		#f.write('rho_f = ' + str(np.dot(MAP_C[i],rho)) + '\n')
		#f.write(str(map_P[i]) + '\n\n')
		#f.write(str(map_C[i]) + '\n\n')
		#f.write(str(M_dinamica[i]) + '\n\n\n')

print(cantidad_CC)

for i in index:
	print(r[i])
'''		
for i in range(16):
	print(i)
	for j in range(cantidad_CC):
		if np.dot(R[j], R[j]) == i+1:
			l = 0
			for k in range(16):
				f.write(str(int(R[j][k])) + ' ')
				l += 1
				if l == 4:
					l = 0
					f.write('\n')
				if k == 15: 
					f.write('\n')
'''
			
'''
for i in range(cantidad_CC):
	l = 0
	for j in range(16):
		f.write(str(int(R[i][j])) + ' ')
		l += 1
		if l == 4:
			l = 0
			f.write('\n')
		if j == 15: 
			f.write('\n')

f.write('\nCanales cuánticos de '+str(n)+' qubits que borran 1 correlaciones = '+str(cantidad_CC))
'''
f.close()
