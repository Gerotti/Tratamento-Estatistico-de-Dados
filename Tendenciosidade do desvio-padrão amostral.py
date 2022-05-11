import numpy as np
import matplotlib.pyplot as plt

x0 = 0
s0 = 1
nREP = 10_000
Ns = [2, 3, 4, 5, 10, 50, 100]
for N in Ns:
  print( 'N = %d:' % N )
  x = x0 + s0*np.random.randn(nREP,N)
  sx = np.std( x, axis=1, ddof=1 )
  sxm = np.mean(sx)
  s_sx = np.std( sx, ddof=1)
  s_sxm = s_sx/np.sqrt(len(sx))
  print( 'sxm = %.4f' % sxm )
  print( 'inc_sxm = %.4f ' % s_sxm )

  vx = sx**2
  vxm = np.mean(vx)
  s_vx = np.std(vx,ddof=1)
  s_vxm = s_vx/np.sqrt(len(vx))
  print( 'vxm = %.3f' % vxm )
  print( 'inc_vxm = %.3f ' % s_vxm )

  n_sx = sum(sx<=s0)
  sn_sx = np.sqrt( n_sx*(1-n_sx/nREP) )
  print( 'n(sx<=sx0) = %d # %.0f' % (n_sx, sn_sx) )
  print( 'n(vx<=vx0) = %d' %sum(vx<=(s0**2)) )
  plt.figure()
  plt.hist( sx, 100);
  plt.xlabel( 'desvio-padrão amostral' );
  plt.ylabel( 'ocorrências');
  plt.title( 'Histograma desvio-padrão amostral para N = %d' %N );
  plt.show()
  plt.figure()
  plt.hist( vx, 100);
  plt.xlabel( 'variancia amostral' );
  plt.ylabel( 'ocorrências');
  plt.title( 'Histograma da variância amostral para N = %d' %N );
  plt.show()
