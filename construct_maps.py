import numpy as np
import functions as f
from scipy import special
import sys

# Define the number n of qbits in the system
n = int(sys.argv[1])
n = 3

dimPhi = 4**n

# Define the number of correlations to be left invariant by the maps
num_of_corr = 2
num_of_corr = num_of_corr - 1

# Define the number of maps
param = int(special.binom(4**n-1, num_of_corr))



# Loop to iterate all the maps
iterable = range(4**n-1)
r = 2

pool = tuple(iterable)
if r > len(pool):
    sys.exit('Number of 1s greater is than number of Rs.')

indices = list(range(r))

oneIndices = tuple(pool[i] for i in indices)

while True:
    for i in reversed(range(r)):
        if indices[i] != i + len(pool) - r:
            break
    else:
        sys.exit('Done.')
    indices[i] += 1
    for j in range(i+1, r):
        indices[j] = indices[j-1] + 1

    oneIndices = tuple(pool[i] for i in indices)

    Rs = [1] + f.onesAndZeros(oneIndices, dimPhi-1)

    Phi_P = f.diagonalMatrix(dimPhi, Rs)







'''
1. Construct the maps in the Pauli basis
'''
maps_in_Pauli_basis = f.maps_in_Pauli_basis(n, param, num_of_corr)

# Save the maps in the Pauli basis to a .npy file so you don't need to calculate the maps again
np.save(str(n) + 'qbits-' + str(num_of_corr + 1) + 'corr_invariant' '-maps_P', maps_in_Pauli_basis)

'''
2. Make a change of basis of the maps to the computational basis
'''
# Create a 3D array to store all the param number of maps of size 4**n
maps_in_computational_basis = np.zeros((param, 4**n, 4**n))

# Calculate the change-of-basis matrix from Pauli to computational basis
change_of_basis_matrix = np.load('3qtbis_change-of-basis_matrix_P-to-C.npy')

for i in range(param):
    maps_in_computational_basis[i] = f.change_of_basis(maps_in_Pauli_basis[i], change_of_basis_matrix)

np.save(str(n) + 'qbits-' + str(num_of_corr + 1) + 'corr_invariant' '-maps_C', maps_in_computational_basis)

'''
3. Compute the reshuffling transformation to get de dynamical matrix of every map in the computational basis
'''
# Create a 3D array to store all the param number of dynamical matrices
Choi_matrices = np.zeros((param, 4**n, 4**n))

# Compute the reshuffle to every map and store it in Choi_matrices
for i in range(param):
    print(i)
    Choi_matrices[i] = f.reshuffle(maps_in_computational_basis[i], n)

np.save(str(n) + 'qbits-' + str(num_of_corr + 1) + 'corr_invariant' '-D', Choi_matrices)

print('Ya están cocinadas las matrices de Choi')


'''
4. Check the positivy of every dynamical matrix in order to conclude about the complete positivity of the map
'''
# Create a list to store the indexes of the actual quantum channels
indexes_of_quantum_channels = []

# Append every index of a quantum channel depending on the positivity of its dynamical matrix
for i in range(param):
    if f.positivity_test(Choi_matrices[i]) == True:
        indexes_of_quantum_channels.append(i)

np.save(str(n) + 'qbits-' + str(num_of_corr + 1) + 'corr_invariant' '-indexes_of_q_channels', np.array(indexes_of_quantum_channels))

'''
5. Save the results to a file. *How am I interested in the format of the file? What results to save?
'''
# To be defined


'''
Misceleanous
'''
print(len(indexes_of_quantum_channels))
