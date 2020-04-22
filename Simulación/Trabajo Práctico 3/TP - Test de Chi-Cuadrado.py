from random import random
from math import trunc
from scipy import stats
import matplotlib.pyplot as plt
import requests

def calculaPos(lista_aleatorios,n,k):
    lista = []
    for i in range (k):
        lista.append(0)
    segmento = 1/k
    for i in range(n):
        pos = trunc(lista_aleatorios[i] / segmento)
        if lista_aleatorios[i] == 1:
            pos = pos - 1
        lista[pos] = lista[pos] + 1
    plt.hist(lista_aleatorios, bins=40, alpha=1, edgecolor = 'black',  linewidth=1)
    plt.grid(True)
    plt.show()
    plt.clf()
    return lista

def chicuadrado(lista_frecuencias,n,k):
    sum = 0
    for i in range (k):
        sum = sum + (lista_frecuencias[i]-(n/k))**2
    x_chi = (k/n)*sum
    print(x_chi)
    print(stats.chi2.ppf(0.95,k-1))
    if x_chi > stats.chi2.ppf(0.95,k-1):
        print("No son uniformes")
    else:
        print("Es Uniforme")
    


lista_aleatorios = []
n = 10000
k = 100
for i in range(n):
    lista_aleatorios.append(random())
lista = calculaPos(lista_aleatorios,n,k)
chicuadrado(lista,n,k)



m = 2**35
a = 5**15
c = 3
z0 = 7



cant_ale = 10000
lista_aleatorios2 = []
for i in range(cant_ale):
    z = (a*z0+c)%m
    u = z/m
    lista_aleatorios2.append(u)
    z0 = z
lista = calculaPos(lista_aleatorios2,n,k)
chicuadrado(lista,n,k)


url = 'https://www.random.org/decimal-fractions/?num=10000&dec=10&col=1&format=plain&rnd=new'
response = requests.get(url).text
#print(response)

lista_aleatorios3 = []
for i in response.split("\n"):
    try:
        lista_aleatorios3.append(float(i))
    except:
        pass
print(len(lista_aleatorios3))
lista = calculaPos(lista_aleatorios3,n,k)
chicuadrado(lista,n,k)





