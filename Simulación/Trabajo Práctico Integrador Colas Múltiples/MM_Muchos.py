import numpy as np
from matplotlib import pyplot
import random


class Cliente(object):
    def __init__(self, tiempo):
        self.tiempo = tiempo
        self.ingreso = tiempo
        self.prioridad = random.random()

class Servidor(object):
    def __init__(self, tasa):
        self.tasa = tasa
        self.cli = None
        self.tiempo_entrada = 0
        self.areaBdeT = 0
        self.UPS = 0


class Cola(object):
    def __init__(self):
        self.colaEsp = []
        self.areaQdeT = 0
        
        self.ultimoEvento = 0
        self.NPCC = 0


class Simulacion(object):
    def __init__(self):
        """Constructor que inicializa las variables de la simulacion."""
        self.TMArribo = 0.8  # Tiempo medio de arribo cola 0
        self.servidores = [Servidor(0.5), Servidor(0.5), Servidor(0.5), Servidor(0.2), Servidor(0.4),
                           Servidor(0.6)]  # Arreglo para los tiempos de partidas de cada servidor
        self.colas = [Cola(), Cola(), Cola(), Cola()]  # Arreglo para guardar los arribos en cada cola
        self.reloj = 0
        self.relof_final = 0
        self.proxEvento = []
        self.tiempoSimu = []
        self.colaArr = []
        self.TPS = 0

    def exponential(self, tasa):
        """Devuelve un valor aleatorio de la funcion exponencial con la tasa indicada"""
        return np.random.exponential(tasa)

    def Inicializacion(self):
        """Inicializa el arreglo con los primeros eventos"""
        self.proxEvento = [[Cliente(self.exponential(self.TMArribo)), 0], [Cliente(99999), 0]]  # Fuerza el primer arribo
        self.colaArr.append(self.proxEvento[0][0])

    def Tiempos(self):
        """Analiza cual es el siguiente evento al cual le da el reloj"""
    
        if self.proxEvento[0][0].tiempo <= self.proxEvento[1][0].tiempo:  # Compara si va un arribo o una partida
            self.reloj = self.proxEvento[0][0].tiempo  # Reasigno el reloj
            self.Arribo(self.proxEvento[0][0], self.proxEvento[0][1])  # Invoco un arribo con la cola a la que pertenece 
        else:
            self.reloj = self.proxEvento[1][0].tiempo  # Reasigno el reloj
            self.Partida(self.proxEvento[1][0], self.proxEvento[1][1])  # Invoco partida con el servidor al que pertenece
        ult_tiempo = min(self.proxEvento[0][0].tiempo,self.proxEvento[1][0].tiempo)
        if ult_tiempo>500:
            self.reloj_final = self.reloj 

    def Arribo(self, cli, cola):
        ser = self.Evaluar_Servidor(cola)
        if ser == 31:  # Servidor Ocupado
            self.colas[cola].areaQdeT += len(self.colas[cola].colaEsp) * (self.reloj - self.colas[cola].ultimoEvento)
            self.colas[cola].ultimoEvento = self.reloj
            if cola == 0:
                self.colaArr.pop(0)  # Saco al cliente de la cola de arribos
            self.colas[cola].colaEsp.append(cli)  # Asigno cliente en cola de espera
        else:
            
            cli.tiempo = self.reloj + self.exponential(self.servidores[ser].tasa)  # Genero nueva partida y cambio la variable de la clase
            self.servidores[ser].cli = cli  # Agrego cliente al servidor
            self.servidores[ser].tiempo_entrada = self.reloj
            if cola == 0:
                self.colaArr.pop(0)

            pos = self.BuscaMin()
            
            self.proxEvento[1] = [self.servidores[pos].cli, pos]
        if cola == 0:
            cli = Cliente(self.reloj + self.exponential(self.TMArribo))
            self.colaArr.append(cli)  # Busco el prox arribo
            self.proxEvento[0] = [self.colaArr[0], 0]  # Cargo el proximo arribo

    def Partida(self, cli, servidor):
        if servidor == 0 or servidor == 1 or servidor == 2: #analiza si es la primer linea de servidores o la segunda
           
            col = self.Evaluar_Cola_sig(servidor)
            self.Arribo(cli, col) #genera arribo para cola 1, 2 o 3
        else:
            self.tiempoSimu.append(self.reloj - cli.ingreso) #Acumula tiempo
        self.servidores[servidor].areaBdeT += self.reloj - self.servidores[servidor].tiempo_entrada
        cola = self.Evaluar_Cola(servidor) #Evalua la cola anterior de la que vino el cliente
        if len(self.colas[cola].colaEsp) == 0:
            self.servidores[servidor].cli = None
        else:
            pos = self.FIFO()
            self.servidores[servidor].cli = self.colas[cola].colaEsp[pos]
            self.servidores[servidor].cli.tiempo = self.reloj + self.exponential(self.servidores[servidor].tasa)
            self.servidores[servidor].tiempo_entrada = self.reloj
            self.colas[cola].areaQdeT += len(self.colas[cola].colaEsp) * (self.reloj - self.colas[cola].ultimoEvento)
            self.colas[cola].ultimoEvento = self.reloj
            self.colas[cola].colaEsp.pop(pos)
        ser = self.BuscaMin()
     
        if ser == 31:
            self.proxEvento[1] = [Cliente(99999), 0] #Fuerza arribo si no hay nadie en el sistema
        else:
            self.proxEvento[1] = [self.servidores[ser].cli, ser]

    def Run(self):
        self.Inicializacion()
        while True: 
            self.Tiempos()
         
            if  self.reloj > 500:
                break
        self.reloj = self.reloj_final
        self.Reporte()


    def FIFO(self):
        return 0

    def LIFO(self, cola):
        if cola == 0:
            return len(self.colas[0].colaEsp) - 1
        else:

            return 0

    def Prioridad(self, cola):
        if cola == 0:
            priori = []
            for c in self.colas[0].colaEsp:
                priori.append(c.prioridad)
            if min(priori) <= 0.03:
                return priori.index(min(priori))
            else:
                return 0
        else:
            return 0

    def Reporte(self):
        i = 0
        for c in self.colas:
            c.NPCC = c.areaQdeT / self.reloj #Numero promedio de clientes en cola
            
            NPCCTot[i].append(c.NPCC)
            npcprom = sum(NPCCTot[i])/len(NPCCTot[i])
            NPCCProm[i].append(npcprom)
            i += 1
        i = 0
        for s in self.servidores:
            s.UPS = s.areaBdeT / self.reloj #Utilizacion promedio del servidor
    
            UPSTot[i].append(s.UPS)
            UPSProm[i].append(sum(UPSTot[i])/len(UPSTot[i]))
            i += 1
        self.TPS = sum(self.tiempoSimu) / len(self.tiempoSimu) #Tiempo promedio de la simulacion x cliente
        TPSTot.append(self.TPS)
        TPSProm.append(sum(TPSTot)/len(TPSTot))
      

    def Analisis(self):
        for i in range(4):
            self.Graficar(NPCCProm[i], "Nro Prom de Clientes en Cola Promedio.")
            print(NPCCProm[i][-1])
        for i in range(6):
            self.Graficar(UPSProm[i], "Utilizacion Prom de Servidores Promedio.")
            print(UPSProm[i][-1])
        self.Graficar(TPSProm, "Tiempo Prom de Servicio Promedio")
        print(TPSProm[-1])

    def Graficar(self, valor, tit):
        pyplot.plot(valor)
        pyplot.suptitle(tit)
        pyplot.show()

    def Evaluar_Servidor(self, cola):
        if cola == 0:
            dispo = []
            for i in range(3):
                if self.servidores[i].cli is None:
                    dispo.append(i)
            if len(dispo) != 0:
                return random.choice(dispo)
            """for i in range(3):
                if self.servidores[i].cli is None:
                    return i"""

        elif self.servidores[cola + 2].cli is None:
            return cola + 2
        return 31

    def BuscaMin(self):
        """Analiza la proxima partida con el menor tiempo y devuelve el servidor"""
        tiempo = []
        for i in range(6):
            if self.servidores[i].cli is not None:
                tiempo.append(self.servidores[i].cli.tiempo)
            else:
                tiempo.append(99999)
        if tiempo.count(99999) != 6:
            return tiempo.index(min(tiempo))
        else:
            return 31

    def Evaluar_Cola(self, servidor):  # Segunda Linea de Colas
        if servidor == 0 or servidor == 1 or servidor == 2:
            return 0
        else:
            return servidor - 2

    def Evaluar_Cola_sig(self,servidor):
        return  servidor + 1
        
    def Evaluar_Cola_Mejorado(self):  # Segunda Linea de Colas
        disp = [] #Primero analizo si algun servidor esta disponible, por orden prioriza los mas rapidos
        for i in range (3):
            if self.servidores[i+3].cli == None:
                disp.append(0)
            else:
                disp.append(1)
        if disp.count(1) != 3:
            for i in range(3):
                if disp[i] == 0:
                    return i+1
        gente_colas = []
       
        for c in range(3):
            cant_gente = len(self.colas[c+1].colaEsp)
            gente_colas.append(cant_gente)
            #if(cant_gente != 0):
             #   band = False
        #if band == True:
         #   return random.randint(1,3)
        #else:
        return gente_colas.index(min(gente_colas)) +1



