import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

def dynMatrix(map, n):
	i = -1
	j = 0
	k = -1
	l = 0 
	p = 0
	DM = np.zeros((n**2,n**2))
	for x in range(n**2): #filas
		for y in range(n**2): #columnas
			i += 1
			DM[[l],[i]] = map[[x],[y]]
			if (i + 1) % n == 0:
				i = k
				l += 1	
		k = k + n
		l = p
		if ((x + 1)% n == 0):
			p = p + n
			l = p
		if (k % (n**2 - 1)) == 0:
			k = -1		
		i = k
	return DM

def dynMatrix2(a, n):
	dim = 2**n

	D = np.zeros((4**n,4**n))
				
	k = 0
	p = 0
	for i in range(4**n):
		if i % dim == 0 and i != 0:
			k = k + 1
			p = 0
		for j in range(dim):
			D[i][dim*j:dim*(j+1)] = a[dim*k+j].reshape((dim,dim))[p]
		p = p + 1
	return D

def D(n, param, map_C):
		
	# M_dinamica almacenará todas las matrices dinámicas correspondientes
	# a todos los mapeos que se encuentren en map_C
	M_dinamica = np.zeros((param, 4**n, 4**n))
	
	# calcular todas las matrices dinámicas:
	for i in range(param):
		print(i)
		M_dinamica[i] = dynMatrix2(map_C[i],n)
		
	return M_dinamica
