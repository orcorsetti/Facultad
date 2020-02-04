from graphics import *


def conjunto_Cantor(win,x,y,h,Len,tope): 

    if Len < tope: return

    line = Line(Point(x, y), Point(x+Len, y)) #la línea usa dos argumentos, que son los vértices al igual que en OPENGL
    line.setWidth(10)
    line.draw(win)
    #la doble barra realiza un truncamiento
    conjunto_Cantor(win,x,y+h,h,Len//3,tope)
    conjunto_Cantor(win,x+Len*2//3,y+h,h,Len//3,tope)

def inicializar():
    Len = 500 #Largo de línea
    tope=Len
    for i in range(5):
        tope=tope//3
    win = GraphWin("Conjunto de Cantor", Len+300, 600) #dibujo las medidas y nombre de la ventana que muestra la salida
    conjunto_Cantor(win,150,10,80,Len,tope) #Parámetros: Datos de ventana + Sep. Izquierda + Sep. Superior + Sep. "Renglones" + Largo Inicial de Línea + Condicion Final
    win.getKey() #llamo a esta función para que la ventana no se cierre automáticamente ()
    win.close()

inicializar()
