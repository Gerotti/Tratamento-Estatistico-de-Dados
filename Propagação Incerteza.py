#propagacao de x (x0=10.0 e sx=0.2) para w(x)=5x**2

import numpy as np
N = int( 1e4 )
x0 = 10.0
sx = 0.2
x = x0 + sx*np.random.randn(N)
w = 5*(x**2)
sw = np.std( w, ddof=1 )

print( 'sw ~', sw)
