# Experimento sujeito a erros aleatórios de desvio-padrão sA e erro  mais um erro sistemático residual de desvio-padrão sS

import numpy as np
import matplotlib.pyplot as plt

N = 25
x0 = 50
sA = 2.0
sS = 0.5
x = np.zeros(N)
erroSist = sS * np.random.randn()
for i in range(N):
  erroAleat_i = sA * np.random.randn()
  x[i] = x0 + erroSist + erroAleat_i

plt.plot( 1+np.arange(N), x, '*')
plt.ylabel('Valor obtido, x')
plt.xlabel('Número da medida')
plt.title(f'Valores obtidos nas {N:.0f} medições')
