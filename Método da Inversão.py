import numpy as np

def gera_x_inversao( N=1, inv_g = lambda g:np.sqrt(g) ):
  X = np.zeros(N)
  for i in range(N):
    g = np.random.rand()
    X[i] = inv_g(g)
  
  return X

x = gera_x_inversao(N=10000000)
import matplotlib.pyplot as plt
plt.hist(x,20)
