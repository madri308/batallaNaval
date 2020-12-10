import pygame
import random

#Declaro los colores que se van a utilizar
negro = (0,0,0)
blanco = (255,255,255)
azul = (112, 159, 176)
gris = (125,120,120)
amarillo = (255,242,0)
rojo = (255,0,0)

#Medidas de los cuadrados
width=40
height=40
margin = 2

#Datos del juego
misBarcos = {}
barcosOponentes = {}
indicadores = ["P","B","C","S","L"]
barcos = {"Portaviones":5,"Battleship":4,"Crucero de batalla":3,"Submarino":2,"Lancha":1}
letrasNumeros = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F' : '6', 'G': '7', 'H':'8','I': '9', 'J':'10'}

#Crea una matrix que se utilizara como tablero
def crearTablero():
    tablero = [["","1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]
    letras = list(letrasNumeros.keys())
    for fila in range(10):
        filaNueva = []
        for columna in range(11):
            if columna == 0:
                filaNueva.append(letras[fila])
            else:
                filaNueva.append(letras[fila]+str(columna))
        tablero.append(filaNueva)
    return tablero

#Muestra los tableros en una ventana y los actualiza
def pintarTableros(tableros,screen):
    font = pygame.font.Font('freesansbold.ttf', 28)
    miTablero = True
    for t in range(len(tableros)):
        tablero = tableros[t]
        for row in range(len(tablero)):
            for column in range(len(tablero[row])): 
                texto = ""
                if column == 0 or row == 0:
                    color = blanco
                    texto = tablero[row][column] 
                elif str(tablero[row][column])[0] == "N":
                    color = amarillo
                elif tablero[row][column] in indicadores and miTablero:
                    color = gris
                    texto = tablero[row][column] 
                elif str(tablero[row][column])[0] == "X":
                    color = rojo
                    texto = tablero[row][column][1] 
                else:
                    color = azul
                x = ((margin+width)*column+margin) + 464*t
                y = (margin+height)*row+margin
                pygame.draw.rect( screen , color , [x, y, width, height] )
                screen.blit(font.render(texto, True, negro), [x, y, width, height])
                pygame.display.update()
        miTablero = False

#Crea ventanas
def crearVentana(ancho,largo,titulo):
    size=[ancho,largo]
    screen=pygame.display.set_mode(size)
    screen.fill(negro) 
    pygame.display.set_caption(titulo) 
    return screen

#Evalua los diccionarios para ver si ya alguien gano
def revisarGanador():
    compu = True
    jugador = True
    for key in barcosOponentes.keys():
        barcoEnPie = barcosOponentes[key]
        if barcoEnPie:
            jugador = False
            break
    for key in misBarcos.keys():
        barcoEnPie = misBarcos[key]
        if barcoEnPie:
            compu = False
            break
    if jugador:
        return "Tu"
    if compu:
        return "PC"
    else:
        return "N"

#Revisa si el tiro que se hizo acerto o no
def revisarTiro(x,y,tablero,barcosActuales):
    if tablero[x][y] in indicadores: #Acerto
        key_list = list(letrasNumeros.keys()) 
        val_list = list(letrasNumeros.values())
        barcosActuales[str(key_list[val_list.index(str(x))])+str(y)] = False
        tablero[x][y] = "X"+tablero[x][y]
        print("Acerto\n")
    else:                           #No acerto
        tablero[x][y] = "N"+tablero[x][y]
        print("Fallo\n")

#Logica del juego
def jugar(miTablero,compuTablero,screen):
    
    font = pygame.font.Font('freesansbold.ttf', 28)
    ganador = "N"
    titulo = font.render('Mi tablero                          Tablero oponente', True, blanco, negro)
    tituloRect = titulo.get_rect()
    tituloRect.center = (464, 480)
    screen.blit(titulo, tituloRect)

    turnoCompu = random.randint(0,1)
    if turnoCompu:
        print("***Inicia la PC ***\n")
    else:
        print("***Inicias tu ***\n")

    cerrar=False 
    while cerrar==False: 
        pintarTableros([miTablero,compuTablero],screen)
        if not turnoCompu:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:  
                    cerrar = True                 
                if event.type == pygame.MOUSEBUTTONDOWN:    
                    pos = pygame.mouse.get_pos()            
                    column=pos[0] // (width+margin)         
                    row=pos[1] // (height+margin)           
                    if column > 10 and row < 11: 
                        column = column-11
                        if column != 0 and row != 0 and compuTablero[row][column][0] != "N" and compuTablero[row][column][0] != "X":       
                            turnoCompu = True
                            pygame.display.set_caption("Batalla Naval")
                            print("Atacaste "+compuTablero[row][column])
                            revisarTiro(row,column,compuTablero,barcosOponentes)
                            ganador = revisarGanador()
                            if ganador != "N":
                                print(ganador)
                                cerrar = True
                        else:
                            pygame.display.set_caption("No puedes tirar en esta zona")
        else:
            celda = ["N"]
            while celda[0] == "N" or celda[0] == "X": #VALIDACION de que no tire en una casilla que ya tiro antes
                x = random.randint(1,10)
                y = random.randint(1,10)
                celda = miTablero[x][y]
            print("PC ataca "+miTablero[x][y])
            revisarTiro(x,y,miTablero,misBarcos)
            ganador = revisarGanador()
            if ganador != "N":
                print(ganador)
                cerrar = True
            turnoCompu = False
    return ganador

def posicionarBarcosCompu(compuTablero):
    file = random.randint(1,4)
    f = open("Tablero"+str(file)+".txt", "r")
    texto = f.read()
    barcosSeparados  = texto.split("\n")
    for barco in range(len(barcosSeparados)):
        indicadorSeparado = barcosSeparados[barco].split(" ")
        nuevoBarco = indicadorSeparado[1].split(",")
        if validar(nuevoBarco,list(barcos.values())[barco]):
            for pos in nuevoBarco:
                barcosOponentes[pos] = True
                compuTablero[int(letrasNumeros[pos[0]])][int(pos[1])] = indicadores[barco]
        else:
            pygame.display.set_caption("Archivo de ubicacion incorrecto")
            break

#Pide las ubicaciones de los barcos 
def posicionarBarcos(screen,miTablero):
    ancho = screen.get_width()
    font = pygame.font.Font(None, 32)
    entryBox = pygame.Rect((ancho//2)-108, 50, 140, 32)
    text = ''
    done = False
    barco = 0
    salir = False
    while not done:
        font = pygame.font.Font('freesansbold.ttf', 28)
        tipoBarco = font.render("Ingrese la ubicacion del "+list(barcos.keys())[barco], True, blanco, negro)
        textRect = tipoBarco.get_rect()
        textRect.center = (ancho//2, 14)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:                    
                    nuevoBarco = text.split(",")
                    text = ''
                    if validar(nuevoBarco,list(barcos.values())[barco]):
                        for pos in nuevoBarco:
                            misBarcos[pos] = True
                            miTablero[int(letrasNumeros[pos[0]])][int(pos[1])] = indicadores[barco]
                        barco += 1
                    if barco == 5:
                        done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill(negro)
        txt_surface = font.render(text, True, azul)
        entryBox.w = max(200, txt_surface.get_width()+10)
        screen.blit(txt_surface, (entryBox.x+5, entryBox.y+5))
        pygame.draw.rect(screen, azul, entryBox, 2)
        screen.blit(tipoBarco, textRect)
        pygame.display.flip()
    return salir
    
#Valida las ubicaciones
def validar(lista,cantidad):
    valido = False
    filaAnterior = -1
    columnaAnterior = -1
    if len(lista) == int(cantidad):
        for pos in lista:
            if pos not in misBarcos.keys():
                if pos[0] in letrasNumeros.keys() and pos[1] in letrasNumeros.values():
                    if int(cantidad) != 1:
                        if filaAnterior != -1:
                            filaActual = int(letrasNumeros[pos[0]])
                            columnaActual = int(pos[1])
                            if (filaAnterior+1 == filaActual and columnaAnterior == columnaActual) or (columnaAnterior+1 == columnaActual and filaAnterior == filaActual):
                                valido = True
                                pygame.display.set_caption("Batalla Naval - Posicionando mis barcos")
                            else:
                                pygame.display.set_caption("Las celdas deben ir seguidas")
                                valido = False
                                # break
                        filaAnterior = int(letrasNumeros[pos[0]])
                        columnaAnterior = int(pos[1])
                    else:
                        valido = True
                        pygame.display.set_caption("Batalla Naval - Posicionando mis barcos")
                else:
                    pygame.display.set_caption("Datos erroneas")
            else:
                pygame.display.set_caption("Ya existe un barco en esa posicion")
    else:
        pygame.display.set_caption("Cantidad de datos incorrectos, deben ser "+str(cantidad))
    return valido
    
def volverJugar(screen,ganador):
    width = screen.get_width() 
    height = screen.get_height() 

    font = pygame.font.Font('freesansbold.ttf', 28)
    titulo = font.render('Ganador: '+ganador, True, blanco, negro)
    tituloRect = titulo.get_rect()
    tituloRect.center = (width//2, height//3)
    screen.blit(titulo, tituloRect) 

    smallfont = pygame.font.SysFont('Corbel',35) 
    quitarText = smallfont.render('Salir' , True , blanco) 
    jugarText = smallfont.render('Jugar' , True , blanco) 
    cerrar = False
    jugar = False
    while not cerrar: 
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                cerrar = True
                jugar = False
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                mouse = pygame.mouse.get_pos()
                if width/4 <= mouse[0] <= width/4+70 and height/2 <= mouse[1] <= height/2+40: 
                    cerrar = True 
                    jugar = False
                if width/2 <= mouse[0] <= width/2+80 and height/2 <= mouse[1] <= height/2+40: 
                    cerrar = True
                    jugar = True

        pygame.draw.rect(screen,gris,[width/4,height/2,70,40]) 
        screen.blit(quitarText , (width/4,height/2)) 

        pygame.draw.rect(screen,gris,[width/2,height/2,80,40]) 
        screen.blit(jugarText , (width/2,height/2)) 

        pygame.display.update() 
    return jugar
#Funcion que maneja todo
def main():
    pygame.init()

    iniciar = True
    while iniciar:
        misBarcos.clear()
        barcosOponentes.clear()

        ganador = "Nadie"
        miTablero = crearTablero()
        compuTablero = crearTablero()

        screen = crearVentana(600,100,"Batalla Naval - Posicionando mis barcos")
        posicionarBarcosCompu(compuTablero)
        salir = posicionarBarcos(screen,miTablero)
        if not salir:
            screen = crearVentana(928,500,"Batalla Naval")
            ganador = jugar(miTablero,compuTablero,screen)

        screen = crearVentana(400,200,"Ganador: "+ganador)
        iniciar = volverJugar(screen,ganador)

    pygame.quit()

main()

