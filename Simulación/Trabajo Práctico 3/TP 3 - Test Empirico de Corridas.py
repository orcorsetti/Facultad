from random import random
from scipy.stats import chi2


a=[[4529.4, 9044.9, 13568, 18091, 22615, 27892],
   [9044.9, 18097, 27139, 36187, 45234, 55789],
   [13568, 27139, 40721, 54281, 67852, 83685],
   [18091, 36187, 54281, 72414, 90470, 111580],
   [22615, 45234, 67852, 90470, 113262, 139476],
   [27892, 55789, 83685, 111580, 139476, 172860]]

b = [1/6, 5/24, 11/120, 19/720, 29/5040, 1/840]
r = []
n = 4000
for i in range (6):
    r.append(0)
ale1 = random()
sum = 1
for i in range (n-1):
    ale = random()
    if ale > ale1:
        sum +=1
    else:
        if sum >= 6:
            r[5]+=1
        else:
            r[sum - 1]+=1
        sum = 1
    ale1 = ale

R = 0
for i in range (6):
    for j in range (6):
        R = R + (a[i][j]*(r[i] - (n * b[i])) * (r[j] - (n * b[j])))
R = R * 1/n
print(R)
chi = chi2.ppf(0.90,6)
print(chi)
if chi >= R:
    print("No se rechaza la H0. Son independientes.")
else:
    print("Se rechaza la H0. No son independientes.")
