import numpy as np
from itertools import product, permutations

# sigma_x eigenbasis
upX = 1/np.sqrt(2) * np.array([1,1])
downX = 1/np.sqrt(2) * np.array([1,-1])

# sigma_y eigenbasis
upY = 1/np.sqrt(2) * np.array([1,1j])
downY = 1/np.sqrt(2) * np.array([1,-1j])

# sigma_z eigenbasis
upZ = np.array([1,0])
downZ = np.array([0,1])


sigmaEigenbasis = [[upX,downX],[upY, downY],[upZ, downZ]]

a = np.zeros((5,4,4), dtype=complex)
for i in range(3):
    k = 0
    for j in list(product([0,1], repeat=2)):
        a[i][k] = np.kron(sigmaEigenbasis[i][j[0]], sigmaEigenbasis[i][j[1]])
        k += 1

a[3] = 1/2*np.array([[1,-1,-1j,-1j],[1,-1,1j,1j],[1,1,1j,-1j],[1,1,-1j,1j]])
a[4] = 1/2*np.array([[1,-1j,-1,-1j],[1,-1j,1,1j],[1,1j,-1,1j],[1,1j,1,-1j]])

r = [1]*16

sigma0 = [[1,0],[0,1]]
sigma1 = [[0,1],[1,0]]
sigma2 = [[0,-1j],[1j,0]]
sigma3 = [[1,0],[0,-1]]

sigma = [sigma0,sigma1,sigma2,sigma3]
rho = np.zeros((4,4), dtype=complex)

k = 0
for i in range(4):
    for j in range(4):
        rho = rho + r[k]*np.kron(sigma[i], sigma[j]) / 4
        k += 1

#print(rho)

projectors = np.zeros((5,4,4,4), dtype=complex)

for i in range(5):
    for j in range(4):
        projectors[i][j] = np.outer(a[i][j], np.conjugate(a[i][j]))
        print(a[i][j])
        print(np.conjugate(a[i][j]))
        print()

print(projectors[1][0])

Phi = np.zeros((5,4,4), dtype=complex)

for i in range(5):
    for j in range(4):
        Phi[i] = Phi[i] + np.matmul(projectors[i][j], np.matmul(rho, projectors[i][j]))

print("Phi:\n")
print(Phi)

print()
print(rho)

print()
print(Phi[2])
print()
print(Phi[0] +Phi[1] )

print()

r = [1,1,1,0, 1,1,0,0, 1,0,1,0, 0,0,0,0]

rho = np.zeros((4,4), dtype=complex)

k = 0
for i in range(4):
    for j in range(4):
        rho = rho + r[k]*np.kron(sigma[i], sigma[j]) / 4
        k += 1

print("rho:")
print(rho)
