import numpy as np
import random
a = np.zeros ((50,50,50))
soma = oco = maior = 0
for i in range (0,50):
    for j in range (0,50):
        for k in range (0,50):
            a[i,j,k] = random.randint(0,100)
for i in range (0,50):
    for j in range (0,50):
        for k in range (0,50):
          soma +=soma+a[i,j,k]
          print (soma)
for i in range (0,50):
    for j in range (0,50):
        for k in range (0,50):
          if a[i, j, k] > maior:
          	maior = a[i, j, k]
      
for i in range (0,50):
    for j in range (0,50):
        for k in range (0,50):
        		if a[a, j, k] == 90:
        		  cont += 1