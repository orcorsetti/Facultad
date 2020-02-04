#maximo de la funcion 1073741823
from random import randint
from random import random
import xlwt #Libreria excel
wb=xlwt.Workbook() #Creamos archivo de excel
ws=wb.add_sheet('AG') #Agregamos hoja
pm=0.25     #0.05
pc=0.75     #0.75
n=int(input('Ingrese numero de corridas: '))

cr=[['' for j in range(10)]for i in range(n+1)]

for j in range(30):         #Crea poblacion inicial 
    for i in range(10):    
        cr[0][i]+=str(randint(0,1))

tab=[[0 for j in range(3)]for i in range(n+1)]  #Creacion tabla función objetivo

for c in range(n):
    print(cr[c])    #Muestra poblacion
    dec=[]
    sum=0
    for i in range(10):
        num= int(str(cr[c][i]),2)   
        sum+=num
        dec.append(num) #Llena tabla decimal, con la poblacion convertida en integer
    
    fit=[[0 for j in range(4)]for i in range(10)] #Creacion tabla Fitness
    sum=0
    for i in range(10): #"Llenado tabla fitness"
        fit[i][0]=str(bin(dec[i])[2:].zfill(30))    #Binario de 30 digitos
        fit[i][1]=dec[i]    #Decimal
        fit[i][2]=(fit[i][1]/((2**30)-1))**2    #"x" evaluadio en la funcion
        sum+=fit[i][2]
    
    for i in range(10): #"Calculo Probabilidades" 
        if round(fit[i][2]*100/sum)==0:
            fit[i][3]=1
        else:
            fit[i][3]=round(fit[i][2]*100/sum) 
    print(fit) #Muestrra tabla fittnes
    
    tab[c][0]=((max(dec))/((2**30)-1))**2 #Llena tabla Funcion Objetivo
    tab[c][1]=((min(dec))/((2**30)-1))**2
    tab[c][2]=sum/10
    ws.write(c,0,str(bin(max(dec))[2:].zfill(30)))  #Llenamos filas y columnas de la hoja excel
    ws.write(c,1,tab[c][0]) 
    ws.write(c,2,tab[c][1]) 
    ws.write(c,3,tab[c][2]) 
    
    print(tab[c])   #Muestra tabla Funcion Objetivo
    
    #Ruleta
    ru=[] 
    for i in range(10): #"Carga Ruleta"
        for j in range (fit[i][3]):
            ru.append(fit[i][1])
    
    #Crossover
    for i in range (5): #Se evalua en pares 
        cr1=randint(0, len(ru)-1) #Selecciona Candidatos
        cr2=randint(0, len(ru)-1) 
        cr1h=str(bin(ru[cr1])[2:].zfill(30))    #Transforma a binario con 30 digitos
        cr2h=str(bin(ru[cr2])[2:].zfill(30))
        cr1h=list(map(int,str(cr1h))) #Separa los elementos de la lista como un elemento c/u
        cr2h=list(map(int,str(cr2h)))
        pc1= random() #Probabilidad crossover
        if pc1<=pc:   
            gen= randint (0,29) #Gen al azar entre 0 y 28
            aux1=cr1h[gen:30]
            aux2=cr2h[gen:30]
            cr1hijo=cr1h[0:gen]+aux2 #Reemplazo de elementos de la poblacion
            cr2hijo=cr2h[0:gen]+aux1
            cr1h=cr1hijo
            cr2h=cr2hijo
            cr1hijo=("".join(map(str,cr1hijo)))
            cr2hijo=("".join(map(str,cr2hijo)))  
            cr[c+1][(i*2)]=cr1hijo  #Le asigna a la prox generacion los hijos
            cr[c+1][(i*2)+1]=cr2hijo 
        else:
            cr[c+1][(i*2)]=("".join(map(str,cr1h)))   #Si no entra en crossover, se le asignan los padres
            cr[c+1][(i*2)+1]=("".join(map(str,cr2h))) 
        
        #Mutacion
        pm1=random()    #Probabilidad mutación
        if pm1<=pm:
            gen= randint(0,29) #Gen al azar entre 0 y 29
            cr1hijo=cr1h
            cr2hijo=cr2h
            if(cr1hijo[gen]==0):
                cr1hijo[gen]=1   #Intercambio   
            else:
                cr1hijo[gen]=0    
            cr1hijo=("".join(map(str,cr1hijo)))     #Junta todos los elementos en un binario de 30
            cr[c+1][(i*2)]=cr1hijo    #Asigna a prox generacion
            
            if(cr2hijo[gen]==0):
                cr2hijo[gen]=1  #Intercambio 
            else:
                cr2hijo[gen]=0
            cr2hijo=("".join(map(str,cr2hijo)))     #Junta todos los elementos en un binario de 30
            cr[c+1][(i*2)+1]=cr2hijo    #Asigna a prox generacion


    

wb.save(r'C:\Users\Public\Documents\AG.xls')    #Se guarda tabla Funcion Objetivo en excel.

