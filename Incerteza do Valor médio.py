# Incerteza do valor médio de experimentos sujeitos a erros aleatórios de desvio-padrão sA e erro sistemático residual de desvio-padrão sS

import numpy as np

def cadaExperimento(N=25, x0=50.0, sA=2.0, sS=0.5):
  x = np.zeros(N)
  erroSist = sS * np.random.randn()
  for i in range(N):
    erroAleat_i = sA * np.random.randn()
    x[i] = x0 + erroSist + erroAleat_i
  xm = np.mean(x)
  return xm

NRep = 1000
xm = np.zeros(NRep)
for i in range(NRep):
  xm[i] = cadaExperimento()

sxf = np.std( xm, ddof=1 )
print( 'sxf ~', sxf )
import matplotlib.pyplot as plt
plt.plot( 1+np.arange(NRep), xm, '.' )
plt.ylabel('Valor médio em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Médias obtidas nas {NRep:.0f} simulações')
