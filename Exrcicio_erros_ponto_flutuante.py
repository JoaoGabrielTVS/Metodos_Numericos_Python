####################################################exercicio 1.1######################################################
n = 25
numero_resposta = 5
xi = 1
for i in range(1,11):
  xi = (xi + n/xi)/2
  print((np.abs(numero_resposta - xi)/np.abs(numero_resposta))*100)

###################################################################1.2######################################
e = 1
while(1):
  if(e + 1) <= 1:
      e = e*2
  else:
      e = e/2






#################################################################################1.3##############################################
x = 1/3

for i in range(50):
  x = 4*x -1
  print(x)

#a convergencia ocorre ate um certo numero , apos um determinado valor  volta a desconvergir

##########################################################################1.4################################################
pi = [0.1,0.01,0.001, 0.0001,0.000000001]
for i in pi:
  print('-----------------------------------------')
 # print((2.718281828459045**(1/i))/(1+(2.718281828459045**(1/i))))

  print(1/((2.718281828459045**(-1/i))+1))
  print('------------------------------------------')
#a segunda opçao para valores muito pequenos nao gera overflow , enquanto a primeira gera , ja no valor 0.001

#############################################################################1.5##################################################################################################################
x = np.longdouble([10**(-12),10**(-15),10**(-17)])
for i in x:
  fx = (((1+i)-1)/i)
  print(fx)

#o resultado ele gera um valor muito proximo de 1 mas nao extamene igual a 1, diferente de quando fazemos de forma analitica que da exatamente igual a 1
import numpy as np
import matplotlib.pyplot as plt


##########################################################################################1.6########################################
resultado = np.array([])
resultado1 = np.array([])
resultado2 = np.array([])
resultado3 = np.array([])
tick = 1
res1 = np.array([])
res2 = np.array([])
res3 = np.array([])
res4 = np.array([])
def gerar_grafico():
  global resultado1
  global resultado

def formula_base(n,l):
  k = 20
  global tick
  global res1
  global res2
  global res3
  global res4
  global resultado3
  global resultado1
  global resultado
  for i in range (k):
      resultado  = np.concatenate((resultado,[(((-1)**i)*((n**(2*i+1))/(2*i+1)))]))
      resultado1 = np.concatenate((resultado1,[(((-1)**i)*((l**(2*i+1))/(2*i+1)))]))
      if tick == 4:
        resultado3  = np.concatenate((resultado3,[(((-1)**i)*(((1/8)**(2*i+1))/(2*i+1)))]))

      if tick == 1:
          q1 = 4*(4*resultado - resultado1)
          res1 = np.concatenate((res1,[q1.sum()]))
      if tick == 2:
          q2 = 4*(resultado + resultado1)
          res2 = np.concatenate((res2,[q2.sum()]))
      if tick == 3:
          q3 = 4*(2*resultado + resultado1)
          res3 = np.concatenate((res3,[q3.sum()]))
      if tick == 4:
          q4 = 4*(resultado + resultado1 + resultado3)
          res4 = np.concatenate((res4,[q4.sum()]))
  resultado3 = np.array([])
  resultado = np.array([])
  resultado1 = np.array([])

  tick += 1

formula_base(1/5,1/239)
formula_base(1/2,1/3)
formula_base(1/3,1/7)
formula_base(1/2,1/5)
print(res1)
print(res2)
print(res3)
print(res4)


k1 = len(res1)
k2 = len(res2)
k3 = len(res3)
k4 = len(res4)
k = max(k1, k2, k3, k4)
x = np.arange(1, k+1)

err1 = np.abs(np.pi - res1)
err2 = np.abs(np.pi - res2)
err3 = np.abs(np.pi - res3)
err4 = np.abs(np.pi - res4)

fig, ax = plt.subplots(figsize=(9,6))
ax.plot(np.arange(1, len(err1)+1), err1, marker='o')
ax.plot(np.arange(1, len(err2)+1), err2, marker='s')
ax.plot(np.arange(1, len(err3)+1), err3, marker='^')
ax.plot(np.arange(1, len(err4)+1), err4, marker='d')

ax.set_yscale('log')
ax.set_xlabel('Número de termos (n)')
ax.set_ylabel('Erro absoluto |π - aproximação|')
ax.grid(True, which='both', linestyle='--', alpha=0.5)
ax.legend()
plt.tight_layout()
plt.show()
