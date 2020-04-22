import random
import matplotlib.pyplot as plt
import math
import numpy as np

largo = 1000

#1° Histograma: distribución uniforme
listau = []
a = 5
b = 10
for i in range(largo):
    listau.append(a+(10-5)*random.uniform(0,1))
ex_uniforme = np.mean(listau)
print("Media Teórica Uniforme",ex_uniforme)
vx_uniforme = np.var(listau)
print("Varianza Teórica Uniforme: ",vx_uniforme)
plt.title('Distribución uniforme')
plt.ylabel('frecuencia')
plt.xlabel('valores')
plt.hist(listau, bins=32, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf()

#2° Histograma: distribución exponencial
listae = []
alfa = 3
for i in range (largo):
    listae.append(-(1/alfa)*math.log(random.uniform(0,1)))
ex_exponencial = np.mean(listae)
print("Media Teórica Exponencial", ex_exponencial)
vx_exponencial = np.var(listae) 
print("Varianza Teórica Exponencial: ",vx_exponencial)
print(vx_exponencial)
plt.title('Distribución exponencial')
plt.ylabel('frecuencia')
plt.xlabel('valores')
plt.hist(listae, bins=32, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf()    

#3° Histograma: distribución gamma
listag = []
k = 5
alfa = 3
prod = 1
for i in range (largo):
    for j in range (k):
        prod = prod * random.uniform(0,1)    
    listag.append(-math.log(prod)/3)
    prod = 1
ex_gamma = np.mean(listag)
print ("Media Teórica Gamma: ", ex_gamma)
vx_gamma = np.var(listag)
print("Varianza Teórica Gamma: ",vx_gamma)
plt.title('Distribución gamma')
plt.ylabel('frecuencia')
plt.xlabel('valores')
plt.hist(listag, bins=32, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf()        

#4° Histograma: distribución normal
listan = []
media = 87.5
probabilidad = 0.5
loop = 12
sum = 0
for i in range(largo):
    for j in range(12):
        sum = sum + random.uniform(0,1)
    listan.append(probabilidad*(sum-6)+media)
    sum = 0
ex_normal = np.mean(listan)
print ("Media Teórica Normal: ", ex_normal)
vx_normal = np.var(listan)
print("Varianza Teórica Normal: ",vx_normal)
plt.title('Distribución Normal')
plt.ylabel('frecuencia')
plt.xlabel('valores')
plt.hist(listan, bins=32, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf()    

#5° Histograma: distribución binomial
listab = []
n = 5
p = 0.5
sum = 0
for i in range (largo):
    for j in range(n):
        if (random.uniform(0,1)<0.5):
            sum += 1
    listab.append(sum)
    sum = 0        
ex_binomial = np.mean(listab)
print ("Media Teórica Binomial: ", ex_binomial)
vx_binomial = np.var(listab)
print("Varianza Teórica Binomial: ",vx_binomial)
plt.title('Distribución binomial')
plt.ylabel('frecuencia')
plt.xlabel('valores')
plt.hist(listab, bins=32, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf() 

#6° Histograma: distribución Poisson

listap = []
plambda = 10
sum = 0
exponente = math.exp(-plambda)
prod = 1
loop = 5
for i in range(largo):
    while prod > exponente:
        prod = prod * random.uniform(0,1)
        if (prod>exponente):
            sum += 1 
    listap.append(sum)
    sum = 0
    prod = 1
ex_poisson = np.mean(listap)
print ("Media Teórica Poisson: ", ex_poisson)
vx_poisson = np.var(listap)
print("Varianza Teórica Poisson: ",vx_poisson)
plt.title('Distribución de poisson')
plt.ylabel('frecuencia')
plt.xlabel('valores')
plt.hist(listap, bins=32, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf()   

#7º Histograma: Distribución Empírica Discreta
listaemp = []
probas = [0.273,0.037,0.195,0.009,0.124,0.058,0.062,0.151,0.047,0.044]
sumas = [probas[0]]
for i in range(len(probas)-1):
    sumas.append(sumas[i]+probas[i+1])
for i in range(largo):
    r = random.uniform(0,1)
    for j in range(10):
        if r <= sumas[j]:
            listaemp.append(j+1)
            break
ex_empirica = np.mean(listaemp)
print ("Media Teórica Empírica: ", ex_empirica)
vx_empirica = np.var(listaemp)
print("Varianza Teórica Empírica: ",vx_empirica)
plt.title('Distribución empírica discreta')
plt.ylabel('frecuencia')
plt.xlabel('valores')
plt.hist(listaemp, bins=32, alpha=1, edgecolor = 'black')
plt.grid(False)
plt.show()
plt.clf()   













