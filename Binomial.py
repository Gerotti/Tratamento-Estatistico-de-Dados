import numpy as np
nU = 4300228
np.random.seed(nU)
N = 10000
n = 0
for i in range(N):
  x = np.random.rand()
  y = np.random.rand()
  if ( (x**2 + y**2)<=1 ):
    n = n+1
sn = np.sqrt(n*(1-n/N))
x = 4*(n/N)
sx = (4/N)*sn
print( f'1) n={n:.0f}, sn = {sn:.0f}')
print( f'2) x={x:.3f}, sx = {sx:.3f}')

p = np.pi/4
sn0 = np.sqrt(N*p*(1-p))
sx0 = (4/N)*sn0
print( f'3.1) sn0 = raiz(N*p*(1-p)) = {sn0:.0f}')
print( f'3.2) sx0 = (4/N)*sn0 = {sx0:.3f}')
