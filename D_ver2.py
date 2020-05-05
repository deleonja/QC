import numpy as np 

def D(n, a)
	dim = 2**n

	D = np.zeros((4**n,4**n))

	l = []
	for i in range(int(np.sqrt(4**n))):
		l.append(2**n*i)

	for i in l:
		for k in l:
			for j in range(dim):
				D[i+j][k:k+dim] = a[i+j].reshape((dim,dim))[j]
	return D
	
def D(n, param, map_C):
		
	# M_dinamica almacenará todas las matrices dinámicas correspondientes
	# a todos los mapeos que se encuentren en map_C
	M_dinamica = np.zeros((param, 4**n, 4**n))
	
	# calcular todas las matrices dinámicas:
	for i in range(param):
		print(i)
		M_dinamica[i] = D(map_C[i],2**n)
		
	return M_dinamica
