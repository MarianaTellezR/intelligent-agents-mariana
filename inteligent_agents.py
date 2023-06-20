import time
import random

#Elementos MODO REACTIVO

maze = [["#","E", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#","O", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
        ["#"," ", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
        ["#"," ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
        ["#"," ", "#", " ", "#", " ", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#"],
        ["#"," ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
        ["#"," ", "#", " ", "#", " ", "#", " ", "#", "X", " ", "#", "#", "#", " ", "#"],
        ["#"," ", " ", " ", " ", " ", "c", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
        ["#","a", "#", "#", " ", "#", "#", "#", "#", " ", "#", "#", " ", " ", " ", "#"],
        ["#"," ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#"],
        ["#"," ", "#", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["#"," ", "#", " ", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
        ["P"," ", " ", " ", " ", " ", " ", " ", " ", " ", "b", " ", " ", " ", " ", "#"],
        ["#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

pasos = ["C"]    
estatusSpy = 0

#Elementos MODO COLABORATIVO

mazee = [["#","E", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
         ["#","O", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#"],
         ["#"," ", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
         ["#","a", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
         ["#"," ", "#", " ", "#", " ", "#", "c", "#", "#", "#", " ", "#", "#", "#", "#"],
         ["#"," ", " ", "b", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
         ["#"," ", "#", " ", "#", " ", "#", " ", "#", "X", " ", "#", "#", "#", " ", "#"],
         ["#"," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
         ["#"," ", "#", "#", " ", "#", "#", " ", "#", " ", "#", "#", " ", " ", " ", "#"],
         ["#"," ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
         ["#"," ", " ", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#"],
         ["#"," ", "#", " ", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
         ["P"," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
         ["#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

ppasos = ["C"]    
statusSpyC = 0

turno = 0
turnoA = 0
turnoB = 0
turnoC = 0

alerta = 0
alertaX = 0
alertaY = 0 

arrivedA = 0
arrivedB = 0
arrivedC = 0

#MODO REACTIVO

def mostrarMapaR():
    #Mostramos nuestro mapa en pantalla
    for rows in maze:
        print(*rows)
    time.sleep(0.25)

def Espia():
    encontrao = 0
    #Vamos a encontrar la posicion del espia:
    for f in range(len(maze)):
        for c in maze[f]:
            if (c=="O"):
                x = f
                y = maze[f].index(c)
                estatusSpy = 0
                encontrao = 1
            elif(c=="Q"):
                x = f
                y = maze[f].index(c)
                estatusSpy = 1
                encontrao = 1
    if(encontrao==0):
        estatusSpy = 2

    #Dependiendo de si el espia tiene o no el tesoro, tomamos camino
    if(estatusSpy==0): #TODAVIA NO TIENE TESORO

        #Revisar si tenemos al tesoro en nuestro alrededor
        if(maze[x-1][y]=="X"):
            step = "U"
            pasos.append(step)
            maze[x][y]=" "
            x = x - 1
            maze[x][y]="Q"          
            

        elif(maze[x][y+1]=="X"):
            step = "R"
            pasos.append(step)
            maze[x][y]=" "
            y = y + 1
            maze[x][y]="Q"
            

        elif(maze[x+1][y]=="X"):
            step = "D"
            pasos.append(step)
            maze[x][y]=" "
            x = x + 1
            maze[x][y]="Q"
            

        elif(maze[x][y-1]=="X"):
            step = "L"
            pasos.append(step)
            maze[x][y]=" "
            y = y - 1
            maze[x][y]="Q"
            
        
        #Dependiendo del ultimo paso que dio, hace su siguiente movimiento.
        else:
            if(pasos[-1] == "U"): #UP
                #Puedo ir a izq,der,arriba
                #ARRIBA
                if(maze[x-1][y]==" "): #Espacio
                    step = "U"
                    pasos.append(step)
                    maze[x][y]=" "
                    x = x - 1
                    maze[x][y]="O"
                else:
                    #DERECHA
                    if(maze[x][y+1]==" "): #Espacio
                        step = "R"
                        pasos.append(step)
                        maze[x][y]=" "
                        y = y+1
                        maze[x][y]="O"

                    else:
                        #IZQUIERDA
                        if(maze[x][y-1]==" "): #Espacio
                            step = "L"
                            pasos.append(step)
                            maze[x][y]=" "
                            y = y-1
                            maze[x][y]="O"

            elif(pasos[-1]=="R"): #RIGHT
                #Puedo ir a der,aba,arriba
                #ARRIBA
                if(maze[x-1][y]==" "): #Espacio
                    step = "U"
                    pasos.append(step)
                    maze[x][y]=" "
                    x = x-1
                    maze[x][y]="O"

                else:
                    #DERECHA
                    if(maze[x][y+1]==" "): #Espacio
                        step = "R"
                        pasos.append(step)
                        maze[x][y]=" "
                        y = y+1
                        maze[x][y]="O"

                    else:
                        #ABAJO
                        if(maze[x+1][y]==" "): #Espacio
                            step = "D"
                            pasos.append(step)
                            maze[x][y]=" "
                            x = x+1
                            maze[x][y]="O"

            elif(pasos[-1]=="D"): #DOWN
                #Puedo ir abajo,der,izq
                #DERECHA
                if(maze[x][y+1]==" "): #Espacio
                    step = "R"
                    pasos.append(step)
                    maze[x][y]=" "
                    y = y+1
                    maze[x][y]="O"

                else:
                    #ABAJO
                    if(maze[x+1][y]==" "): #Espacio
                        step = "D"
                        pasos.append(step)
                        maze[x][y]=" "
                        x = x+1
                        maze[x][y]="O"

                    else:
                        #IZQUIERDA
                        if(maze[x][y-1]==" "): #Espacio
                            step = "L"
                            pasos.append(step)
                            maze[x][y]=" "
                            y = y-1
                            maze[x][y]="O"

            elif(pasos[-1]=="L"): #LEFT
                #Puedo ir abajo,arriba,izq
                #ARRIBA
                if(maze[x-1][y]==" "): #Espacio
                    step = "U"
                    pasos.append(step)
                    maze[x][y]=" "
                    x = x-1
                    maze[x][y]="O"

                else:
                    #ABAJO
                    if(maze[x+1][y]==" "): #Espacio
                        step = "D"
                        pasos.append(step)
                        maze[x][y]=" "
                        x = x+1
                        maze[x][y]="O"

                    else:
                        #IZQUIERDA
                        if(maze[x][y-1]==" "): #Espacio
                            step = "L"
                            pasos.append(step)
                            maze[x][y]=" "
                            y = y-1
                            maze[x][y]="O"


            else: #INICIAL
                #CAMINO ARRIBA
                if(maze[x-1][y]==" "): #Espacio
                    step = "U"
                    pasos[0] = step
                    maze[x][y]=" "
                    x = x-1
                    maze[x][y]="O"
        
                else:
                    #CAMINO DERECHA
                    if(maze[x][y+1]==" " and pasos[-1]!="L"): #Espacio
                        step = "R"
                        pasos[0] = step
                        maze[x][y]=" "
                        y = y+1
                        maze[x][y]="O"

                    else:
                        #CAMINO ABAJO
                        if(maze[x+1][y]==" "): #Espacio
                            step = "D"
                            pasos[0] = step
                            maze[x][y]=" "
                            x = x+1
                            maze[x][y]="O"

                        else:
                            #CAMINO IZQUIERDA
                            if(maze[x][y-1]==" "): #Espacio
                                step = "L"
                                pasos[0] = step
                                maze[x][y]=" "
                                y = y-1
                                maze[x][y]="O"

    elif(estatusSpy==1): #YA TIENE SU TESORO
        if(bool(pasos)==False): #Lista vacia, es decir ya llego a inicio
            print("El espia ha llegado a la salida con el tesoro")
            quit()

        elif(bool(pasos)==True): #Lista NO vacia, no hemos llegado a inicio

            if(pasos[-1]=="D"): #Paso fue ABAJO, entonces de regreso va ARRIBA
                if(maze[x-1][y]=="a" or maze[x-1][y]=="b" or maze[x-1][y]=="c"):
                    maze[x][y]=="Q"
                else:
                    maze[x][y]=" "
                    x = x-1
                    maze[x][y]="Q"
                    pasos.pop()
            
            elif(pasos[-1]=="U"): #Paso fue ARRIBA, entonces de regreso va ABAJO
                if(maze[x+1][y]=="a" or maze[x+1][y]=="b" or maze[x+1][y]=="c"):
                    maze[x][y]=="Q"
                else:
                    maze[x][y]=" "
                    x = x+1
                    maze[x][y]="Q"
                    pasos.pop()
            
            elif(pasos[-1]=="R"): #Paso fue DERECHA, entonces de regreso va IZQUIERDA
                if(maze[x][y-1]=="a" or maze[x][y-1]=="b" or maze[x][y-1]=="c"):
                    maze[x][y]=="Q"
                else:
                    maze[x][y]=" "
                    y = y-1
                    maze[x][y]="Q"
                    pasos.pop()
            
            elif(pasos[-1]=="L"): #Paso fue IZQUIERDA, entonces de regreso va DERECHA
                if(maze[x][y+1]=="a" or maze[x][y+1]=="b" or maze[x][y+1]=="c"):
                    maze[x][y]=="Q"
                else:
                    maze[x][y]=" "
                    y = y+1
                    maze[x][y]="Q"
                    pasos.pop()
    elif(estatusSpy==2):
        pass
        
def GuardiaA():
    
    #Vamos a encontrar la posicion del guardia A:
    for f in range(len(maze)):
        for c in maze[f]:
            if (c=="a"):
                x = f
                y = maze[f].index(c)
                estatusGA = 0
                
            elif (c=="A"):
                x = f
                y = maze[f].index(c)
                estatusGA = 1   
                


    #Guardia A sin haber capturado al Espia
    if(estatusGA==0):

        pospaths1 = []

        #Primero revisamos si tenemos al espia cerca

        if(maze[x][y+1]=="O" or maze[x][y+1]=="Q"): #DERECHA ESTA ESPIA
            maze[x][y]=" "
            y = y+1
            maze[x][y]="A"

        elif(maze[x][y-1]=="O" or maze[x][y-1]=="Q"): #IZQUIERDA ESTA ESPIA
            maze[x][y]=" "
            y = y-1
            maze[x][y]="A"  
        
        elif(maze[x+1][y]=="O" or maze[x+1][y]=="Q"): #ABAJO ESTA ESPIA
            maze[x][y]=" "
            x = x+1
            maze[x][y]="A"

        elif(maze[x-1][y]=="O" or maze[x-1][y]=="Q"): #ARRIBA ESTA ESPIA
            maze[x][y]=" "
            x = x-1
            maze[x][y]="A"

        else:
            #Vemos que caminos hay disponibles y los guardamos en una lista:
            if(maze[x][y+1]==" "):
                pospaths1.append("R")

            if(maze[x][y-1]==" "):
                pospaths1.append("L")

            if(maze[x+1][y]==" "):
                pospaths1.append("D")

            if(maze[x-1][y]==" "):
                pospaths1.append("U")

            #Elegimos aleatoriamente uno de esos posibles caminos
    
            step = random.choice(pospaths1)

            #Avanzamos de acuerdo con el paso elegido aleatoriamente

            if(step=="R"): #DERECHA
                maze[x][y]=" "
                y = y+1
                maze[x][y]="a"

            elif(step=="L"): #IZQUIERDA
                maze[x][y]=" "
                y = y-1
                maze[x][y]="a"  
        
            elif(step=="D"): #ABAJO
                maze[x][y]=" "
                x = x+1
                maze[x][y]="a"

            elif(step=="U"): #ARRIBA
                maze[x][y]=" "
                x = x-1
                maze[x][y]="a"

    #Guardia A al haber capturado al espia
    elif(estatusGA==1):
        
        
        #Buscamos antes que nada si la prision esta a un lado 
        if(maze[x][y-1]=="P"): #Ver si esta a IZQUIERDA
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        elif(maze[x+1][y]=="P"): #Ver si esta ABAJO
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        elif(maze[x][y+1]=="P"): #Ver si esta DERECHA
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        elif(maze[x-1][y]=="P"): #Ver si esta ARRIBA
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        else:
            if(maze[x][y-1]==" "): #Busca IZQUIERDA
                maze[x][y]=" "
                y = y - 1
                maze[x][y]="A"
            elif(maze[x+1][y]==" "): #Busca ABAJO
                maze[x][y]=" "
                x = x + 1
                maze[x][y]="A"
            elif(maze[x][y+1]==" "): #Busca DERECHA
                maze[x][y]=" "
                y = y + 1
                maze[x][y]="A"
            elif(maze[x-1][y]==" "): #Busca ARRIBA
                maze[x][y]=" "
                x = x - 1
                maze[x][y]="A"
        
def GuardiaB():
    
    #Vamos a encontrar la posicion del guardia B:
    for f in range(len(maze)):
        for c in maze[f]:
            if (c=="b"):
                x = f
                y = maze[f].index(c)
                estatusGB = 0
                
            elif (c=="B"):
                x = f
                y = maze[f].index(c)
                estatusGB = 1   
                


    #Guardia B sin haber capturado al Espia
    if(estatusGB==0):

        pospaths2 = []

        #Primero revisamos si tenemos al espia cerca

        if(maze[x][y+1]=="O" or maze[x][y+1]=="Q"): #DERECHA ESTA ESPIA
            maze[x][y]=" "
            y = y+1
            maze[x][y]="B"

        elif(maze[x][y-1]=="O" or maze[x][y-1]=="Q"): #IZQUIERDA ESTA ESPIA
            maze[x][y]=" "
            y = y-1
            maze[x][y]="B"  
        
        elif(maze[x+1][y]=="O" or maze[x+1][y]=="Q"): #ABAJO ESTA ESPIA
            maze[x][y]=" "
            x = x+1
            maze[x][y]="B"

        elif(maze[x-1][y]=="O" or maze[x-1][y]=="Q"): #ARRIBA ESTA ESPIA
            maze[x][y]=" "
            x = x-1
            maze[x][y]="B"

        else:
            #Vemos que caminos hay disponibles y los guardamos en una lista:
            if(maze[x][y+1]==" "):
                pospaths2.append("R")

            if(maze[x][y-1]==" "):
                pospaths2.append("L")

            if(maze[x+1][y]==" "):
                pospaths2.append("D")

            if(maze[x-1][y]==" "):
                pospaths2.append("U")

            #Elegimos aleatoriamente uno de esos posibles caminos
    
            step = random.choice(pospaths2)

            #Avanzamos de acuerdo con el paso elegido aleatoriamente

            if(step=="R"): #DERECHA
                maze[x][y]=" "
                y = y+1
                maze[x][y]="b"

            elif(step=="L"): #IZQUIERDA
                maze[x][y]=" "
                y = y-1
                maze[x][y]="b"  
        
            elif(step=="D"): #ABAJO
                maze[x][y]=" "
                x = x+1
                maze[x][y]="b"

            elif(step=="U"): #ARRIBA
                maze[x][y]=" "
                x = x-1
                maze[x][y]="b"

    #Guardia A al haber capturado al espia
    elif(estatusGB==1):
        
        
        #Buscamos antes que nada si la prision esta a un lado 
        if(maze[x][y-1]=="P"): #Ver si esta a IZQUIERDA
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        elif(maze[x+1][y]=="P"): #Ver si esta ABAJO
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        elif(maze[x][y+1]=="P"): #Ver si esta DERECHA
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        elif(maze[x-1][y]=="P"): #Ver si esta ARRIBA
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        else:
            if(maze[x][y-1]==" "): #Busca IZQUIERDA
                maze[x][y]=" "
                y = y - 1
                maze[x][y]="B"
            elif(maze[x+1][y]==" "): #Busca ABAJO
                maze[x][y]=" "
                x = x + 1
                maze[x][y]="B"
            elif(maze[x][y+1]==" "): #Busca DERECHA
                maze[x][y]=" "
                y = y + 1
                maze[x][y]="B"
            elif(maze[x-1][y]==" "): #Busca ARRIBA
                maze[x][y]=" "
                x = x - 1
                maze[x][y]="B"    

def GuardiaC():
    
    #Vamos a encontrar la posicion del guardia C:
    for f in range(len(maze)):
        for c in maze[f]:
            if (c=="c"):
                x = f
                y = maze[f].index(c)
                estatusGC = 0
                
            elif (c=="C"):
                x = f
                y = maze[f].index(c)
                estatusGC = 1   
                


    #Guardia C sin haber capturado al Espia
    if(estatusGC==0):

        pospaths3 = []

        #Primero revisamos si tenemos al espia cerca

        if(maze[x][y+1]=="O" or maze[x][y+1]=="Q"): #DERECHA ESTA ESPIA
            maze[x][y]=" "
            y = y+1
            maze[x][y]="C"

        elif(maze[x][y-1]=="O" or maze[x][y-1]=="Q"): #IZQUIERDA ESTA ESPIA
            maze[x][y]=" "
            y = y-1
            maze[x][y]="C"  
        
        elif(maze[x+1][y]=="O" or maze[x+1][y]=="Q"): #ABAJO ESTA ESPIA
            maze[x][y]=" "
            x = x+1
            maze[x][y]="C"

        elif(maze[x-1][y]=="O" or maze[x-1][y]=="Q"): #ARRIBA ESTA ESPIA
            maze[x][y]=" "
            x = x-1
            maze[x][y]="C"

        else:
            #Vemos que caminos hay disponibles y los guardamos en una lista:
            if(maze[x][y+1]==" "):
                pospaths3.append("R")

            if(maze[x][y-1]==" "):
                pospaths3.append("L")

            if(maze[x+1][y]==" "):
                pospaths3.append("D")

            if(maze[x-1][y]==" "):
                pospaths3.append("U")

            #Elegimos aleatoriamente uno de esos posibles caminos
    
            step = random.choice(pospaths3)

            #Avanzamos de acuerdo con el paso elegido aleatoriamente

            if(step=="R"): #DERECHA
                maze[x][y]=" "
                y = y+1
                maze[x][y]="c"

            elif(step=="L"): #IZQUIERDA
                maze[x][y]=" "
                y = y-1
                maze[x][y]="c"  
        
            elif(step=="D"): #ABAJO
                maze[x][y]=" "
                x = x+1
                maze[x][y]="c"

            elif(step=="U"): #ARRIBA
                maze[x][y]=" "
                x = x-1
                maze[x][y]="c"

    #Guardia A al haber capturado al espia
    elif(estatusGC==1):
        
        
        #Buscamos antes que nada si la prision esta a un lado 
        if(maze[x][y-1]=="P"): #Ver si esta a IZQUIERDA
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        elif(maze[x+1][y]=="P"): #Ver si esta ABAJO
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        elif(maze[x][y+1]=="P"): #Ver si esta DERECHA
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        elif(maze[x-1][y]=="P"): #Ver si esta ARRIBA
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        else:
            if(maze[x][y-1]==" "): #Busca IZQUIERDA
                maze[x][y]=" "
                y = y - 1
                maze[x][y]="C"
            elif(maze[x+1][y]==" "): #Busca ABAJO
                maze[x][y]=" "
                x = x + 1
                maze[x][y]="C"
            elif(maze[x][y+1]==" "): #Busca DERECHA
                maze[x][y]=" "
                y = y + 1
                maze[x][y]="C"
            elif(maze[x-1][y]==" "): #Busca ARRIBA
                maze[x][y]=" "
                x = x - 1
                maze[x][y]="C"

#MODO COLABORATIVO

def mostrarMapaC():
    #Mostramos nuestro mapa en pantalla
    for rows in mazee:
        print(*rows)
    time.sleep(0.25)
    
def Espia_Colab():
    encontrao = 0
    global turno
    global alerta
    global alertaX
    global alertaY

    #Vamos a encontrar la posicion del espia:
    for f in range(len(mazee)):
        for c in mazee[f]:
            if (c=="O"):
                x = f
                y = mazee[f].index(c)
                statusSpyC = 0
                encontrao = 1
            elif(c=="Q"):
                x = f
                y = mazee[f].index(c)
                statusSpyC = 1
                encontrao = 1
    if(encontrao==0):
        statusSpyC = 2
        alerta = 0
        alertaX = 0
        alertaY = 0

    

    #Dependiendo de si el espia tiene o no el tesoro, tomamos camino
    if(statusSpyC==0): #TODAVIA NO TIENE TESORO
        cantidadG = 0
        #Revisamos si hay guardias a un lado
        if(mazee[x][y+1]=="a" or mazee[x][y+1]=="b" or mazee[x][y+1]=="c"): #DERECHA 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "R"
        if(mazee[x+1][y]=="a" or mazee[x+1][y]=="b" or mazee[x+1][y]=="c"): #ABAJO 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "D"
        if(mazee[x][y-1]=="a" or mazee[x][y-1]=="b" or mazee[x][y-1]=="c"): #IZQUIERDA 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "L"
        if(mazee[x-1][y]=="a" or mazee[x-1][y]=="b" or mazee[x-1][y]=="c"): #ARRIBA 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "U"
        

        if(cantidadG==0):
            
            #Revisar si tenemos al tesoro en nuestro alrededor
            if(mazee[x-1][y]=="X"):
                step = "U"
                ppasos.append(step)
                mazee[x][y]=" "
                x = x - 1
                mazee[x][y]="Q"          
            

            elif(mazee[x][y+1]=="X"):
                step = "R"
                ppasos.append(step)
                mazee[x][y]=" "
                y = y + 1
                mazee[x][y]="Q"
            

            elif(mazee[x+1][y]=="X"):
                step = "D"
                ppasos.append(step)
                mazee[x][y]=" "
                x = x + 1
                mazee[x][y]="Q"
            

            elif(mazee[x][y-1]=="X"):
                step = "L"
                ppasos.append(step)
                mazee[x][y]=" "
                y = y - 1
                mazee[x][y]="Q"
            
        
            #Dependiendo del ultimo paso que dio, hace su siguiente movimiento.
            else:
                if(ppasos[-1] == "U"): #UP
                    #Puedo ir a izq,der,arriba
                    #ARRIBA
                    if(mazee[x-1][y]==" "): #Espacio
                        step = "U"
                        ppasos.append(step)
                        mazee[x][y]=" "
                        x = x - 1
                        mazee[x][y]="O"
                    else:
                        #DERECHA
                        if(mazee[x][y+1]==" "): #Espacio
                            step = "R"
                            ppasos.append(step)
                            mazee[x][y]=" "
                            y = y+1
                            mazee[x][y]="O"

                        else:
                            #IZQUIERDA
                            if(mazee[x][y-1]==" "): #Espacio
                                step = "L"
                                ppasos.append(step)
                                mazee[x][y]=" "
                                y = y-1
                                mazee[x][y]="O"

                elif(ppasos[-1]=="R"): #RIGHT
                    #Puedo ir a der,aba,arriba
                    #ARRIBA
                    if(mazee[x-1][y]==" "): #Espacio
                        step = "U"
                        ppasos.append(step)
                        mazee[x][y]=" "
                        x = x-1
                        mazee[x][y]="O"

                    else:
                        #DERECHA
                        if(mazee[x][y+1]==" "): #Espacio
                            step = "R"
                            ppasos.append(step)
                            mazee[x][y]=" "
                            y = y+1
                            mazee[x][y]="O"

                        else:
                            #ABAJO
                            if(mazee[x+1][y]==" "): #Espacio
                                step = "D"
                                ppasos.append(step)
                                mazee[x][y]=" "
                                x = x+1
                                mazee[x][y]="O"

                elif(ppasos[-1]=="D"): #DOWN
                    #Puedo ir abajo,der,izq
                    #DERECHA
                    if(mazee[x][y+1]==" "): #Espacio
                        step = "R"
                        ppasos.append(step)
                        mazee[x][y]=" "
                        y = y+1
                        mazee[x][y]="O"

                    else:
                        #ABAJO
                        if(mazee[x+1][y]==" "): #Espacio
                            step = "D"
                            ppasos.append(step)
                            mazee[x][y]=" "
                            x = x+1
                            mazee[x][y]="O"

                        else:
                            #IZQUIERDA
                            if(mazee[x][y-1]==" "): #Espacio
                                step = "L"
                                ppasos.append(step)
                                mazee[x][y]=" "
                                y = y-1
                                mazee[x][y]="O"

                elif(ppasos[-1]=="L"): #LEFT
                    #Puedo ir abajo,arriba,izq
                    #ARRIBA
                    if(mazee[x-1][y]==" "): #Espacio
                        step = "U"
                        ppasos.append(step)
                        mazee[x][y]=" "
                        x = x-1
                        mazee[x][y]="O"

                    else:
                        #ABAJO
                        if(mazee[x+1][y]==" "): #Espacio
                            step = "D"
                            ppasos.append(step)
                            mazee[x][y]=" "
                            x = x+1
                            mazee[x][y]="O"

                        else:
                            #IZQUIERDA
                            if(mazee[x][y-1]==" "): #Espacio
                                step = "L"
                                ppasos.append(step)
                                mazee[x][y]=" "
                                y = y-1
                                mazee[x][y]="O"


                else: #INICIAL
                    #CAMINO ARRIBA
                    if(mazee[x-1][y]==" "): #Espacio
                        step = "U"
                        ppasos[0] = step
                        mazee[x][y]=" "
                        x = x-1
                        mazee[x][y]="O"
        
                    else:
                        #CAMINO DERECHA
                        if(mazee[x][y+1]==" " and ppasos[-1]!="L"): #Espacio
                            step = "R"
                            ppasos[0] = step
                            mazee[x][y]=" "
                            y = y+1
                            mazee[x][y]="O"

                        else:
                            #CAMINO ABAJO
                            if(mazee[x+1][y]==" "): #Espacio
                                step = "D"
                                ppasos[0] = step
                                mazee[x][y]=" "
                                x = x+1
                                mazee[x][y]="O"

                            else:
                                #CAMINO IZQUIERDA
                                if(mazee[x][y-1]==" "): #Espacio
                                    step = "L"
                                    ppasos[0] = step
                                    mazee[x][y]=" "
                                    y = y-1
                                    mazee[x][y]="O"
        
        elif(cantidadG==1):
            if(turno<=7):
                mazee[x][y]="O"
                turno = turno + 1
                step = "C"
                ppasos.append(step)
            elif(turno>7):
                turno = 0
                alerta = 0
                alertaX = 0
                alertaY = 0
                if(guard=="R"): #KILL GUARD RIGHT
                    step = "R"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    y = y + 1
                    mazee[x][y]="O"
                elif(guard=="D"): #KILL GUARD DOWN
                    step = "D"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    x = x + 1
                    mazee[x][y]="O"
                elif(guard=="L"): #KILL GUARD LEFT
                    step = "L"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    y = y - 1
                    mazee[x][y]="O"
                elif(guard=="U"):
                    step = "U"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    x = x - 1
                    mazee[x][y]="O"
        elif(cantidadG>1):
            pass

    elif(statusSpyC==1): #YA TIENE SU TESORO

        cantidadG = 0

        #Revisamos si hay guardias a un lado
        if(mazee[x][y+1]=="a" or mazee[x][y+1]=="b" or mazee[x][y+1]=="c"): #DERECHA 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "R"
        if(mazee[x+1][y]=="a" or mazee[x+1][y]=="b" or mazee[x+1][y]=="c"): #ABAJO 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "D"
        if(mazee[x][y-1]=="a" or mazee[x][y-1]=="b" or mazee[x][y-1]=="c"): #IZQUIERDA 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "L"
        if(mazee[x-1][y]=="a" or mazee[x-1][y]=="b" or mazee[x-1][y]=="c"): #ARRIBA 1 GUARDIA
            cantidadG = cantidadG + 1
            guard = "U"

        if(cantidadG==0): #NO HAY GUARDIAS A LA VISTA

            if(bool(ppasos)==False): #Lista vacia, es decir ya llego a inicio
                print("El espia ha llegado a la salida con el tesoro")
                quit()

            elif(bool(ppasos)==True): #Lista NO vacia, no hemos llegado a inicio

                if(ppasos[-1]=="D"): #Paso fue ABAJO, entonces de regreso va ARRIBA
                    if(mazee[x-1][y]=="a" or mazee[x-1][y]=="b" or mazee[x-1][y]=="c"):
                        mazee[x][y]=="Q"
                    else:
                        mazee[x][y]=" "
                        x = x-1
                        mazee[x][y]="Q"
                        ppasos.pop()
            
                elif(ppasos[-1]=="U"): #Paso fue ARRIBA, entonces de regreso va ABAJO
                    if(mazee[x+1][y]=="a" or mazee[x+1][y]=="b" or mazee[x+1][y]=="c"):
                        mazee[x][y]=="Q"
                    else:
                        mazee[x][y]=" "
                        x = x+1
                        mazee[x][y]="Q"
                        ppasos.pop()
            
                elif(ppasos[-1]=="R"): #Paso fue DERECHA, entonces de regreso va IZQUIERDA
                    if(mazee[x][y-1]=="a" or mazee[x][y-1]=="b" or mazee[x][y-1]=="c"):
                        mazee[x][y]=="Q"
                    else:
                        mazee[x][y]=" "
                        y = y-1
                        mazee[x][y]="Q"
                        ppasos.pop()
            
                elif(ppasos[-1]=="L"): #Paso fue IZQUIERDA, entonces de regreso va DERECHA
                    if(mazee[x][y+1]=="a" or mazee[x][y+1]=="b" or mazee[x][y+1]=="c"):
                        mazee[x][y]=="Q"
                    else:
                        mazee[x][y]=" "
                        y = y+1
                        mazee[x][y]="Q"
                        ppasos.pop()
                elif(ppasos[-1]=="C"): #Paso fue CENTRO, entonces se queda CENTRO
                    if(mazee[x][y]=="a" or mazee[x][y]=="b" or mazee[x][y]=="c"):
                        mazee[x][y]=="Q"
                    else:
                        mazee[x][y]=" "
                        mazee[x][y]="Q"
                        ppasos.pop()

        elif(cantidadG==1): #TENEMOS UN GUARDIA A UN LADO - FIGHT
            if(turno<=7):
                mazee[x][y]="Q"
                turno = turno + 1
                step = "C"
                ppasos.append(step)
            elif(turno>7):
                turno = 0
                alerta = 0
                alertaX = 0
                alertaY = 0
                if(guard=="R"): #KILL GUARD RIGHT
                    step = "R"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    y = y + 1
                    mazee[x][y]="Q"
                elif(guard=="D"): #KILL GUARD DOWN
                    step = "D"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    x = x + 1
                    mazee[x][y]="Q"
                elif(guard=="L"): #KILL GUARD LEFT
                    step = "L"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    y = y - 1
                    mazee[x][y]="Q"
                elif(guard=="U"): #KILL GUARD UP
                    step = "U"
                    ppasos.append(step)
                    mazee[x][y]=" "
                    x = x - 1
                    mazee[x][y]="Q"
        elif(cantidadG>1):
            pass

    elif(statusSpyC==2):
        pass
       
def GuardiaA_Colab():
    encontrao = 0
    global alerta
    global alertaX
    global alertaY
    global turnoA
    global arrivedA
    global arrivedB
    global arrivedC

    #Vamos a encontrar la posicion del guardia A:
    for f in range(len(mazee)):
        for c in mazee[f]:
            if (c=="a"):
                x = f
                y = mazee[f].index(c)
                estatusGA = 0
                encontrao = 1
                
            elif (c=="A"):
                x = f
                y = mazee[f].index(c)
                estatusGA = 1
                encontrao = 1
    if(encontrao==0):
        estatusGA = 2
                

    #Guardia A sin haber capturado al Espia
    if(estatusGA==0):
        pelea = 0
        pospaths1 = []

        #Primero revisamos si tenemos al espia cerca

        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q"): #DERECHA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x
            alertaY = y + 1      
            spy = "R"

        elif(mazee[x][y-1]=="O" or mazee[x][y-1]=="Q"): #IZQUIERDA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x
            alertaY = y - 1
            spy = "L"
        
        elif(mazee[x+1][y]=="O" or mazee[x+1][y]=="Q"): #ABAJO ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x + 1
            alertaY = y 
            spy = "D"

        elif(mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"): #ARRIBA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x - 1
            alertaY = y
            spy = "U"
        

        #Dependiendo de si tenemos espia a un lado o no y la alarma se hace lo sig

        if(pelea==1 and alerta==1):
            if(turnoA<=7):
                
                turnoA = turnoA + 1
                
                if(arrivedB==1 or arrivedC==1):
                    
                    if(spy=="R"):
                        mazee[x][y]=" "
                        y = y + 1
                        mazee[x][y]="A"

                    elif(spy=="L"):
                        mazee[x][y]=" "
                        y = y - 1
                        mazee[x][y]="A"

                    elif(spy=="D"):
                        mazee[x][y]=" "
                        x = x + 1
                        mazee[x][y]="A"

                    elif(spy=="U"):
                        mazee[x][y]=" "
                        x = x - 1
                        mazee[x][y]="A"

                elif(arrivedB==0 or arrivedC==0):
                    pass

 
            elif(turnoA>7):
                turnoA = 0
                alerta = 0
                alertaX = 0
                alertaY = 0
                pass

        elif(pelea==0 and alerta==1):
            poss = []

            fil = alertaX - x
            col = alertaY - y

            #BUSCAMOS LOS CAMINOS DISPONIBLES ALREDEDOR

            if(mazee[x][y+1]==" "): #DERECHA HAY CAMINO
                poss.append("R")

            if(mazee[x][y-1]==" "): #IZQUIERDA HAY CAMINO
                poss.append("L")
        
            if(mazee[x+1][y]==" "): #ABAJO HAY CAMINO
                poss.append("D")

            if(mazee[x-1][y]==" "): #ARRIBA HAY CAMINO
                poss.append("U")
            
            if(col > 0): #ESPIA ESTA EN LA DIRECCION DERECHA
                if "R" in poss:
                    #Mover derecha
                    mazee[x][y] = " "
                    y = y + 1
                    mazee[x][y] = "a"
                else:
                    if(fil > 0): #ESPIA EN LA DIRECCION ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "a"
                        elif "L" in poss:
                            #Mover izquierda
                            mazee[x][y] = " "
                            y = y - 1
                            mazee[x][y] = "a"
                        elif "U" in poss:
                            #Mover arriba 
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "a"
                    elif(fil < 0): #ESPIA EN LA DIRECCION ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "a"
                        elif "L" in poss:
                            #Mover izquierda
                            mazee[x][y] = " "
                            y = y - 1
                            mazee[x][y] = "a"
                        elif "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "a"
                    else: #fil = 0
                        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                            arrivedA = 1
                            mazee[x][y] = "a"
                        else:
                            pasitos = []

                            if "D" in poss:
                                pasitos.append("D")
                            if "U" in poss:
                                pasitos.append("U")
                            
                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "D"):
                                    mazee[x][y] = " "
                                    x = x + 1
                                    mazee[x][y] = "a"

                                elif(eleccion == "U"):
                                    mazee[x][y] = " "
                                    x = x - 1
                                    mazee[x][y] = "a"

                                pasitos.clear()

                            elif(bool(pasitos)==False):

                                if "L" in poss:
                                    pasitos.append("L")
                                if "R" in poss:
                                    pasitos.append("R")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "L"):
                                        mazee[x][y] = " "
                                        y = y - 1
                                        mazee[x][y] = "a"

                                    elif(eleccion == "R"):
                                        mazee[x][y] = " "
                                        y = y + 1
                                        mazee[x][y] = "a"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    mazee[x][y]="a"
                                    pasitos.clear()

            elif(col < 0): #ESPIA EN DIRECCION IZQUIERDA
                if "L" in poss:
                    #Mover izquierda
                    mazee[x][y] = " "
                    y = y - 1
                    mazee[x][y] = "a"
                else:
                    if(fil > 0): #ESPIA EN DIRECCION ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "a"
                        elif "R" in poss:
                            #Mover Derecha
                            mazee[x][y] = " "
                            y = y + 1
                            mazee[x][y] = "a"
                        elif "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "a"
                    elif(fil < 0): #ESPIA EN DIRECCION ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "a"
                        elif "R" in poss:
                            #Mover derecha
                            mazee[x][y] = " "
                            y = y + 1
                            mazee[x][y] = "a"
                        elif "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "a"
                    else: #fil = 0
                        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):

                            arrivedA = 1
                            mazee[x][y] = "a"

                        else:
                            pasitos = []

                            if "D" in poss:
                                pasitos.append("D")
                            if "U" in poss:
                                pasitos.append("U")
                            
                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "D"):
                                    mazee[x][y] = " "
                                    x = x + 1
                                    mazee[x][y] = "a"

                                elif(eleccion == "U"):
                                    mazee[x][y] = " "
                                    x = x - 1
                                    mazee[x][y] = "a"

                                pasitos.clear()

                            elif(bool(pasitos)==False):

                                if "L" in poss:
                                    pasitos.append("L")
                                if "R" in poss:
                                    pasitos.append("R")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "L"):
                                        mazee[x][y] = " "
                                        y = y - 1
                                        mazee[x][y] = "a"

                                    elif(eleccion == "R"):
                                        mazee[x][y] = " "
                                        y = y + 1
                                        mazee[x][y] = "a"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    maze[x][y] = "a"
                                    pasitos.clear()

            else: #col = 0
                if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                            arrivedA = 1
                            mazee[x][y] = "a"
                else:
                    if(fil > 0): #ESPIA EN LA COLUMNA PERO ESTA ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "a"
                        else:
                            pasitos = []

                            if "L" in poss:
                                pasitos.append("L")
                            if "R" in poss:
                                pasitos.append("R")

                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "L"):
                                    mazee[x][y] = " "
                                    y = y - 1
                                    mazee[x][y] = "a"

                                elif(eleccion == "R"):
                                    mazee[x][y] = " "
                                    y = y + 1
                                    mazee[x][y] = "a"

                                pasitos.clear() 

                            elif(bool(pasitos)==False):

                                if "D" in poss:
                                    pasitos.append("D")
                                if "U" in poss:
                                    pasitos.append("U")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "D"):
                                        mazee[x][y] = " "
                                        x = x + 1
                                        mazee[x][y] = "a"

                                    elif(eleccion == "U"):
                                        mazee[x][y] = " "
                                        x = x - 1
                                        mazee[x][y] = "a"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    maze[x][y] = "a"
                                    pasitos.clear()

                    elif(fil < 0): #ESPIA EN LA COLUMNA PERO ESTA ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "a"
                        else:
                            pasitos = []

                            if "L" in poss:
                                pasitos.append("L")
                            if "R" in poss:
                                pasitos.append("R")

                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "L"):
                                    mazee[x][y] = " "
                                    y = y - 1
                                    mazee[x][y] = "a"

                                elif(eleccion == "R"):
                                    mazee[x][y] = " "
                                    y = y + 1
                                    mazee[x][y] = "a"

                                pasitos.clear() 

                            elif(bool(pasitos)==False):

                                if "D" in poss:
                                    pasitos.append("D")
                                if "U" in poss:
                                    pasitos.append("U")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "D"):
                                        mazee[x][y] = " "
                                        x = x + 1
                                        mazee[x][y] = "a"

                                    elif(eleccion == "U"):
                                        mazee[x][y] = " "
                                        x = x - 1
                                        mazee[x][y] = "a"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    maze[x][y] = "a"
                                    pasitos.clear()

            if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                arrivedA = 1
                mazee[x][y] = "a"
            else:
                arrivedA = 0
                            
            
        elif(pelea==0 and alerta==0):
            #Vemos que caminos hay disponibles y los guardamos en una lista:
            if(mazee[x][y+1]==" "):
                pospaths1.append("R")

            if(mazee[x][y-1]==" "):
                pospaths1.append("L")

            if(mazee[x+1][y]==" "):
                pospaths1.append("D")

            if(mazee[x-1][y]==" "):
                pospaths1.append("U")

            #Elegimos aleatoriamente uno de esos posibles caminos
    
            step = random.choice(pospaths1)

            #Avanzamos de acuerdo con el paso elegido aleatoriamente

            if(step=="R"): #DERECHA
                mazee[x][y]=" "
                y = y+1
                mazee[x][y]="a"

            elif(step=="L"): #IZQUIERDA
                mazee[x][y]=" "
                y = y-1
                mazee[x][y]="a"  
        
            elif(step=="D"): #ABAJO
                mazee[x][y]=" "
                x = x+1
                mazee[x][y]="a"

            elif(step=="U"): #ARRIBA
                mazee[x][y]=" "
                x = x-1
                mazee[x][y]="a"

    #Guardia A al haber capturado al espia
    elif(estatusGA==1):
        
        
        #Buscamos antes que nada si la prision esta a un lado 
        if(mazee[x][y-1]=="P"): #Ver si esta a IZQUIERDA
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x+1][y]=="P"): #Ver si esta ABAJO
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x][y+1]=="P"): #Ver si esta DERECHA
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x-1][y]=="P"): #Ver si esta ARRIBA
            print("Guardia A ha escoltado al espia a la prision.")
            quit()
        else:
            if(mazee[x][y-1]==" "): #Busca IZQUIERDA
                mazee[x][y]=" "
                y = y - 1
                mazee[x][y]="A"
            elif(mazee[x+1][y]==" "): #Busca ABAJO
                mazee[x][y]=" "
                x = x + 1
                mazee[x][y]="A"
            elif(mazee[x][y+1]==" "): #Busca DERECHA
                mazee[x][y]=" "
                y = y + 1
                mazee[x][y]="A"
            elif(mazee[x-1][y]==" "): #Busca ARRIBA
                mazee[x][y]=" "
                x = x - 1
                mazee[x][y]="A"
    elif(estatusGA == 2):
        pass
      
def GuardiaB_Colab():
    encontrao = 0
    global alerta
    global alertaX
    global alertaY
    global turnoB
    global arrivedB
    global arrivedA
    global arrivedC

    #Vamos a encontrar la posicion del guardia B:
    for f in range(len(mazee)):
        for c in mazee[f]:
            if (c=="b"):
                x = f
                y = mazee[f].index(c)
                estatusGB = 0
                encontrao = 1
                
            elif (c=="B"):
                x = f
                y = mazee[f].index(c)
                estatusGB = 1 
                encontrao = 1
    if(encontrao == 0):
        estatusGB = 2
                

    #Guardia B sin haber capturado al Espia
    if(estatusGB==0):
        pelea = 0
        pospaths2 = []

        #Primero revisamos si tenemos al espia cerca

        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q"): #DERECHA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x
            alertaY = y + 1    
            spy = "R"

        elif(mazee[x][y-1]=="O" or mazee[x][y-1]=="Q"): #IZQUIERDA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x
            alertaY = y - 1 
            spy = "L"
        
        elif(mazee[x+1][y]=="O" or mazee[x+1][y]=="Q"): #ABAJO ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x + 1
            alertaY = y
            spy = "D"

        elif(mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"): #ARRIBA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x - 1
            alertaY = y
            spy = "U"
        
        if(pelea==1 and alerta==1):
            if(turnoB<=7):
                
                turnoB = turnoB + 1
                
                if(arrivedA==1 or arrivedC==1):
                    
                    if(spy=="R"):
                        mazee[x][y]=" "
                        y = y + 1
                        mazee[x][y]="B"

                    elif(spy=="L"):
                        mazee[x][y]=" "
                        y = y - 1
                        mazee[x][y]="B"

                    elif(spy=="D"):
                        mazee[x][y]=" "
                        x = x + 1
                        mazee[x][y]="B"

                    elif(spy=="U"):
                        mazee[x][y]=" "
                        x = x - 1
                        mazee[x][y]="B"
                elif(arrivedA==0 or arrivedC==0):
                    pass

            elif(turnoB>7):
                turnoB = 0
                alerta = 0
                alertaX = 0
                alertaY = 0
                pass

        elif(pelea==0 and alerta==1):
            #PELEAAAA
            poss = []

            fil = alertaX - x
            col = alertaY - y

            #BUSCAMOS LOS CAMINOS DISPONIBLES ALREDEDOR

            if(mazee[x][y+1]==" "): #DERECHA HAY CAMINO
                poss.append("R")

            if(mazee[x][y-1]==" "): #IZQUIERDA HAY CAMINO
                poss.append("L")
        
            if(mazee[x+1][y]==" "): #ABAJO HAY CAMINO
                poss.append("D")

            if(mazee[x-1][y]==" "): #ARRIBA HAY CAMINO
                poss.append("U")
            
            if(col > 0): #ESPIA ESTA EN LA DIRECCION DERECHA
                if "R" in poss:
                    #Mover derecha
                    mazee[x][y] = " "
                    y = y + 1
                    mazee[x][y] = "b"
                else:
                    if(fil > 0): #ESPIA EN LA DIRECCION ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "b"
                        elif "L" in poss:
                            #Mover izquierda
                            mazee[x][y] = " "
                            y = y - 1
                            mazee[x][y] = "b"
                        elif "U" in poss:
                            #Mover arriba 
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "b"
                    elif(fil < 0): #ESPIA EN LA DIRECCION ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "b"
                        elif "L" in poss:
                            #Mover izquierda
                            mazee[x][y] = " "
                            y = y - 1
                            mazee[x][y] = "b"
                        elif "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "b"
                    else: #fil = 0
                        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                            arrivedB = 1
                            mazee[x][y] = "b"
                        else:
                            pasitos = []

                            if "D" in poss:
                                pasitos.append("D")
                            if "U" in poss:
                                pasitos.append("U")
                            
                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "D"):
                                    mazee[x][y] = " "
                                    x = x + 1
                                    mazee[x][y] = "b"

                                elif(eleccion == "U"):
                                    mazee[x][y] = " "
                                    x = x - 1
                                    mazee[x][y] = "b"

                                pasitos.clear()

                            elif(bool(pasitos)==False):

                                if "L" in poss:
                                    pasitos.append("L")
                                if "R" in poss:
                                    pasitos.append("R")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "L"):
                                        mazee[x][y] = " "
                                        y = y - 1
                                        mazee[x][y] = "b"

                                    elif(eleccion == "R"):
                                        mazee[x][y] = " "
                                        y = y + 1
                                        mazee[x][y] = "b"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    mazee[x][y]="b"
                                    pasitos.clear()

            elif(col < 0): #ESPIA EN DIRECCION IZQUIERDA
                if "L" in poss:
                    #Mover izquierda
                    mazee[x][y] = " "
                    y = y - 1
                    mazee[x][y] = "b"
                else:
                    if(fil > 0): #ESPIA EN DIRECCION ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "b"
                        elif "R" in poss:
                            #Mover Derecha
                            mazee[x][y] = " "
                            y = y + 1
                            mazee[x][y] = "b"
                        elif "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "b"
                    elif(fil < 0): #ESPIA EN DIRECCION ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "b"
                        elif "R" in poss:
                            #Mover derecha
                            mazee[x][y] = " "
                            y = y + 1
                            mazee[x][y] = "b"
                        elif "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "b"
                    else: #fil = 0
                        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):

                            arrivedB = 1 
                            mazee[x][y] = "b"

                        else:
                            pasitos = []

                            if "D" in poss:
                                pasitos.append("D")
                            if "U" in poss:
                                pasitos.append("U")
                            
                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "D"):
                                    mazee[x][y] = " "
                                    x = x + 1
                                    mazee[x][y] = "b"

                                elif(eleccion == "U"):
                                    mazee[x][y] = " "
                                    x = x - 1
                                    mazee[x][y] = "b"

                                pasitos.clear()

                            elif(bool(pasitos)==False):

                                if "L" in poss:
                                    pasitos.append("L")
                                if "R" in poss:
                                    pasitos.append("R")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "L"):
                                        mazee[x][y] = " "
                                        y = y - 1
                                        mazee[x][y] = "b"

                                    elif(eleccion == "R"):
                                        mazee[x][y] = " "
                                        y = y + 1
                                        mazee[x][y] = "b"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    mazee[x][y]="b"
                                    pasitos.clear()

            else: #col = 0
                if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                            arrivedB = 1
                            mazee[x][y] = "b"
                else:
                    if(fil > 0): #ESPIA EN LA COLUMNA PERO ESTA ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "b"
                        else:
                            pasitos = []

                            if "L" in poss:
                                pasitos.append("L")
                            if "R" in poss:
                                pasitos.append("R")

                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "L"):
                                    mazee[x][y] = " "
                                    y = y - 1
                                    mazee[x][y] = "b"

                                elif(eleccion == "R"):
                                    mazee[x][y] = " "
                                    y = y + 1
                                    mazee[x][y] = "b"

                                pasitos.clear() 

                            elif(bool(pasitos)==False):

                                if "D" in poss:
                                    pasitos.append("D")
                                if "U" in poss:
                                    pasitos.append("U")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "D"):
                                        mazee[x][y] = " "
                                        x = x + 1
                                        mazee[x][y] = "b"

                                    elif(eleccion == "U"):
                                        mazee[x][y] = " "
                                        x = x - 1
                                        mazee[x][y] = "b"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    maze[x][y] = "b"
                                    pasitos.clear()

                    elif(fil < 0): #ESPIA EN LA COLUMNA PERO ESTA ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "b"
                        else:
                            pasitos = []

                            if "L" in poss:
                                pasitos.append("L")
                            if "R" in poss:
                                pasitos.append("R")

                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "L"):
                                    mazee[x][y] = " "
                                    y = y - 1
                                    mazee[x][y] = "b"

                                elif(eleccion == "R"):
                                    mazee[x][y] = " "
                                    y = y + 1
                                    mazee[x][y] = "b"

                                pasitos.clear() 

                            elif(bool(pasitos)==False):

                                if "D" in poss:
                                    pasitos.append("D")
                                if "U" in poss:
                                    pasitos.append("U")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "D"):
                                        mazee[x][y] = " "
                                        x = x + 1
                                        mazee[x][y] = "b"

                                    elif(eleccion == "U"):
                                        mazee[x][y] = " "
                                        x = x - 1
                                        mazee[x][y] = "b"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    maze[x][y] = "b"
                                    pasitos.clear()

            if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                arrivedB = 1
                mazee[x][y] = "b"
            else:
                arrivedB = 0

        elif(pelea==0 and alerta==0):
            #Vemos que caminos hay disponibles y los guardamos en una lista:
            if(mazee[x][y+1]==" "):
                pospaths2.append("R")

            if(mazee[x][y-1]==" "):
                pospaths2.append("L")

            if(mazee[x+1][y]==" "):
                pospaths2.append("D")

            if(mazee[x-1][y]==" "):
                pospaths2.append("U")

            #Elegimos aleatoriamente uno de esos posibles caminos
    
            step = random.choice(pospaths2)

            #Avanzamos de acuerdo con el paso elegido aleatoriamente

            if(step=="R"): #DERECHA
                mazee[x][y]=" "
                y = y+1
                mazee[x][y]="b"

            elif(step=="L"): #IZQUIERDA
                mazee[x][y]=" "
                y = y-1
                mazee[x][y]="b"  
        
            elif(step=="D"): #ABAJO
                mazee[x][y]=" "
                x = x+1
                mazee[x][y]="b"

            elif(step=="U"): #ARRIBA
                mazee[x][y]=" "
                x = x-1
                mazee[x][y]="b"

    #Guardia A al haber capturado al espia
    elif(estatusGB==1):

        #Buscamos antes que nada si la prision esta a un lado 
        if(mazee[x][y-1]=="P"): #Ver si esta a IZQUIERDA
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x+1][y]=="P"): #Ver si esta ABAJO
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x][y+1]=="P"): #Ver si esta DERECHA
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x-1][y]=="P"): #Ver si esta ARRIBA
            print("Guardia B ha escoltado al espia a la prision.")
            quit()
        else:
            if(mazee[x][y-1]==" "): #Busca IZQUIERDA
                mazee[x][y]=" "
                y = y - 1
                mazee[x][y]="B"
            elif(mazee[x+1][y]==" "): #Busca ABAJO
                mazee[x][y]=" "
                x = x + 1
                mazee[x][y]="B"
            elif(mazee[x][y+1]==" "): #Busca DERECHA
                mazee[x][y]=" "
                y = y + 1
                mazee[x][y]="B"
            elif(mazee[x-1][y]==" "): #Busca ARRIBA
                mazee[x][y]=" "
                x = x - 1
                mazee[x][y]="B"

    elif(estatusGB == 2): #MUERTO GUARDIA B
        pass             

