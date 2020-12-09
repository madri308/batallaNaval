import pygame
import random

#Declaro los colores que se van a utilizar
negro = (0,0,0)
blanco = (255,255,255)
azul = (112, 159, 176)
gris = (125,120,120)
amarillo = (255,242,0)

#Medidas de los cuadrados
width=40
height=40
margin = 2

#Datos del juego
derrive = 0
meDerrivaron = 0
misBarcos = []
barcosOponentes = []


barcos = {"Portaviones":5,"Battleship":5,"Crucero de batalla":3,"Submarino":2,"Lancha":1}
diccionario = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F' : '6', 'G': '7', 'H':'8','I': '9', 'J':'10'}
def crearTablero():
    tablero = [["","1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]
    letras = list(diccionario.keys())
    for fila in range(10):
        filaNueva = []
        for columna in range(11):
            if columna == 0:
                filaNueva.append(letras[fila])
            else:
                filaNueva.append(letras[fila]+str(columna))
        tablero.append(filaNueva)
    return tablero

def pintarTableros(tableros,screen):
    font = pygame.font.Font('freesansbold.ttf', 28)
    for t in range(len(tableros)):
        tablero = tableros[t]
        for row in range(len(tablero)):  #por cada fila
            for column in range(len(tablero[row])):  #por cada columna
                texto = ""
                if column == 0 or row == 0:
                    color = blanco
                    texto = tablero[row][column] #Obtengo el texto de la celda
                elif tablero[row][column] == "T":
                    color = amarillo
                elif tablero[row][column] == "P":
                    color = gris
                else:
                    color = azul
                x = ((margin+width)*column+margin) + 464*t
                y = (margin+height)*row+margin
                pygame.draw.rect( screen , color , [x, y, width, height] )
                screen.blit(font.render(texto, True, negro), [x, y, width, height])
                pygame.display.update() #Acualizo la pantalla

def crearVentana(ancho,largo,titulo):
    size=[ancho,largo]
    screen=pygame.display.set_mode(size)
    screen.fill(negro) #Pinto la ventana de negro
    pygame.display.set_caption(titulo) #Titulo de la ventana

    return screen
def revisarTiro(x,y,tablero):
    tablero[x][y] = "T"

def jugar(miTablero,compuTablero,screen):
    font = pygame.font.Font('freesansbold.ttf', 28)
    text = font.render('Mi tablero                          Tablero oponente', True, blanco, negro)
    textRect = text.get_rect()
    textRect.center = (464, 480)
    screen.blit(text, textRect)
    turnoCompu = False
    cerrar=False #Variable para saber si debo terminar
    while cerrar==False: #Mientras no deba terminar
        pintarTableros([miTablero,compuTablero],screen)
        if not turnoCompu:
            for event in pygame.event.get(): #Obtengo cualquier cosa que se haga en la ventana 
                if event.type == pygame.QUIT:   #Si cierra la ventana
                    cerrar = True                 #Debo terminar el programa
                if event.type == pygame.MOUSEBUTTONDOWN:    #Si hice click
                    pos = pygame.mouse.get_pos()            #Obtengo la posicion donde hice click
                    column=pos[0] // (width+margin)         #Calculo la columna
                    row=pos[1] // (height+margin)           #Calculo la fila
                    if column > 10 and row < 11: 
                        column = column-11
                        print(compuTablero[row][column])
                        if column != 0 and row != 0:       
                            turnoCompu = True
                            revisarTiro(row,column,compuTablero)
        else:
            x = random.randint(1,10)
            y = random.randint(1,10)
            revisarTiro(x,y,miTablero)
            turnoCompu = False

def posicionarBarcos(screen,miTablero):
    ancho = screen.get_width()
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect((ancho//2)-108, 50, 140, 32)
    text = ''
    done = False
    barco = 0
    while not done:
        font = pygame.font.Font('freesansbold.ttf', 28)
        tipoBarco = font.render("Ingrese la ubicacion del "+list(barcos.keys())[barco], True, blanco, negro)
        textRect = tipoBarco.get_rect()
        textRect.center = (ancho//2, 14)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    misBarcos = text.split(",")
                    text = ''
                    for pos in misBarcos:
                        miTablero[int(diccionario[pos[0]])][int(pos[1])] = 'P'#list(barcos.keys())[barco][0]
                    if barco == 4:
                        done = True
                    else:
                        barco += 1
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill(negro)
        txt_surface = font.render(text, True, azul)
        input_box.w = max(200, txt_surface.get_width()+10)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, azul, input_box, 2)
        screen.blit(tipoBarco, textRect)
        pygame.display.flip()

def validar(lista,cantidad):
    valido = False
    if len(lista) == cantidad:
        for pos in lista:
            if pos[0] in diccionario.keys() and pos[1] in diccionario.values():
                valido = True
    return valido

def main():
    pygame.init()
    miTablero = crearTablero()
    compuTablero = crearTablero()
    
    screen = crearVentana(600,100,"Batalla Naval - Posicionando mis barcos")
    posicionarBarcos(screen,miTablero)
    screen = crearVentana(928,600,"Batalla Naval")
    jugar(miTablero,compuTablero,screen)

    pygame.quit()
main()
