import numpy as np

def gera_x_exclusao(N=1, xmin=0, xmax=1, ymax=2, f = lambda x: 2*x):
  i = 0
  X = np.zeros(N)
  while (i<N):
    #gerar xcandidato
    xc = xmin + (xmax-xmin)*np.random.rand()
    #gerar y para verificacao
    yv = ymax * np.random.rand()
    if (yv <= f(xc) ):
      X[i] = xc
      i = i+1
  return X

x = gera_x_exclusao(N=10000000)
import matplotlib.pyplot as plt
plt.hist(x,20)
