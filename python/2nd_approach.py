import numpy as np
from itertools import combinations
from itertools import product
import functions as f 

r = f.combinations_of_correlations(3, 3)

counter = 0

qubits_positions = np.zeros((3,3))

for i in range(3):
	for j in range(3):
		qubits_positions[i][j] = 4**i*(j+1)
		
for k in range(r.shape[0]):
	qubits_corr = np.zeros((3,3))
	norms = np.zeros(3)
	for i in range(3):
		for j in range(3):
			qubits_corr[i][j] = r[k][int(qubits_positions[i][j])]
		norms[i] = np.dot(qubits_corr[i],qubits_corr[i])
	for elem in list(product([0,1,2,3], repeat=3))[1:22]:
		#print(elem)
		if norms[0] == elem[0] and norms[1] == elem[1] and norms[2] == elem[2]:
			#print(r[k])
			counter = counter + 1

print(counter)

a = list(product([0,1,3], repeat=3))
indexes = []

for j in range(len(a)):
    sum = 0
    for i in range(3):
        sum = sum + a[j][i]
    if sum <= 3:
        indexes.append(j)