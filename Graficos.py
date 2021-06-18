#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import ticker


def arg(num):
        if num%2==0:
            if int(math.sqrt(num))*int(math.sqrt(num))==num:
                return int(math.sqrt(num)), int(math.sqrt(num))
            else:
                return int(math.sqrt(num)) + 1, int(math.sqrt(num))
        else:
            if int(math.sqrt(num+1))*int(math.sqrt(num+1))==num:
                return int(math.sqrt(num)), int(math.sqrt(num))
            else:
                return int(math.sqrt(num+1)) + 1, int(math.sqrt(num+1))


arch = open("C:\\Users\\Fabian Perez\\source\\repos\\Cutting\\x64\\Release\\input2.txt")

cantCortes = int(arch.readline())
linea = arch.readline()

fig1 = plt.figure("Placas")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)

for i in range(1, cantCortes+1):
    if cantCortes != 1:
        aux = arg(cantCortes)
        ax = fig1.add_subplot(int(aux[0]), int(aux[1]), i)
    else:
        ax = fig1.add_subplot(1, 1, i)

    aux = linea.split()
    linea = arch.readline()
    aux2 = linea.split()
    h = int(aux2[0])
    w = int(aux2[1])
    o = int(aux[0])
    j = int(aux[1])
    q = int(aux[2])
    n = int(aux[3])
    if o == 0:
        ancho = np.array(range(w + 1))
        largo = np.zeros(len(ancho))
        for j in range(len(ancho)):
            largo[j] = q
        ax.plot(ancho, largo, "r--")
        ax.set_xlabel('Ancho de la placa')
        ax.set_ylabel('Alto de la placa')
        ax.set_xlim(0, w)
        ax.set_ylim(0, h)
        ax.set_title('Se corta un total de ' + str(n) + ' veces')
    elif o == 1:
        largo = np.array(range(h + 1))
        ancho = np.zeros(len(largo))
        for k in range(len(largo)):
            ancho[k] = q
        ax.plot(ancho, largo, "r--")
        ax.set_xlabel('Ancho de la placa')
        ax.set_ylabel('Alto de la placa')
        ax.set_xlim(0, w)
        ax.set_ylim(0, h)
        ax.set_title('Se corta un total de ' + str(n) + ' veces')
    linea = arch.readline()
plt.show()


# In[ ]:




