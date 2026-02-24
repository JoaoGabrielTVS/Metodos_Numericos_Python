import numpy as np
resultado = np.array([])


k = 300



for i in range (k):    
  resultado  = np.concatenate((resultado,[4*((-1)**i)*(1/(2*i+1))]))
 
print(resultado.sum())
