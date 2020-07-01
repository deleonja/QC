import numpy as np
from bellBasis import bellBasis
from itertools import product, permutations
from functions import change_of_basis_matrix_P_to_C

# sigma_x eigenbasis
upX = 1/np.sqrt(2) * np.array([1,1])
downX = 1/np.sqrt(2) * np.array([1,-1])

# sigma_y eigenbasis
upY = 1/np.sqrt(2) * np.array([1,1j])
downY = 1/np.sqrt(2) * np.array([1,-1j])

# sigma_z eigenbasis
upZ = np.array([1,0])
downZ = np.array([0,1])

sigmaEigenbasis = [[upZ, downZ],[upX,downX],[upY, downY],[upZ, downZ]]

indices = list(product([0,1,2,3],repeat=2))
bases = np.zeros((20,4,4), dtype=complex)

w = 0
for i in indices:
    bases[w] = np.kron(sigmaEigenbasis[i[0]], sigmaEigenbasis[i[1]])
    w += 1

print(bases)

bases[16:20] = bellBasis()




for i in range(16):
    for j in range(16):
        for k in range(4):
            for l in range(4):
                innerP = np.vdot(bases[i][k], bases[j][l])
                innerP_Squared = np.absolute(innerP)**2
        if (round(innerP_Squared,3) == 0.25):
            z=1#print('i = ', i, 'j = ', j, '\n')
