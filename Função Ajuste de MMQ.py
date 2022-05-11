import numpy as np

def meuMMQ( Y, G, si ):
  """"
    Y é o vetor de dados
    G é uma matriz com [g1, g2, ...]
    si é um número ou o vetor de incertezas
  """
  if ( np.size(Y)!=np.shape(G)[0] ):
    print( 'ajuste não pode ser realizado: número de linhas da matriz G deve ser igual ao número de dados')
    return
  if np.size(si)==1:
    si = si*np.ones_like(Y)
  N = np.size(Y)
  P = np.shape(G)[1]
  D = np.zeros([P,1])
  M = np.zeros([P,P])
  for i in range(N):
    for linha in range(P):
      D[linha] += Y[i]*G[i,linha]/(si[i]**2)
      for coluna in range(P):
        M[linha,coluna] += G[i,linha]*G[i,coluna]/(si[i]**2)
  
  VA = np.linalg.inv(M)
  A = np.dot( VA, D )
  sA = np.sqrt( np.diag(VA) )
  sA = sA.reshape(A.shape)
  F = np.zeros([N,1])
  for i in range(N):
    for j in range(P):
      F[i] += A[j]*G[i,j]
  return A, sA, VA, F

f = 1.99 #para o ajuste dos dados reais (f = 2 deve ser usado na atividade 14)
si = 0.06
g1 = np.cos(2*np.pi*f*t)
g2 = np.sin(2*np.pi*f*t)
g3 = np.ones_like(t) #para o ajuste dos dados reais (não deve ser usado na atividade 14)
G = np.transpose([g1, g2, g3])
A, sA, VA, F = meuMMQ(Y, G, si)
plt.figure()
plt.subplot(3,1,(1,2))
plt.plot( t, Y, '*')
plt.plot( t, F, '-r')
plt.ylabel( '...' )
plt.subplot(4,1,4)
plt.plot( t, Y-F, '*')
plt.xlabel( 'tempo (s)' )
plt.ylabel( '...' )
plt.grid()
plt.show()
