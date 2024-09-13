import random

def jogoLegal():
    jogada = 5
    vitoria = 0
    while jogada != 0:
        print('\033[0;040m==========JOGO DA VELHA==========')
        jogada = int(input('\033[0;040m1 - Pedra\n2 - Papel\n3 - Tesoura\n'))
        
        if jogada > 3 or jogada < 0:
            print('\033[0;040mEscolha algo certo aff...')
            return vitoria
        
        match jogada:
            case 0:
                print('\033[0;040mTchau!')
                return vitoria
            case 1:
                jogadaMaquina = 2
            case 2:
                jogadaMaquina = 3
            case 3:
                jogadaMaquina = 1
        
        if ((jogada == 1 and jogadaMaquina == 3) or (jogada == 2 and jogadaMaquina == 1) or (jogada == 3 and jogadaMaquina == 2)): #Jogador ganha (Nunca vai acontecer nesse modo 😈)
            print('\033[0;032m Você ganhou!\n\n')
            vitoria += 1
        
        elif ((jogada == 1 and jogadaMaquina == 2) or (jogada == 2 and jogadaMaquina == 3) or (jogada == 3 and jogadaMaquina == 1)): #Jogador perde (Como sempre 😈)
            print('\033[0;031mMáquina venceu!\n\n')
        else:
            print('\033[0;033mEmpate\n\n') #Só pra ter né, vai q
    

def jogoJusto():
    jogada = 5
    vitoria = 0
    while jogada != 0:
        print('\033[0;040m==========JOGO DA VELHA==========')
        jogada = int(input('\033[0;040m1 - Pedra\n2 - Papel\n3 - Tesoura\n'))
        if jogada == 0:
            print('Tchau!')
            return vitoria
        if jogada > 3 or jogada < 0:
            print('\033[0;040mEscolha algo certo aff...')
            return vitoria
        
        jogadaMaquina = random.randint(1, 3)

        if ((jogada == 1 and jogadaMaquina == 3) or (jogada == 2 and jogadaMaquina == 1) or (jogada == 3 and jogadaMaquina == 2)): #Jogador ganha
            print('\033[0;032m Você ganhou!\n\n')
            vitoria += 1
        
        elif ((jogada == 1 and jogadaMaquina == 2) or (jogada == 2 and jogadaMaquina == 3) or (jogada == 3 and jogadaMaquina == 1)): #Jogador perde
            print('\033[0;031mMáquina venceu!\n\n')
        
        else:
            print('\033[0;033mEmpate\n\n')


escolha = int(input('\033[0;040mQual jogo você quer jogar?\n1 - Normal\n2 - Hard\n'))

if escolha == 1:
    res = jogoJusto()
elif escolha == 2:
    res = jogoLegal()
else:
    print('\033[0;040mEscolha algo certo aff...')
    
print(f'\033[0;040mVocê ganhou {res} vezes')