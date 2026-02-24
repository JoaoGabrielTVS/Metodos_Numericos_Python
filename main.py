import numpy as np
resultado = np.array([1])


k = 3



for i in range (k):    
  resultado  = np.concatenate([[4*((-1)**i)*(1/(2*i+1))],resultado])
  print(resultado)