def GuardiaC_Colab():
    encontrao=0
    global alerta
    global alertaX
    global alertaY
    global turnoC
    global arrivedC
    global arrivedA
    global arrivedB
    #Vamos a encontrar la posicion del guardia C:
    for f in range(len(mazee)):
        for c in mazee[f]:
            if (c=="c"):
                x = f
                y = mazee[f].index(c)
                estatusGC = 0
                encontrao = 1
                
            elif (c=="C"):
                x = f
                y = mazee[f].index(c)
                estatusGC = 1   
                encontrao = 1

    if(encontrao==0):
        estatusGC = 2

    #Guardia C sin haber capturado al Espia
    if(estatusGC==0):
        pelea = 0
        pospaths3 = []

        #Primero revisamos si tenemos al espia cerca

        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q"): #DERECHA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x
            alertaY = y + 1    
            spy = "R"

        elif(mazee[x][y-1]=="O" or mazee[x][y-1]=="Q"): #IZQUIERDA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x
            alertaY = y - 1 
            spy = "L"
        
        elif(mazee[x+1][y]=="O" or mazee[x+1][y]=="Q"): #ABAJO ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x + 1
            alertaY = y   
            spy = "D"

        elif(mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"): #ARRIBA ESTA ESPIA
            pelea = 1
            alerta = 1
            alertaX = x - 1
            alertaY = y
            spy = "U"

        if(pelea==1 and alerta==1):
            if(turnoC<=7):
                
                turnoC = turnoC + 1

                if(arrivedA==1 or arrivedB==1):
                    
                    if(spy=="R"):
                        mazee[x][y]=" "
                        y = y + 1
                        mazee[x][y]="C"

                    elif(spy=="L"):
                        mazee[x][y]=" "
                        y = y - 1
                        mazee[x][y]="C"

                    elif(spy=="D"):
                        mazee[x][y]=" "
                        x = x + 1
                        mazee[x][y]="C"

                    elif(spy=="U"):
                        mazee[x][y]=" "
                        x = x - 1
                        mazee[x][y]="C"
                elif(arrivedA==0 or arrivedB==0):
                    pass

            elif(turnoC>7):
                turnoC = 0
                alerta = 0 
                alertaX = 0
                alertaY = 0

        elif(pelea==0 and pelea==1):
            #PELEAAA VAMOSSS
            print("C va en camino a interceptar")
            poss = []

            fil = alertaX - x
            col = alertaY - y

            #BUSCAMOS LOS CAMINOS DISPONIBLES ALREDEDOR

            if(mazee[x][y+1]==" "): #DERECHA HAY CAMINO
                poss.append("R")

            if(mazee[x][y-1]==" "): #IZQUIERDA HAY CAMINO
                poss.append("L")
        
            if(mazee[x+1][y]==" "): #ABAJO HAY CAMINO
                poss.append("D")

            if(mazee[x-1][y]==" "): #ARRIBA HAY CAMINO
                poss.append("U")
            
            if(col > 0): #ESPIA ESTA EN LA DIRECCION DERECHA
                if "R" in poss:
                    #Mover derecha
                    mazee[x][y] = " "
                    y = y + 1
                    mazee[x][y] = "c"
                else:
                    if(fil > 0): #ESPIA EN LA DIRECCION ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "c"
                        elif "L" in poss:
                            #Mover izquierda
                            mazee[x][y] = " "
                            y = y - 1
                            mazee[x][y] = "c"
                        elif "U" in poss:
                            #Mover arriba 
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "c"
                    elif(fil < 0): #ESPIA EN LA DIRECCION ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "c"
                        elif "L" in poss:
                            #Mover izquierda
                            mazee[x][y] = " "
                            y = y - 1
                            mazee[x][y] = "c"
                        elif "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "c"
                    else: #fil = 0
                        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                            arrivedC = 1
                            mazee[x][y] = "c"
                        else:
                            pasitos = []

                            if "D" in poss:
                                pasitos.append("D")
                            if "U" in poss:
                                pasitos.append("U")
                            
                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "D"):
                                    mazee[x][y] = " "
                                    x = x + 1
                                    mazee[x][y] = "c"

                                elif(eleccion == "U"):
                                    mazee[x][y] = " "
                                    x = x - 1
                                    mazee[x][y] = "c"

                                pasitos.clear()

                            elif(bool(pasitos)==False):

                                if "L" in poss:
                                    pasitos.append("L")
                                if "R" in poss:
                                    pasitos.append("R")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "L"):
                                        mazee[x][y] = " "
                                        y = y - 1
                                        mazee[x][y] = "c"

                                    elif(eleccion == "R"):
                                        mazee[x][y] = " "
                                        y = y + 1
                                        mazee[x][y] = "c"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    mazee[x][y]="c"
                                    pasitos.clear()

            elif(col < 0): #ESPIA EN DIRECCION IZQUIERDA
                if "L" in poss:
                    #Mover izquierda
                    mazee[x][y] = " "
                    y = y - 1
                    mazee[x][y] = "c"
                else:
                    if(fil > 0): #ESPIA EN DIRECCION ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "c"
                        elif "R" in poss:
                            #Mover Derecha
                            mazee[x][y] = " "
                            y = y + 1
                            mazee[x][y] = "c"
                        elif "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "c"
                    elif(fil < 0): #ESPIA EN DIRECCION ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "c"
                        elif "R" in poss:
                            #Mover derecha
                            mazee[x][y] = " "
                            y = y + 1
                            mazee[x][y] = "c"
                        elif "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "c"
                    else: #fil = 0
                        if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):

                            arrivedC = 1 
                            mazee[x][y] = "c"

                        else:
                            pasitos = []

                            if "D" in poss:
                                pasitos.append("D")
                            if "U" in poss:
                                pasitos.append("U")
                            
                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "D"):
                                    mazee[x][y] = " "
                                    x = x + 1
                                    mazee[x][y] = "c"

                                elif(eleccion == "U"):
                                    mazee[x][y] = " "
                                    x = x - 1
                                    mazee[x][y] = "c"

                                pasitos.clear()

                            elif(bool(pasitos)==False):

                                if "L" in poss:
                                    pasitos.append("L")
                                if "R" in poss:
                                    pasitos.append("R")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "L"):
                                        mazee[x][y] = " "
                                        y = y - 1
                                        mazee[x][y] = "c"

                                    elif(eleccion == "R"):
                                        mazee[x][y] = " "
                                        y = y + 1
                                        mazee[x][y] = "c"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    mazee[x][y]="c"
                                    pasitos.clear()

            else: #col = 0
                if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                            arrivedC = 1
                            mazee[x][y] = "c"
                else:
                    if(fil > 0): #ESPIA EN LA COLUMNA PERO ESTA ABAJO
                        if "D" in poss:
                            #Mover abajo
                            mazee[x][y] = " "
                            x = x + 1
                            mazee[x][y] = "c"
                        else:
                            pasitos = []

                            if "L" in poss:
                                pasitos.append("L")
                            if "R" in poss:
                                pasitos.append("R")

                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "L"):
                                    mazee[x][y] = " "
                                    y = y - 1
                                    mazee[x][y] = "c"

                                elif(eleccion == "R"):
                                    mazee[x][y] = " "
                                    y = y + 1
                                    mazee[x][y] = "c"

                                pasitos.clear() 

                            elif(bool(pasitos)==False):

                                if "D" in poss:
                                    pasitos.append("D")
                                if "U" in poss:
                                    pasitos.append("U")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "D"):
                                        mazee[x][y] = " "
                                        x = x + 1
                                        mazee[x][y] = "c"

                                    elif(eleccion == "U"):
                                        mazee[x][y] = " "
                                        x = x - 1
                                        mazee[x][y] = "c"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    maze[x][y] = "c"
                                    pasitos.clear() 

                    elif(fil < 0): #ESPIA EN LA COLUMNA PERO ESTA ARRIBA
                        if "U" in poss:
                            #Mover arriba
                            mazee[x][y] = " "
                            x = x - 1
                            mazee[x][y] = "c"
                        else:
                            pasitos = []

                            if "L" in poss:
                                pasitos.append("L")
                            if "R" in poss:
                                pasitos.append("R")

                            if(bool(pasitos)==True):

                                eleccion = random.choice(pasitos)

                                if(eleccion == "L"):
                                    mazee[x][y] = " "
                                    y = y - 1
                                    mazee[x][y] = "c"

                                elif(eleccion == "R"):
                                    mazee[x][y] = " "
                                    y = y + 1
                                    mazee[x][y] = "c"

                                pasitos.clear() 

                            elif(bool(pasitos)==False):

                                if "D" in poss:
                                    pasitos.append("D")
                                if "U" in poss:
                                    pasitos.append("U")

                                if(bool(pasitos)==True):

                                    eleccion = random.choice(pasitos)

                                    if(eleccion == "D"):
                                        mazee[x][y] = " "
                                        x = x + 1
                                        mazee[x][y] = "c"

                                    elif(eleccion == "U"):
                                        mazee[x][y] = " "
                                        x = x - 1
                                        mazee[x][y] = "c"

                                    pasitos.clear()

                                elif(bool(pasitos)==False):

                                    maze[x][y] = "c"
                                    pasitos.clear()

            if(mazee[x][y+1]=="O" or mazee[x][y+1]=="Q" or mazee[x][y-1]=="O" or mazee[x][y-1]=="Q" or mazee[x+1][y]=="O" or mazee[x+1][y]=="Q" or mazee[x-1][y]=="O" or mazee[x-1][y]=="Q"):
                arrivedC = 1
                mazee[x][y] = "c"
            else:
                arrivedC = 0

        elif(pelea==0 and pelea==0):
            #Vemos que caminos hay disponibles y los guardamos en una lista:
            if(mazee[x][y+1]==" "):
                pospaths3.append("R")

            if(mazee[x][y-1]==" "):
                pospaths3.append("L")

            if(mazee[x+1][y]==" "):
                pospaths3.append("D")

            if(mazee[x-1][y]==" "):
                pospaths3.append("U")

            #Elegimos aleatoriamente uno de esos posibles caminos
    
            step = random.choice(pospaths3)

            #Avanzamos de acuerdo con el paso elegido aleatoriamente

            if(step=="R"): #DERECHA
                mazee[x][y]=" "
                y = y+1
                mazee[x][y]="c"

            elif(step=="L"): #IZQUIERDA
                mazee[x][y]=" "
                y = y-1
                mazee[x][y]="c"  
        
            elif(step=="D"): #ABAJO
                mazee[x][y]=" "
                x = x+1
                mazee[x][y]="c"

            elif(step=="U"): #ARRIBA
                mazee[x][y]=" "
                x = x-1
                mazee[x][y]="c"

    #Guardia C al haber capturado al espia
    elif(estatusGC==1):
        
        
        #Buscamos antes que nada si la prision esta a un lado 
        if(mazee[x][y-1]=="P"): #Ver si esta a IZQUIERDA
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x+1][y]=="P"): #Ver si esta ABAJO
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x][y+1]=="P"): #Ver si esta DERECHA
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        elif(mazee[x-1][y]=="P"): #Ver si esta ARRIBA
            print("Guardia C ha escoltado al espia a la prision.")
            quit()
        else:
            if(mazee[x][y-1]==" "): #Busca IZQUIERDA
                mazee[x][y]=" "
                y = y - 1
                mazee[x][y]="C"
            elif(mazee[x+1][y]==" "): #Busca ABAJO
                mazee[x][y]=" "
                x = x + 1
                mazee[x][y]="C"
            elif(mazee[x][y+1]==" "): #Busca DERECHA
                mazee[x][y]=" "
                y = y + 1
                mazee[x][y]="C"
            elif(mazee[x-1][y]==" "): #Busca ARRIBA
                mazee[x][y]=" "
                x = x - 1
                mazee[x][y]="C"
    elif(estatusGC==2):
        pass

