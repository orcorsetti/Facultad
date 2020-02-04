opc=10    
while (opc!=5):
    opc=10
    while opc<1 or opc>5:       #Valida Opcion
        opc=int(input('1)Parte 1   2)Parte 2   3)Parte 3 exhaustiva   4)Parte 3 greedy   5)Salir   :   ' ))
    if(opc==1):    
        lista=[[150],[325],[600],[805],[430],[1200],[770],[60],[930],[353]]
        listavol=[150,325,600,805,430,1200,770,60,930,353]
        listapre=[[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]
        combinaciones=[]
 
        for i in range(len(lista)): #Crea Lista de combinaciones
            combinaciones.append([]) 

        for a in range(len(lista)): 
            combinaciones[0].append(lista[a])
            for b in range(a+1,len(lista)):
                combinaciones[1].append(lista[a] + lista[b])
                for c in range(b+1,len(lista)):
                    combinaciones[2].append(lista[a] + lista[b] + lista[c])
                    for d in range(c+1,len(lista)):
                        combinaciones[3].append(lista[a] + lista[b]+ lista[c]+ lista[d])
                        for e in range(d+1,len(lista)):
                            combinaciones[4].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e])
                            for f in range (e+1,len(lista)):
                                combinaciones[5].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f])
                                for g in range (f+1,len(lista)):
                                    combinaciones[6].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g])
                                    for h in range (g+1,len(lista)):
                                        combinaciones[7].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g]+lista[h])
                                        for i in range (h+1,len(lista)):
                                            combinaciones[8].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g]+lista[h]+lista[i])
                                            for j in range (i+1,len(lista)):
                                                combinaciones[9].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g]+lista[h]+lista[i]+lista[j])
        
        combinacionesvol=[]
        for i in range (len(combinaciones)): #Filtra volumenes menores o iguales a 4200
            for j in range (len(combinaciones[i])):
                sum=0
                for k in range (len(combinaciones[i][j])):
                    sum= sum + combinaciones[i][j][k]
                if (sum<=4200):
                    combinacionesvol.append(combinaciones[i][j])
        
        mx=0
        sumVol=0
        listaindice=[]
        for i in range (len(combinacionesvol)): #busca y suma el beneficio de cada combinacion, y guarda la de mayor beneficio
            sum=0
            sumV=0
            for j in range (len(combinacionesvol[i])):
                ind=listavol.index(combinacionesvol[i][j])
                sum= sum+ listapre[ind][1]
                sumV= sumV + listapre[ind][0]
            if (sum>mx):
                indmax=i
                mx=sum
                sumVol= sumV
        for i in range (len(combinacionesvol[indmax])):
            ind=listavol.index(combinacionesvol[indmax][i])
            listaindice.append(ind+1)

        print(combinacionesvol[indmax]) #Combinacion de mayor beneficio
        print(listaindice) #Indices de los elementos
        print(mx) #Valor del beneficio
        print(sumVol) #Volúmen total



    if(opc==2): 
        listapre=[[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]
        listaGreedy=[]
        listaOrdenada=[]

        for i in range(10): #Crea lista geedy
            listaGreedy.append(float(listapre[i][1]/listapre[i][0]))
        listaOrdenada=sorted(listaGreedy,reverse=True)

        mochila=[]
        sumVol=0
        sumPrecio=0
        for i in range(10): #Recorre lista, suma volumen y precio si no excede el limite de la mochila
            for j in range(10):
                if (listaOrdenada[i]==float(listapre[j][1]/listapre[j][0])):
                    ind=j
            sumVol= sumVol + listapre[ind][0]
            if sumVol<=4200:
                mochila.append(listapre[ind])
                sumPrecio= sumPrecio + listapre[ind][1]
            else:
                sumVol=sumVol - listapre[ind][0]

        volumenes=[]
        greedy=[]
        indices=[]
        for i in range(len(mochila)):
            volumenes.append(mochila[i][0])#muestra volúmenes
        for i in range(len(mochila)):
            greedy.append(float(mochila[i][1]/mochila[i][0]))#muestra cociente Greedy
        for i in range(len(mochila)):
            for j in range(10):
                if (mochila[i]==listapre[j]):
                    indices.append(j+1)


        print(volumenes)
        print(greedy)
        print(indices)
        print(sumPrecio)
        print(sumVol)


    if(opc==3): 
        lista=[[1800],[600],[1200]]
        listapeso=[1800,600,1200]
        listapre=[[1800,72],[600,36],[1200,60]]
        combinaciones=[]
        for i in range(len(lista)): #Crea Lista de combinaciones
            combinaciones.append([]) 

        for a in range(len(lista)):
            combinaciones[0].append(lista[a])
            for b in range(a+1,len(lista)):
                combinaciones[1].append(lista[a] + lista[b])
                for c in range(b+1,len(lista)):
                    combinaciones[2].append(lista[a] + lista[b] + lista[c])

        combinacionesvol=[]
        for i in range (len(combinaciones)): #Filtra volumenes menores o iguales a 3000
            for j in range (len(combinaciones[i])):
                sum=0
                for k in range (len(combinaciones[i][j])):
                    sum= sum + combinaciones[i][j][k]
                if (sum<=3000):
                    combinacionesvol.append(combinaciones[i][j])
        mx=0
        sumPeso=0
        listaindice=[]
        for i in range (len(combinacionesvol)): #busca y suma el beneficio de cada combinacion, y guarda la de mayor beneficio
            sum=0
            sumP=0
            for j in range (len(combinacionesvol[i])):
                ind=listapeso.index(combinacionesvol[i][j])
                sum= sum+ listapre[ind][1]
                sumP= sumP + listapre[ind][0]
            if (sum>mx):
                indmax=i
                mx=sum
                sumPeso=sumP
        for i in range (len(combinacionesvol[indmax])):
            ind=listapeso.index(combinacionesvol[indmax][i])
            listaindice.append(ind+1)

        print(combinacionesvol[indmax]) #Combinacion de mayor beneficio
        print(listaindice) #Indices de los elementos
        print(mx) #Valor del beneficio        
        print(sumPeso)


    if(opc==4): 
        listapre=[[1800,72],[600,36],[1200,60]]
        listaGreedy=[]
        listaOrdenada=[]

        for i in range(3):
            listaGreedy.append(float(listapre[i][1]/listapre[i][0]))
        listaOrdenada=sorted(listaGreedy,reverse=True)

        mochila=[]
        sumPeso=0
        sumPrecio=0
        for i in range(3):
            for j in range(3):
                if (listaOrdenada[i]==float(listapre[j][1]/listapre[j][0])):
                    ind=j
            sumPeso= sumPeso + listapre[ind][0]
            if sumPeso<=3000:
                mochila.append(listapre[ind])
                sumPrecio= sumPrecio + listapre[ind][1]
            else:
                sumPeso=sumPeso - listapre[ind][0]

        pesos=[]
        greedy=[]
        indices=[]
        for i in range(len(mochila)):
            pesos.append(mochila[i][0])#muestra volúmenes
        for i in range(len(mochila)):
            greedy.append(float(mochila[i][1]/mochila[i][0]))#muestra cociente Greedy
        for i in range(len(mochila)):
            for j in range(3):
                if (mochila[i]==listapre[j]):
                    indices.append(j+1)


        print(pesos)
        print(greedy)
        print(indices)
        print(sumPrecio)
        print(sumPeso)
