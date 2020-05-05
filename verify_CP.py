import numpy as np
from numpy import linalg as la
from itertools import product

def chop(expr, *, max=1e-10):
	return [i if abs(i) > max else 0 for i in expr]

def CP(M_dinamica):
	smallest_eig = chop(np.linalg.eigh(M_dinamica)[0])[0]
	CP = np.array_equal(M_dinamica,M_dinamica.transpose()) and smallest_eig >= 0
	return CP
		
	
	

	
