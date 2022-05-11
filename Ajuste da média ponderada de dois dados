import numpy as np
x = np.array([10, 20])
sx = np.array([5, 2])
def funcao_lnL( x0, X=x, SX=sx ):
  lnL = 0
  for xis, sigma in zip(X,SX):
    lnL += -(1/2)*np.log(2*np.pi) - np.log(sigma) -1/2*( (xis-x0)/sigma )**2
  return lnL

As = np.linspace(10,20,81)
LnLs = funcao_lnL(As, X=np.array([10,20,15,18]), SX=np.array([5,2,3,8]))
import matplotlib.pyplot as plt
plt.plot( As, LnLs, '-')

from scipy import optimize
res = optimize.minimize_scalar( lambda a: -funcao_lnL(a, X=np.array([10,20,15,18]), SX=np.array([5,2,3,8])), bounds=(10, 20) )
res.x
print( As )
