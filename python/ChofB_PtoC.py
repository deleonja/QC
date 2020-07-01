import numpy as np
from itertools import product

def change_of_basis(n, param, map_P):
	# base de Pauli:
	sx = np.array([[0,1],[1,0]])
	sy = np.array([[0,-1],[1,0]])
	sz = np.array([[1,0],[0,-1]])
	s0 = np.array([[0,0],[0,0]])
	sid = np.array([[1,0],[0,1]])

	"""
	PAULI OPERATORS FUNCTION
	N: the number of qubits
	alpha: the Pauli matrix: 1->x, 2->y, 3->z
	n: label of the qubit
	"""
	
	def S(N,alpha,n):
		if alpha == 1: #if we define the x spin operator
			if n == 0: #if we consider the first site of the chain
				Sn = np.kron(sx,np.identity(2**(N-1)))
			else: #for the rest of the chain
				Sn = np.kron(np.kron(np.identity(2**(n-1)),sx),np.identity(2**(N-n)))
		elif alpha == 2: #if we define the y spin operator
			if n == 0: #if we consider the first site of the chain
				Sn = np.kron(sy,np.identity(2**(N-1)))
			else: #for the rest of the chain
				Sn = np.kron(np.kron(np.identity(2**(n-1)),sy),np.identity(2**(N-n)))
		elif alpha == 3: #if we define the z spin operator
			if n == 0: #if we consider the first site of the chain
				Sn = np.kron(sz,np.identity(2**(N-1)))
			else: #for the rest of the chain
				Sn = np.kron(np.kron(np.identity(2**(n-1)),sz),np.identity(2**(N-n)))
		elif alpha == 0:
			Sn = np.identity(2**N)
		return Sn
	
	alpha = [0,1,2,3]
	R = np.array(list(product(alpha, repeat=(n))))
	
	base_Pauli = np.zeros((4**n, 4**n))

	for i in range(4**n):
		dummy = np.identity(2**n)
		for j in range(n):
			dummy = dummy @ S(n,R[i][j],j+1)
		base_Pauli[i] = dummy.reshape(4**n)
	
	# matriz de cambio de base de la b. de Pauli a la b. computacional:
	M_cb_PaC = np.column_stack(base_Pauli)

	# matriz inversa de M_cb_PaC
	M_cb_PaC_inv = np.linalg.inv(M_cb_PaC)

	# en map_C se almacenarán los mapeos en la b. computacional:
	map_C = np.zeros((param, 4**n, 4**n)) 

	for i in range(param):
		map_C[i] = np.dot(M_cb_PaC, np.dot(map_P[i], M_cb_PaC_inv))
	
	return map_C
