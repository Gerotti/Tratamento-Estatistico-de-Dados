import numpy as np

def umExperimento( N=10, sA=1, x0=50 ):
  if (N<=2):
    raise ValueError('Número de medidas menor do que 3')
  x = np.zeros(N)
  for i in range(N):
    x[i] = x0 + sA*np.random.randn()
  xf = ( np.sum(x) - np.max(x) - np.min(x) )/(N-2)
  xm = np.mean(x)
  return xf, xm

NRep = 100000
X = np.zeros(NRep)
Xm = np.zeros(NRep)
for i in range(NRep):
  X[i], Xm[i] = umExperimento()
sX = np.std( X, ddof=1 )
sXm = np.std( Xm, ddof=1 )
print( f'sX={sX:f} x smédia={sXm:f}' )
