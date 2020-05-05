import numpy as np
from itertools import product

a = [0,1]
r = np.array(list(product(a, repeat=(15))))

f = open('analisis.4', mode = 'w')
R = np.ones((2**15,16))
RR = np.zeros((2**15,4,4))
for i in range(2**15):
	for j in range(15):
		R[i][j+1] = r[i][j]
	if np.dot(R[i],R[i]) == 4:
		l = 0
		for k in range(16):
			f.write(str(int(R[j][k])) + ' ')
			l += 1
			if l == 4:
				l = 0
				f.write('\n')
			if k == 15: 
				f.write('\n')
f.close()
