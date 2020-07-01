import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

def l_func(x, a, b):
    return a*x + b

time = np.loadtxt("computingTime.txt")
matrices = np.arange(2,time.shape[0]+2)

computingTime = np.polyfit(matrices, time, 1)
#print(computingTime)

plt.plot(matrices, time, '.--k')
plt.plot(matrices, l_func(matrices, *computingTime), '--r')
plt.ylabel(r"Tiempo de cómputo t [s]")
plt.xlabel(r"Número de matrices de 64$\times$64 analizadas N")
plt.legend(['Datos',r't(N)=%3.3f N + %3.3f' % tuple(computingTime)], frameon=False)
plt.grid("--k", lw=0.05)

plt.savefig("computingTime.pdf")

#plt.show()
