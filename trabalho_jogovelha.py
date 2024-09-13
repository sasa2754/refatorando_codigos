def mostra_velha():
    global tab
    print("\n\n")
    print(" 0     1     2 \n\n")
    print("   |   |   \n")
    print(f"  {tab[0][0]} | {tab[0][1]}  | {tab[0][2]} \n")
    print("___|___|___\n")
    print("   |   |   \n")
    print(f"  {tab[1][0]} | {tab[1][1]}  | {tab[1][2]} \n")
    print("___|___|___\n")
    print("   |   |   \n")
    print(f"  {tab[2][0]} | {tab[2][1]}  | {tab[2][2]} \n")
    print("   |   |   \n\n\n")

def zerarMatriz():
    global tab
    l = 0
    c = 0
    for l in range(3):
        for c in range(3):
            tab[l][c] = 0



def jogadorX(nomeJogadorX):
    global tab
    linha = 0
    coluna = 0
    x = 0
    check = 0
    while x == 0:
        linha = int(input(f'{nomeJogadorX}, informe a linha escolhida: '))
        coluna = int(input(f'{nomeJogadorX}, informe a coluna escolhida: '))
        
        x = validador(linha, coluna)
        
    tab[linha][coluna] = 'X'
    
    mostra_velha()
    
    check = vencedor()
    
    if(check == 1):
        print(f'{nomeJogadorX} venceu o jogo!')
        return 1
    else:
        return 0
    
    
    
def jogadorO(nomeJogadorO):
    global tab
    linha = 0
    coluna = 0
    x = 0
    check = 0
    while x == 0:
        linha = int(input(f'{nomeJogadorO}, informe a linha escolhida: '))
        coluna = int(input(f'{nomeJogadorO}, informe a coluna escolhida: '))
        
        x = validador(linha, coluna)
        
    tab[linha][coluna] = 'O'
    
    mostra_velha()
    
    check = vencedor()
    
    if(check == 1):
        print(f'{nomeJogadorO} venceu o jogo!')
        return 1
    else:
        return 0
    

def validador(linha, coluna):
    global tab
    if (tab[linha][coluna] == 'X' or tab[linha][coluna] == 'O'):
        print('Lugar ocupado.')
        return 0
    
    elif(linha > 2 or coluna > 2 or linha < 0 or coluna < 0):
        print('Valor incorreto!')
        return 0
    
    else:
        return 1
    

def vencedor():
    global tab
    if (tab[0][0] == tab[0][1] and tab[0][1] == tab[0][2] and  tab[0][2] != 0 or 
		tab[1][0] == tab[1][1] and tab[1][1] == tab[1][2] and  tab[1][2] != 0 or  
		tab[2][0] == tab[2][1] and tab[2][1] == tab[2][2] and  tab[2][2] != 0 or
		tab[0][0] == tab[1][0] and tab[1][0] == tab[2][0] and  tab[2][0] != 0 or
		tab[0][1] == tab[1][1] and tab[1][1] == tab[2][1] and  tab[2][1] != 0 or
		tab[0][2] == tab[1][2] and tab[1][2] == tab[2][2] and  tab[2][2] != 0 or
		tab[0][0] == tab[1][1] and tab[1][1] == tab[2][2] and  tab[2][2] != 0 or
		tab[0][2] == tab[1][1] and tab[1][1] == tab[2][0] and  tab[2][0] != 0):
        
        return 1
    
    else:
        return 0
    

nomeX = input('Informe o nome do jogador 1 (X): ')
nomeO = input('Informe o nome do jogador 2 (O): ')

tab = [['', '', ''], ['', '', ''], ['', '', '']]

mostra_velha()     

for i in range(5):
    check = jogadorX(nomeX)
    
    if (i == 4 or check == 1):
        break
    
    check = jogadorO(nomeO)
    
    if (check == 1):
        break
    
if (check == 0):
    print('O jogo empatou!')