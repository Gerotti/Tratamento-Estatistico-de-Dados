import numpy as np
N = 10000
L = 1
erro = np.zeros(N)
for i in range(N):
  erro[i] = L*( np.random.rand() - 0.5)

inc_arred = np.std( erro, ddof=1 )
print( 'inc_arred = ', inc_arred )
tendenciosidade = np.mean( erro )
print( 'tend = ', tendenciosidade )
inc_tendenciosidade = inc_arred/np.sqrt(N)
print( 'inc_tend = ', inc_tendenciosidade )
print( 'L/raiz(12) =', L/np.sqrt(12))
