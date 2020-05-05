import numpy as np
from itertools import combinations
from itertools import product

def R(n, num_of_corr):
	r_index = list(range(4**n-1))

	positions = list(combinations(r_index, num_of_corr))

	r = np.zeros((len(positions),4**n))

	for i in range(len(positions)):
		r[i][0] = 1
		for j in positions[i]:
			r[i][j+1] = 1
	return r
	
r = R(3,3)

print(r[10])

'''	
r = R(3, 3)

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
'''			
	
	
# 1 2 3, 4 8 12, 16 32 48
