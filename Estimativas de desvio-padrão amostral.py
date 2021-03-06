# Sobre as estimativas de desvio-padrão amostral de experimentos sujeitos a erros aleatórios e a erros sistemáticos residuais

import numpy as np

def cadaExperimento2(N=25, x0=50.0, sA=2.0, sS=0.5):
  x = np.zeros(N)
  erroSist = sS * np.random.randn()
  for i in range(N):
    erroAleat_i = sA * np.random.randn()
    x[i] = x0 + erroSist + erroAleat_i
  xm = np.mean(x)
  sx = np.std(x, ddof=1)
  return (xm,sx)

NRep = 1000
xm = np.zeros(NRep)
sx = np.zeros(NRep)
for i in range(NRep):
  xm[i], sx[i] = cadaExperimento2()

import matplotlib.pyplot as plt
plt.plot( 1+np.arange(NRep), sx, '.r' )
plt.ylabel('Desvio-padrão amostral em cada simulação')
plt.xlabel('Número da simulação')
plt.title(f'Desvios-padrões amostrais nas {NRep:.0f} simulações')
