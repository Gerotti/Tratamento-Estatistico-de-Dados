import numpy as np
N = 10000
xI = 0
xF = np.pi
yMax = 1
n = 0
for i in range(N):
  x = xI + (xF-xI)*np.random.rand()
  y = yMax * np.random.rand()
  if (y<=np.sin(x)):
    n = n + 1

Area = (n/N)*(xF-xI)*yMax
print( 'Area ~ ', Area)
