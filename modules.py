'''
Arquivo de funções utilizadas
2025.06.25
Mayara Mierzva
'''

# OBJETIVO: Criar um arquivo de funções que serão utilizadas nos projetos.

# BIBILIOTECAS:
from random import randint

# CONSTANTES:
TAM = int(50) # Tamanho da Tela
MAR = int(2) # Margem
CAR = '#' # CARACTERE utilizado para desenhar a linha
# VARIÁVEIS:


# LISTAS:

# FUNÇÕES:
def limpaTela():
    print('\n'*TAM) # (\n mostra linhas em branco)

# Função para desenhar uma linha de #:
def mostraLine():
    print(f'{CAR}'*TAM)

# Função para Mostrar uma msg Centralizada:
def msgCenter(msg):
    print(f'{CAR} {msg:^{TAM-MAR-MAR}} {CAR}')

# Função para mostrar uma msg à esquerda:
def msgLeft(msg):
    print(f'{CAR} {msg:<{TAM-MAR-MAR}} {CAR}')

# Função para mostrar cabeçalho:
def mostraCabecalho(MSGS):
    mostraLine()
    for msg in MSGS:
        msgCenter(msg)
    mostraLine() 

# Função para mostrar Menu;
def mostraMenu(MSGS):
    mostraLine()
    for msg in MSGS:
        msgLeft(msg)
    mostraLine()
    
# Função para sortear um número:
def sortNum(limite):
    key = randint(1, limite)
    return key

# Função para validar as entradas:
def validaValue(resp, opcoes):
    if resp in opcoes:
        return True
    else:
            MSGS = [f'{resp} não é uma opção válida!', 
                    f'Escolha entre {opcoes}']
            mostraMenu(MSGS)
            return False
        
# Função para obter a entrada do usuário:
def getValue(msg):
    resp = input(f'{CAR}{msg}:').strip()
    return resp

# Função para mostrar uma dica:
def mostraDica(resp, key):
    if resp > key:
        mostraCabecalho(['Tente um número menor!'])
    else:
        mostraCabecalho(['Tente um número maior!'])

# Função para perguntar se o jogador deseja jogar novamente:
def playAgain():
    opcoes = ['1', '0']
    mostraCabecalho(['Deseja jogar novamente?', '[1] Sim', '[0] Não'])
    resp = getValue('Escolha uma opção')
    return resp == '1'