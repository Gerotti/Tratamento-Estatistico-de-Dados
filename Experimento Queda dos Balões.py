import numpy as np
import matplotlib.pyplot as plt

H = 35.0  #(m)
sH = 0.5  #(m)
a = 10. #(m/s²)
tq = np.sqrt(2*H/a)
stq = lambda N: 0.1/np.sqrt(N)

def aceleracao(H=H, tq=tq ):
  return 2*H/(tq**2)

def inc_aceleracao(stq, sH=sH, H=H, tq=tq):
  sa_H = (2/(tq**2))*(sH*np.ones(np.shape(stq)))
  sa_tq = (4*H/(tq**3))*stq
  return np.sqrt(sa_H**2 + sa_tq**2), sa_H, sa_tq

sa, sa_H, sa_tq = inc_aceleracao( stq(100.) )
print( 'sa= %.2f m/s², sa_H= %.2f m/s², sa_tq= %.2f m/s² ' % (sa, sa_H, sa_tq) )

N = np.arange(1,1001)
sa, sa_H, sa_tq = inc_aceleracao( stq(N) )
plt.plot( N, sa, '.-', label='sa')
plt.plot( N, sa_H, '-r', label='sa_H')
plt.plot( N, sa_tq, '-k', label='sa_tq')
plt.xscale('log')
plt.legend()
plt.xlabel('Número de medições de tempo')
plt.ylabel('inc. aceleração de queda (m/s²)')
