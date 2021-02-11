import time 
import terminedia as TM

FPS = 0.3 # Afeta a velocidade da mudanca de quadros

# Comandos e constantes
UP = 'w'
DOWN = 's'
LEFT = 'a'
RIGHT = 'd'
SELECT = 'l'
COLOR = "\033[1;36m" # Ciano
BOLD  = "\033[;1m" # Bold
RESETCOLOR = "\033[0;0m"

def tabuleiro():
    print('\n\n')
    for i in range(2):
        print('     |     |     ')
        
        print('  ' + posicoes[i][0] + '  |  ' + posicoes[i][1] + '  |  ' + posicoes[i][2] + '  ')

        
        print('_____|_____|_____')
    

    print('     |     |     ')
    print('  ' + posicoes[2][0] + '  |  ' + posicoes[2][1] + '  |  ' + posicoes[2][2] + '  ')
    print('     |     |     ')
    
def controle(key, cursorX, cursorY, posicoes):
    if key == DOWN:
        if cursorY < 2 and posicoes[cursorY+1][cursorX] == ' ':
            cursorY += 1 
        
        elif cursorY == 2 and posicoes[0][cursorX] == ' ': # 'Teleportar' pela parede
            cursorY = 0

    elif key == UP:
        if cursorY > 0 and posicoes[cursorY-1][cursorX] == ' ':
            cursorY -= 1
        elif cursorY == 0 and posicoes[2][cursorX] == ' ':
            cursorY = 2

    elif key == LEFT:
        if cursorX > 0 and posicoes[cursorY][cursorX-1] == ' ':
            cursorX -= 1
        
        elif cursorX == 0 and posicoes[cursorY][2] == ' ':
            cursorX = 2

    elif key == RIGHT:
        if cursorX < 2 and posicoes[cursorY][cursorX+1] == ' ':
            cursorX += 1 
    
        elif cursorX == 2 and posicoes[cursorY][0] == ' ':
            cursorX = 0
            
    return cursorX, cursorY

def jogada(cursorX, cursorY, rodada):
    if rodada%2 == 0:
        posicoes[cursorY][cursorX] = 'O'
    else:
        posicoes[cursorY][cursorX] = 'X'

    rodada = checaVitoria(rodada)

    if (rodada > 0): # Ainda ha jogo
        cursorY, cursorX = encontraCasaVazia()

    return cursorX, cursorY, rodada

def encontraCasaVazia():
    for i in range(3):
        for j in range(3):
            if (posicoes[j][i] == ' '):
                return j, i
        
def checaVitoria(rodada):
    if (posicoes[0][0] == posicoes[1][1] == posicoes[2][2] != ' '): # Checa diagonal principal
        vencedor = posicoes[0][0]
        posicoes[0][0], posicoes[1][1], posicoes[2][2] = colorize(vencedor)
        vitoria(vencedor)
        return -1
    
    elif(posicoes[1][1] == posicoes[0][2] == posicoes[2][0] != ' '): # Checa diagonal secundaria
        vencedor = posicoes[1][1]
        posicoes[1][1], posicoes[0][2], posicoes[2][0] = colorize(vencedor)
        vitoria(vencedor)
        return -1

    else:
        for i in range(3): # Checa vitoria nas horizontais e verticais
            if (posicoes[i][0] == posicoes[i][1] == posicoes[i][2] != ' '):
                vencedor = posicoes[i][0]
                posicoes[i][0], posicoes[i][1], posicoes[i][2] = colorize(vencedor)
                vitoria(vencedor)
                return -1

            if (posicoes[0][i] == posicoes[1][i] == posicoes[2][i] != ' '):  
                vencedor = posicoes[0][i]
                posicoes[0][i], posicoes[1][i], posicoes[2][i] = colorize(vencedor)
                vitoria(vencedor)
                return -1
    if(rodada == 9): # Empate
        vitoria('empate')
        return 0
    
    else:
        rodada += 1 # Se nao houve vitoria, acrescenta-se uma rodada
        return rodada

def colorize(vencedor):
        posicao1 = posicao2 = posicao3 = COLOR + vencedor + RESETCOLOR
        return posicao1, posicao2, posicao3

def vitoria(vencedor):
        if (vencedor == 'empate'):
            print('\n\n Empate.')
        else:
            print('\n\n' + COLOR + vencedor + RESETCOLOR + ' ganhou!')



posicoes = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
cursorX = 0
cursorY = 0
rodada = 1 

while (rodada > 0):
    posicoes[cursorY][cursorX] = '▮'
    tabuleiro()
    time.sleep(FPS)
    posicoes[cursorY][cursorX] = ' '
    tabuleiro()
    time.sleep(FPS)

    with TM.keyboard():
        key = TM.inkey()

        if (key == SELECT):
            cursorX, cursorY, rodada = jogada(cursorX, cursorY, rodada)        
        else: 
            cursorX, cursorY = controle(key, cursorX, cursorY, posicoes)

tabuleiro()