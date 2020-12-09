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

def crearTablero():
    letras = ["A","B","C","D","E","F","G","H","I","J"]
    tablero = [["","1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]
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
                else:
                    color = azul
                x = ((margin+width)*column+margin) + 464*t
                y = (margin+height)*row+margin
                pygame.draw.rect( screen , color , [x, y, width, height] )
                screen.blit(font.render(texto, True, negro), [x, y, width, height])
                pygame.display.update() #Acualizo la pantalla

def crearVentana(ancho,largo):
    size=[ancho,largo]
    screen=pygame.display.set_mode(size)
    screen.fill(negro) #Pinto la ventana de negro
    pygame.display.set_caption("Color Boxes") #Titulo de la ventana

    return screen
def revisarTiro(x,y,tablero):
    tablero[x][y] = "T"

def main():
    pygame.init()
    screen = crearVentana(928,600)
    
    font = pygame.font.Font('freesansbold.ttf', 28)
    text = font.render('Mi tablero                          Tablero oponente', True, blanco, negro)
    textRect = text.get_rect()
    textRect.center = (464, 480)
    screen.blit(text, textRect)

    miTablero = crearTablero()
    compuTablero = crearTablero()
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
    pygame.quit()
main()
