'''
	IMPORTANTE: en la última línea de cógido se encuentra la línea de código con la que se corre este programa en el bash
	
	¿Qué falta por hacer?
	- Idear una manera de no tener problema de RAM para n >= 3.
	- Idear una manera de organizar los datos. 
	
	Programa: Verificación de los mapeos que borran correlaciones de n qubits
	Autor: José Alfredo de León
	09.03.2020
	
	Este programa pretende calcular todos los mapeos que borran cualquier coordenada o combinaciones de estas de la super esfera de Bloch
	de un sistema de n qubits. Así también, verifica cuáles de estos mapeos son canales cuánticos físicos. 
'''
# 1, 2, 4, 7, 16, 32

import numpy as np
from numpy import linalg as la
from itertools import product
import sys
np.set_printoptions(threshold=sys.maxsize)
'''
1 Generar los mapeos en la base de Pauli
'''

#n = int(np.loadtxt('n.dat', unpack=True))
n = 2
param = 1 #  2**(4**n-1), cantidad de mapeos a manipular

#a = [0,1]
#r = np.array(list(product(a, repeat=(4**n - 1))))

#r = np.zeros((63,63))

r = np.zeros((1,15))
r[0][0] = 1

#for i in range(63):
#	r[i][i] = 1

# en map_P se almacenarán los mapeos en la base de Pauli
map_P = np.zeros((param, 4**n, 4**n)) # 2**(4**n-1), 


for i in range(param): # se generan todos los posibles mapeos     2**(4**n-1)
	map_P[i][0][0] = 1
	for j in range(4**n - 1):
		map_P[i][j+1][j+1] = r[i][j] 

'''
2 Hacer cambio de base a la base computacional
'''
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
	map_C[i] = np.dot(M_cb_PaC_inv, np.dot(map_P[i], M_cb_PaC))


print(np.dot(map_C[0], np.ones((16))))


'''
3 Calcular la matriz dinámica:
'''
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
	
# M_dinamica almacenará todas las matrices dinámicas correspondientes
# a todos los mapeos que se encuentren en map_C
M_dinamica = np.zeros((param, 4**n, 4**n))

# calcular todas las matrices dinámicas:
for i in range(param):
	M_dinamica[i] = dynMatrix(map_C[i],2**n)

'''
4 Verificar positividad
'''
def chop(expr, *, max=1e-10):
	return [i if abs(i) > max else 0 for i in expr]


cantidad_CC = 0

print(np.array_equal(M_dinamica[i],M_dinamica[i].transpose()))
print(chop(np.linalg.eigh(M_dinamica[0])[0])[0])

'''
f = open('PRUEBA_z1.txt', mode = 'w')

f.write(str(map_P[0]))
f.write(str(map_C[0]))
f.write(str(M_dinamica[0]))

for j in range(16):
	for k in range(16):
		f.write(str(int(map_P[0][j][k])) + ' ')
	f.write('\n')
f.write('\n')

for j in range(16):
	for k in range(16):
		f.write(str(map_C[0][j][k]) + ' ')
	f.write('\n')
f.write('\n')
	
for j in range(16):
	for k in range(16):
		f.write(str(M_dinamica[0][j][k]) + ' ')
	f.write('\n')
f.write('\n')
f.close()
'''

rho = np.array([4,2-2j,2-2j,-2j,2+2j,0,2,0,2+2j,2,0,0,2j,0,0,0])

print(str(map_P[0]) + '\n')

print(str(map_C[0]) + '\n')

print(np.dot(map_C[0],rho))

'''
data_file = open(str(n)+'_cc.'+str(param), mode = 'w', encoding='utf-8')
for i in range(param):
	smaller_eig = chop(np.linalg.eigh(M_dinamica[i])[0])[0]
	#print(str(smaller_eig >= 0))
	#print(str(np.array_equal(M_dinamica[i],M_dinamica[i].transpose())) + '\n\n')
	#print(np.array_equal(M_dinamica[i],M_dinamica[i].transpose()))
	
	if np.array_equal(M_dinamica[i],M_dinamica[i].transpose()) == True and smaller_eig >= 0:
		cantidad_CC = cantidad_CC + 1
		data_file.write(str(r[i]) + '\n')
		data_file.write(str(map_P[i]) + '\n\n')
		data_file.write(str(map_C[i]) + '\n\n')
		data_file.write(str(M_dinamica[i]) + '\n\n\n')
	#data_file.write('hola')

data_file.write('Canales cuánticos que borran '+str(param)+' corr. = '+str(cantidad_CC))
data_file.close()
'''
		
'''
other_data = open('other_data.dat', mode = 'w')
suma = 0
for i in range(2**15):
	for j in r[i]:
		suma = suma + j
	if suma == 14:
		other_data.write(str(r[i]) + '\n')
		other_data.write(str(map_C[i]) + '\n\n')
		other_data.write(str(M_dinamica[i]) + '\n\n\n')
	suma = 0

other_data.close()
'''

# for i in `seq 1 1 2`; do echo $i > n.dat; /usr/bin/time -f "%e %M %P" -a -o 'qubit_maps_ver2.rend' python3 qubits_maps_ver2.py ; done

#15,0,14,14,13,11,12,11,12,11,7,14,13,13,12,10,11,10,11,10,6,11,10,8,11,10,8,10,12,11,11,12,8,7,6,7,6											

