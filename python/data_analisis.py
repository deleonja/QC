import numpy as np

r = np.load('3qbits-4_corr_invariant-corr_of_QC.npy')

comb = np.load('3qbits-4_corr_invariant-combinations_of_norms.npy')

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
	for elem in [[0,0,0]]:
		#print(elem)
		if norms[0] == elem[0] and norms[1] == elem[1] and norms[2] == elem[2]:
			if r[k][25] == 1:
				print(r[k])
				print()
				counter = counter + 1
#print(r.shape)
print(counter)
