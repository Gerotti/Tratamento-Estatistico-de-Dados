# propagacao do efeito da incerteza de a sobre w para w(a,b)=2*(a**2)*b para a0=10.0  com  sa=0.2    e b0=5.0 com sb=0.2

import numpy as np
N = int(1e4)
a0 = 10.0
sa = 0.2
b0 = 5.0
sb = 0.2
w = np.zeros(N)
w_a = np.zeros(N)
w_b = np.zeros(N)
for i in range(N):
  a = a0 + sa * np.random.randn()
  b = b0 + sb * np.random.randn()
  w[i] = 2*(a**2)*b

  w_a[i] = 2*(a**2)*b0
  w_b[i] = 2*(a0**2)*b

sw = np.std( w, ddof=1 )
sw_a = np.std( w_a, ddof=1 )
sw_b = np.std( w_b, ddof=1 )
print( f'sw ~ {sw:.0f}' )
print( f'sw_a ~ {sw_a:.0f}' )
print( f'sw_b ~ {sw_b:.0f}' )
