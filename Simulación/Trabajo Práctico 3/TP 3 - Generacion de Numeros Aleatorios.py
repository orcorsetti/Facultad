import random
import xlwt
from xlwt import Workbook
from sympy import primerange



def DCM(a,b):
    t = 0
    while(b != 0):
        t = a
        a = b
        b = t%b
    return a    
def primosEntreSi(a,b):
    return DCM(a,b) == 1


    
def comrpuebaTeorema(m,c,a):
    band = False
    if (m%4 == 0 and (a-1)%4 == 0):
        lista_primos = list(primerange(0,100))
        for i in range(len(lista_primos)):
            if (m%lista_primos[i] == 0 or (a-1)%lista_primos[i] == 0):
                band = True
                break    
        if(band):
            if(primosEntreSi(m,c)):
                return True
            else:
                return False    
        else:
            return False
    else:
        return False




wb = Workbook()
sh1 = wb.add_sheet('Metodo de los cuadrados')
sh1.write(0,1,"i")
sh1.write(0,2,"Zi")
sh1.write(0,3,"Ui")
sh1.write(0,4,"Zi2")

#Metodo cuadrado de los medios

lista_aleatorios = []
zcero = 1009
largo = 15

for i in range(largo):
    zcuadrado = pow(zcero,2)
    aux = list(str(zcuadrado))
    if (len(aux)<8):
        comp = 8-len(aux)
        for i2 in range (comp):
            aux = ["0"] + aux
    lista_si = aux[2:6]
    if i == 0:
        sh1.write(i+1,1,i)
        sh1.write(i+1,2,zcero)
        sh1.write(i+1,4,zcuadrado)
    else:
        sh1.write(i+1,1,i)
        sh1.write(i+1,2,zcero)
        sh1.write(i+1,3,ale)
        sh1.write(i+1,4,zcuadrado)
    zcero =int(''.join(lista_si))
    ale = zcero/1000 

wb.save("prueba-generacion.xls")  

#Generador congruencial lineal mixto


def GCL(m,c,a,z0):
    cant_ale = 20
    lista_aleatorios2 = []
    for i in range(cant_ale):
        z = (a*z0+c)%m
        u = z/m
        lista_aleatorios2.append(u)
        z0 = z
    #print(lista_aleatorios2)
    if(comrpuebaTeorema(m,c,a)):
        print("El teorema se comprueba")
    else:
        print("El teorema no se comprueba")
GCL(16,3,5,7)
GCL(16,3,4,7)
GCL(16,4,5,7)
GCL(16,4,4,7)


