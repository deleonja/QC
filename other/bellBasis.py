import numpy as np

def bellBasis():
    # Returns a np array with the Bell basis
    basis = 1/np.sqrt(2)*np.array([[1,0,0,1],[1,0,0,-1],[0,1,1,0],[0,1,-1,0]])
    return basis

def evaluateMUBs(possibleMUBs, numOfBases, dim):
    for i in range(numOfBases):
        for j in range(numOfBases):
            if i == j:
                continue
            for k in range(dim):
                for l in range(dim):
                    innerP_Squared = np.vdot(possibleMUBs[i][k], possibleMUBs[j][l])
                    innerP_Squared = np.absolute(innerP_Squared)**2
                    print("i = ", i, "j = ", j)
                    print(innerP_Squared)
    return
