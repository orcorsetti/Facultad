import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 



#Grafica 1 - Frecuencia Relativa
lista = []
frecs = []
largo = 2700
e = 7
for i in range(largo):
    lista.append(random.randint(0,36))
    frecs.append(lista.count(e)/len(lista))
plt.plot(frecs)
plt.hlines(1/37,0,largo)
plt.ylabel('Frecuencia Relativa (Numero 7)')
plt.xlabel('n')
plt.show()

#Grafica 2 - Media
esp = []
for i in range(len(lista)):
    esp.append(sum(lista[:(i+1)]) / (i+1))
plt.plot(esp)
plt.hlines(18,0,largo)
plt.ylabel('Media Aritmética')
plt.xlabel('n')
plt.show()

#Grafica 3 - Bla
med = []
for i in range(len(esp)):
    med.append(sum(esp[:(i+1)])/(i+1))
plt.plot(med)
plt.hlines(18,0,largo)
plt.plot(esp)
plt.ylabel('E(E)')
plt.xlabel('n')
plt.show()

#Grafica 4 - Variancia
var = []
medmed = (sum(esp)/len(esp))
suma = 0
for i in range(len(esp)):
    var.append(((esp[i]-medmed)**2)*(1/37))
plt.plot(var)
plt.ylabel('V(E)')
plt.xlabel('n')
plt.show()

#Grafica 5 - Barras
elems=[]
ele = []
for i in range(37):
    elems.append(lista.count(i))
    ele.append(i)
ele.append(37)
print(elems)
plt.title('Histograma')
plt.ylabel('Cantidad de ocurrencias')
plt.xlabel('X')
plt.hist(lista, bins=ele, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf()
