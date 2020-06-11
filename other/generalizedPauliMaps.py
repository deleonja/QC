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

a = np.zeros((3,4,4), dtype=complex)
for i in range(3):
    k = 0
    for j in list(product([0,1], repeat=2)):
        a[i][k] = np.kron(sigmaEigenbasis[i][j[0]], sigmaEigenbasis[i][j[1]])
        k += 1

print(a)

notMUB = False
for i in range(3):
    for j in range(3):
        if i == j:
            break
        for k in range(4):
            for l in range(4):
                innerP_Squared = np.vdot(a[i][k], a[j][l])
                innerP_Squared = np.absolute(innerP_Squared)**2
                #print(innerP_Squared)
