import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

NGL = 2
IC = 0.90
tC_INF = stats.t.ppf( (1-IC)/2, df=NGL )
tC_SUP = stats.t.isf( (1-IC)/2, df=NGL )
print( tC_INF, tC_SUP )

ts = np.linspace( -10, 10, 100)
PDF = stats.t.pdf(ts,df=NGL)
ts90 = np.linspace( tC_INF, tC_SUP, 100)
PDF90 = stats.t.pdf(ts90,df=NGL)

plt.figure()
plt.plot( ts, PDF, '-r')
plt.plot( ts90, PDF90, '.-k')
plt.xlabel( 't' )
plt.ylabel( 'pdf(t) com %d graus de liberdade' % NGL)
plt.show()
