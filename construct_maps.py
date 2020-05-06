import numpy as np
import functions as f

# Define the number n of qbits in the system
n = 3

# Define the number of correlations to be left invariant by the maps
num_of_corr = 4 - 1

# Define the number of maps
param = 39711

'''
1. Construct the maps in the Pauli basis
'''
maps_in_Pauli_basis = f.maps_in_Pauli_basis(n, param, num_of_corr)

'''
2. Make a change of basis of the maps to the computational basis
'''
# Create a 3D array to store all the param number of maps of size 4**n
maps_in_computational_basis = np.zeros((param, 4**n, 4**n))

# Calculate the change-of-basis matrix from Pauli to computational basis
change_of_basis_matrix = f.change_of_basis_matrix_P_to_C(n)

for i in range(param):
    maps_in_computational_basis[i] = f.change_of_basis(maps_in_Pauli_basis[i], change_of_basis_matrix)

'''
3. Compute the reshuffling transformation to get de dynamical matrix of every map in the computational basis
'''
# Create a 3D array to store all the param number of dynamical matrices
Choi_matrices = np.zeros((param, 4**n, 4**n))

# Compute the reshuffle to every map and store it in Choi_matrices
for i in range(param):
    Choi_matrices = f.reshuffle(maps_in_computational_basis, n)

'''
4. Check the positivy of every dynamical matrix in order to conclude about the complete positivity of the map 
'''
# Create a list to store the indexes of the actual quantum channels 
indexes_of_quantum_channels = []

# Append every index of a quantum channel depending on the positivity of its dynamical matrix
for i in range(param):
    if f.positivity_test(Choi_matrices[i]) == True:
        indexes_of_quantum_channels.append(i)

'''
5. Save the results to a file. *How am I interested in the format of the file? What results to save? 
'''
# To be defined