NPCCTot3 = []
UPSTot3 = []
TPSTot3 = []
for i1 in range(3):
    NPCCTot = [[],[],[],[]]
    UPSTot = [[],[],[],[],[],[]]
    TPSTot = []
    UPSProm = [[],[],[],[],[],[]]
    TPSProm = []
    NPCCProm = [[],[],[],[]]
    for i in range(500):
        print(i)
        sim = Simulacion()
        sim.Run()
    #sim.Analisis()
    NPCCTot3.append(NPCCProm)
    UPSTot3.append(UPSProm)
    TPSTot3.append(TPSProm)

for i in range(4):
    pyplot.title("NPCC Cola: "+str(i))
    pyplot.plot(NPCCTot3[0][i])
    pyplot.plot(NPCCTot3[1][i])
    pyplot.plot(NPCCTot3[2][i])
    pyplot.show()
for i in range(6):
    pyplot.title("UPS Servidor: "+str(i))
    pyplot.plot(UPSTot3[0][i])
    pyplot.plot(UPSTot3[1][i])
    pyplot.plot(UPSTot3[2][i])
    pyplot.show()
pyplot.title("Tiempo Promedio de Servicio: "+str(i))
pyplot.plot(TPSTot3[0])
pyplot.plot(TPSTot3[1])
pyplot.plot(TPSTot3[2])
pyplot.show()

