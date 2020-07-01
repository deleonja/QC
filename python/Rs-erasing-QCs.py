import time
startTime = time.time()
import numpy as np
import functions as f
from scipy import special
import sys

n = int(sys.argv[1])                    # number of qubits
PhiOrder = 4**n                         # order of Phi matrix

r = int(sys.argv[2])

ChangeOfBasisMatrix = f.change_of_basis_matrix_P_to_C(n)

resultsFile = open("Rs-QCs-"+str(n)+"qbits-"+str(r)+"Inv.txt", "w")
performance = open("computingTime.txt", "w")

rIndices = range(4**n-1)
pool = tuple(rIndices)
if r > len(pool):
    sys.exit("Number of 1's is greater than number of Rs.")

indices = list(range(r))

oneIndices = tuple(pool[i] for i in indices)

Rs = [1] + f.onesAndZeros(oneIndices, PhiOrder-1)

Phi_P = f.diagonalMatrix(PhiOrder, Rs)

#print(Phi_P)
#print()

Phi_C = f.change_of_basis(Phi_P, ChangeOfBasisMatrix)

#print(Phi_C)
#print()

# Reshuffle Phi in comp. basis to obtain the Choi matrix
ChoiMatrix = f.reshuffle(Phi_C, n)

#print("Choi matrix:")
#print(ChoiMatrix)
#print()

# Check positivity of the Choi matrix
ChoiM_Positiviness = f.positivity_test(ChoiMatrix)

#print("Choi matrix positiviness : " + str(ChoiM_Positiviness))

if (ChoiM_Positiviness == True):
    for i in Rs:
        resultsFile.write(str(i)+" ")

    resultsFile.write("\n")

k = 1
print(k)

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

    Rs = [1] + f.onesAndZeros(oneIndices, PhiOrder-1)

    Phi_P = f.diagonalMatrix(PhiOrder, Rs)

    #print(Phi_P)
    #print()

    Phi_C = f.change_of_basis(Phi_P, ChangeOfBasisMatrix)

    #print(Phi_C)
    #print()

    # Reshuffle Phi in comp. basis to obtain the Choi matrix
    ChoiMatrix = f.reshuffle(Phi_C, n)

    #print("Choi matrix:")
    #print(ChoiMatrix)
    #print()

    # Check positivity of the Choi matrix
    ChoiM_Positiviness = f.positivity_test(ChoiMatrix)

    #print("Choi matrix positiviness : " + str(ChoiM_Positiviness))
    #print()

    #print("Rs = " + str(Rs))

    if (ChoiM_Positiviness == True):
        for i in Rs:
            resultsFile.write(str(i)+" ")

        resultsFile.write("\n")

    performance.write(str(time.time()-startTime)+"\n")
    print(k)
    k += 1

resultsFile.close()
