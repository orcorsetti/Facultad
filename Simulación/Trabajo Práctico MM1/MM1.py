import  numpy as np
from array import array
from matplotlib import pyplot


NPCC=array('f')
UTSer=array('f')
NPCProm= array('f')
UTSerProm=array('f')
DemCli=array('f')
DemCliProm= array('f')
npcc=int


class Simulador(object):


    def __init__(self):
        """Constructor que inicializa las variables"""
        self.Reloj = 0.0
        self.EstadoServidor = ""
        self.ProximoEvento = ""
        self.ListaDeEventos = array('f')
        self.Cola = array('f')
        self.TSAcumulado = 0.0
        self.DemoraAcumulada = 0.0
        self.NroDeClientesEnCola = 0
        self.AreaQDeT = 0.0
        self.TiempoUltimoEvento = 0.0
        self.CompletaronDemora = 0
        self.Paso = 0
        self.TMEntreArribos = 7.0
        self.TMDeServicio = 9.0
        self.Iniciado = False


    # Sub Inicializar()
    def inicializar(self):


        self.Reloj = 0
        self.EstadoServidor = "D"
        self.ProximoEvento = ""
        self.TSAcumulado = 0
        self.DemoraAcumulada = 0
        self.NroDeClientesEnCola = 0
        self.AreaQDeT = 0
        self.TiempoUltimoEvento = 0
        self.CompletaronDemora = 0

        #Calculo el tiempo de primer arribo
        self.ListaDeEventos.append(valorExponencial(self.TMEntreArribos))

        #Fuerza a que el primer evento no sea una partida
        self.ListaDeEventos.append(99999.0)
        self.Paso = 0
        self.Iniciado = False

    # Sub Principal()
    def run(self):
        # Llamo a la rutina de inicializacion
        self.inicializar()

        # Loop Until Reloj >= 8 And NroDeClientesEnCola = 0 And EstadoServidor = "D"
        while True:
            # llamada a la rutina de tiempos
            self.tiempos()

            # llamada a la rutina correspondiente en funciÃ³n del tipo de evento

            if self.ProximoEvento == "ARRIBOS":
                self.arribos()
            else:
                self.partidas()

            if self.Reloj >= 50 and self.NroDeClientesEnCola == 0 and self.EstadoServidor == "D":
                break

        self.reportes()

    def arribos(self):
        # Todo arribo desencadena un nuevo arribo
        self.ListaDeEventos[0] = self.Reloj + valorExponencial(self.TMEntreArribos)

        # Pregunto si el servidor estÃ¡ desocupado

        if self.EstadoServidor == "D":
            # Cambio el estado del servidor a "Ocupado"
            self.EstadoServidor = "O"

            # Programo el proximo evento partida
            self.ListaDeEventos[1] = self.Reloj + valorExponencial(self.TMDeServicio)

            # Acumulo el tiempo de servicio
            self.TSAcumulado += (self.ListaDeEventos[1] - self.Reloj)

            # Actualizo la cantidad de clientes que completaron la demora

            self.CompletaronDemora += 1

        else:
            # Calculo el Área bajo Q(t) desde el momento actual del reloj hacia atrÃ¡s (TiempoUltimoEvento)

            self.AreaQDeT += (self.NroDeClientesEnCola * (self.Reloj - self.TiempoUltimoEvento))

            # Incremento la cantidad de clientes en cola en uno (1)
            self.NroDeClientesEnCola += 1

            #Guardo el valor del reloj en la posiciÃ³n "NroDeClientesEnCola" para saber cuando llegÃ³
            #el cliente a la cola y mÃ¡s adelante calcular la demora.

            self.Cola.append(self.Reloj)

    def partidas(self):
        # Pregunto si hay clientes en cola
        if self.NroDeClientesEnCola > 0:
            # Tiempo del prÃ³ximo evento partida
            self.ListaDeEventos[1] = self.Reloj + valorExponencial(self.TMDeServicio)

            # Acumulo la demora acumulada como el valor actual del reloj
            # menos el valor del reloj cuando el cliente ingresÃ³ a la cola
            self.DemoraAcumulada += self.Reloj - self.Cola[0]

            #  Actualizo el contador de clientes que completaron la demora
            self.CompletaronDemora += 1

            #  Acumulo el tiempo de servicio
            self.TSAcumulado += (self.ListaDeEventos[1] - self.Reloj)
            #
            # Calculo el Área bajo Q(t) del periodo anterior (Reloj - TiempoUltimoEvento)
            self.AreaQDeT += (self.NroDeClientesEnCola * (self.Reloj - self.TiempoUltimoEvento))
            #
            # Decremento la cantidad de clientes en cola en uno (1)
            self.NroDeClientesEnCola -= 1

            # Llamo a la rutina encargada de gestionar la cola
            # En este caso deberÃ¡ desplazar todos los valores una posiciÃ³n hacia adelante

            self.Cola.pop(0)
        else:
            #Al no haber clientes en cola, establezco el estado del servidor en "DesOcupado"
            self.EstadoServidor = "D"

            # Fuerza a que no haya partidas si no hay clientes atendiendo
            self.ListaDeEventos[1] = 99999.0

    def tiempos(self):
        self.TiempoUltimoEvento = self.Reloj
        if self.ListaDeEventos[0] <= self.ListaDeEventos[1]:
            self.Reloj = self.ListaDeEventos[0]
            self.ProximoEvento = "ARRIBOS"
        else:
            self.Reloj = self.ListaDeEventos[1]
            self.ProximoEvento = "PARTIDAS"


    def reportes(self):
        var=0
        var4=0
        var5=0
        try:
            var1 = self.AreaQDeT / self.Reloj
        except ZeroDivisionError:
            var1 = 0

        print("Nro promedio de cli en cola:", var1)

        NPCC.append(var1)

        for i in NPCC:
            var+=i
        var=var/len(NPCC)
        NPCProm.append(var)

        try:
            var2 = self.TSAcumulado / self.Reloj
        except ZeroDivisionError:
            var2 = 0
        print("Utilización promedio de los servidores:", var2)

        UTSer.append(var2)

        for i in UTSer:
            var4+=i
        var4=var4/len(UTSer)
        UTSerProm.append(var4)

        try:
            var3 = self.DemoraAcumulada / self.CompletaronDemora
        except ZeroDivisionError:
            var3 = 0

        print("Demora promedio por cliente:", var3)

        DemCli.append(var3)

        for i in DemCli:
            var5+=i
        var5=var5/len(DemCli)
        DemCliProm.append(var5)

    def DPPC(self):
        dppc = (self.TMEntreArribos)/((self.TMDeServicio)*((self.TMDeServicio)-(self.TMEntreArribos)))
        print("Demora promedio por cliente:", dppc)
        self.Graficar(dppc, DemCliProm,"Demora promedio por cliente.")

    def UPS(self):
        ups = (self.TMEntreArribos)/(self.TMDeServicio)
        print("Utilizacion promedio de los servidores:", ups)
        self.Graficar(ups, UTSerProm,"Utilizacion promedio de los servidores")

    def NPCC(self):
        npcc = ((self.TMEntreArribos)**2)/((self.TMDeServicio)*((self.TMDeServicio)-(self.TMEntreArribos)))
        print("Nro promedio de cli en cola:", npcc)
        self.Graficar(npcc, NPCProm, "Nro promedio de cli en cola.")


    def Graficar(self, var, valor,tit):
        x = range(0, 1000)
        datos = []
        for i in range(1000):
            datos.append(var)

        pyplot.plot(x, datos,"r--")
        pyplot.plot(valor)
        pyplot.suptitle(tit)
        pyplot.show()

    def Analitica(self):
        self.NPCC()
        self.UPS()
        self.DPPC()




def valorExponencial(media):
    return np.random.exponential(1/media)

def quitarDeLaCola(pcola):
    ncola = len(pcola)
    for i in range(ncola):
        pcola[i] = pcola[i + 1]
    pcola[ncola] = ""



for i in range(1000):
    sim1 = Simulador()
    sim1.run()

sim1.Analitica()