#FUNCION PRINCIPAL

def miMain():
    while(True):
        print("             MENU PROYECTO FINAL              ")
        print(" ")
        print("-----------------Simbologia-------------------")
        print("X -> Tesoro")
        print("E -> Entrada")
        print("P -> Prision")
        print("O -> Espia            Q -> Espia con tesoro")
        print("a -> Guardia 1        A -> Guardia 1 con espia")
        print("b -> Guardia 2        B -> Guardia 2 con espia")
        print("c -> Guardia 3        C -> Guardia 3 con espia")
        print("# -> Obstaculos o paredes")
        print("----------------------------------------------")
        print("1. Modo Reactivo")
        print("2. Modo Colaborativo")
        print("3. Salir")
        print(" ")
        opt = int(input("Que modo desea ejecutar? "))

        if(opt==1):
            print("Modo Reactivo")
            while(True): 
                Espia()
                print(" ")
                mostrarMapaR()

                GuardiaA()
                print(" ")
                mostrarMapaR()

                GuardiaB()
                print(" ")
                mostrarMapaR()

                GuardiaC()
                print(" ")
                mostrarMapaR()

        elif(opt==2):
            print("Modo colaborativo")
            while(True): 
                Espia_Colab()
                print(" ")
                mostrarMapaC()

                GuardiaA_Colab()
                print(" ")
                mostrarMapaC()

                GuardiaB_Colab()
                print(" ")
                mostrarMapaC()

                GuardiaC_Colab()
                print(" ")
                mostrarMapaC()
        elif(opt==3):
            print("Hasta la proxima! ")
            break
        else:
            print("Opcion invalida")
    
#EJECUCION COMPLETA

miMain()


