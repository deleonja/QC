import numpy as np
from itertools import product
from analisis2 import R

r = R(3, 3)

counter = 0

qubits_positions = np.zeros((3,3))

# Guardar los indices de r en donde se encuentran las corr. no
# cruzadas de cada qbit en el arreglo qubits_positions
for i in range(3):
	for j in range(3):
		qubits_positions[i][j] = 4**i*(j+1)
		
print(qubits_positions)

print('número de rs = ' + str(r.shape[0]))
		
# Encontrar las r's en las que sólo se repiten combinaciones 
# de lo que es válido para 1 qbit
for k in range(r.shape[0]):
	qubits_corr = np.zeros((3,3))
	norms = np.zeros(3)
	for i in range(3):
		for j in range(3):
			qubits_corr[i][j] = r[k][int(qubits_positions[i][j])]
		norms[i] = np.dot(qubits_corr[i],qubits_corr[i])
	for elem in [[1,1,1]]:#list(product([0,1,3], repeat=3))[1:]:
		contador = 0
		for i in range(3): 
			if norms[i] == elem[i]:
				contador = contador + 1
			else: 
				break
		if contador == 3:
			print(k)
			counter = counter + 1

print(counter)
