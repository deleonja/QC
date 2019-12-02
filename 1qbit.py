import numpy as np
from numpy import linalg as la

QC_1qubit_XcorrWiped = np.array([[1,0,0,0],[0,1/2,-1/2,0],[0,-1/2,1/2,0],[0,0,0,1]])
QC_1qubit_YcorrWiped = np.array([[1,0,0,0],[0,1/2,1/2,0],[0,1/2,1/2,0],[0,0,0,1]])
QC_1qubit_ZcorrWiped = np.array([[1/2,0,0,1/2],[0,1,0,0],[0,0,1,0],[1/2,0,0,1/2]])
QC_1qubit_XYcorrWiped = np.array([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]])   
QC_1qubit_YZcorrWiped = np.array([[1/2,0,0,1/2],[0,1/2,1/2,0],[0,1/2,1/2,0],[1/2,0,0,1/2]])  
QC_1qubit_XZcorrWiped = np.array([[1/2,0,0,1/2],[0,1/2,-1/2,0],[0,-1/2,1/2,0],[1/2,0,0,1/2]])  

q = (-1)**(1/2)
a = np.array([[1,(1-3**(1/2))/2,(1-3**(1/2))/2,1],[0,0,0,0],[0,0,0,0],[1,(-1-3**(1/2))/2,(-1-3**(1/2))/2,1]])

b = np.kron(np.array([[1,0,0,1],[0,-1,1,0],[0,1,-1,0],[1,0,0,1]]),np.identity(4))


'''
A = np.zeros((16,16))
for x in range(16):
	for y in range(16):
		if x == 0 and y == 0:
			A[[x],[y]] = 1
			if x == 3 and y == 3:
				A[[x],[y]] = 1	
			if x == 10 and y == 10:
				A[[x],[y]] = 1
			if x == 15 and y == 15:
				A[[x],[y]] = 1		
		else:
			A[[x],[y]] = 0 
			
print(A);
'''

def dynMatrix(QC, n):
	i = -1
	j = 0
	k = -1
	l = 0 
	p = 0
	DM = np.zeros((n**2,n**2))
	for x in range(n**2): ##filas
		for y in range(n**2): ##columnas
			i += 1
			#print(str(x) + "," + str(y) + " -> " + str(l) + "," + str(i))
			DM[[l],[i]] = QC[[x],[y]]
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
	print("Quantum channel:") 
	print(QC)	
	print("")
	print("Dynamical matrix:")
	print(DM)
	print("")
	print("Adjoint of the dynamical matrix:")
	print(DM.transpose())
	return DM

def checkHermiticity(DM, n):
	t = False
	for x in range(n**2):
		for y in range(n**2):
			#print(str(x) + ", " + str(y))
			if DM[[x],[y]] != DM.transpose()[[x],[y]]:
				print("Dynamical matrix not hermitian")
				t = True
				break
			else:  
				continue
		if t == True:
			break
	print("")
	return

def eigenvalues(DM):
	print("Eigenvalues:")
	print(la.eig(DM)[0])
	print("")
	print("")


print('2 QUBITs: Y1Z1X2Z2 ERASED')
#A = QC_1qubit_XYcorrWiped
#A = np.kron(QC_1qubit_XYcorrWiped, np.identity(4))
#A = np.kron(np.identity(4), QC_1qubit_XYcorrWiped)
#dynMatrix(a, 2)
#dynMatrix( np.kron( np.kron(QC_1qubit_XYcorrWiped, np.identity(4)), np.identity(4)), 8)
eigenvalues( dynMatrix( np.kron( np.kron( QC_1qubit_YZcorrWiped, QC_1qubit_YZcorrWiped), np.identity(4) ) , 8) )
checkHermiticity( dynMatrix( np.kron( np.kron(QC_1qubit_YZcorrWiped, QC_1qubit_XZcorrWiped), np.identity(4)), 8), 8)
