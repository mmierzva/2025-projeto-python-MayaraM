'''
Jogo de Perguntas e Respostas
2025.06.30
Mayara M.
'''
# Objetivo: Criar um jogo de perguntas e respostas sobre bandas.
from modules import mostraCabecalho, mostraMenu, getValue

# VARIÁVEIS:
resp = 0
perguntas = 0
msg = ''

# LISTAS: 
msgsCab = ['JOGO DE PERGUNTAS E RESPOSTAS - BANDAS', 'Desenvolvido por Mayara']
msgsSelect = ['ESCOLHA O LEVEL:', '[1] Fácil', '[2] Médio', '[3] Difícil', 'Escolha o nível de dificuldade: ']

# Mostrar cabeçalho ao iniciar o programa:
mostraCabecalho(msgsCab)

# CHAMA A FUNÇÃO PRINCIPAL:
def playGame():
    global acertos, resp, perguntas, msg

    PlayAgain = 'sim' # Se o jogador quisr jogar novamente, o menu inicial será mostrado.
    while PlayAgain.lower() == 'sim':
        mostraMenu(msgsSelect) 


    # Mostrar msg
        msg = '-> Digite o level'
        resp = getValue(msg) # Pega o valor inserido pelo usuário

        # Verificar se valor é valido:
        opcoes = ['1', '2', '3']
        while resp not in opcoes:
            resp = getValue('Valor inválido, tente novamente') # Caso o valor não estiver válido, pede para o usuário digitar novamente.

        # Verificar opções e mostrar prguntas de acordo com a opção:
        if resp == '1':
            perguntas = [
                {
                    'pergunta': '1. Como é o nome do icônico álbum lançado pelos Beatles, onde aparece os quatro integrantes atravessando uma faixa de pedestre?',
                    'opcoes': ['1. Rubber Soul', '2. Abbey Road', '3. Let It Be'],
                    'resposta': '2'
                },
                {
                    'pergunta': '2. Qual banda é conhecida pelo álbum "The Wall"?',
                    'opcoes': ['1. Queen', '2. Led Zeppelin', '3. Pink Floyd'],
                    'resposta': '3'
                },
                { 'pergunta': '3. Qual banda lançou o álbum "Back in Black"?',
                    'opcoes': ['1. AC/DC', '2. Guns N\' Roses', '3. Metallica'],
                    'resposta': '1'
                }
            ]

            for p in perguntas: 
                print(p['pergunta'])
                for opcao in p['opcoes']:
                    print(opcao) # Imprime as perguntas de acordo com a entrada do usuário.
                RespUser = input('Digite a resposta correta: ')
                OpcVal = [opcao.split('.')[0] for opcao in p['opcoes']]
                while RespUser not in OpcVal:
                    RespUser = input('Opção inválida, tente novamente: ') # Caso resposta for != das opções disponíveis, pedir para o usuário digitar novamente até inserir uma resposta válida.
                if RespUser == p['resposta']: # Se a resposta do usuário for igual á resposta correta, imprime mensagem.
                    print()
                    print('Parabéns, você acertou!')
                else:
                    print(f'Resposta incorreta. A resposta era: {p["resposta"]}.') # Se a resposta do usuário for diferente da correta, imprime a mensagem certa e continua o jogo.
                print()  # Linha em branco para separar as perguntas

        elif resp == '2':
            perguntas = [
                {
                    'pergunta': '1. Quem lançou o hit "Starman" em 1972?',
                    'opcoes': ['1. Elton John', '2. David Bowie', '3. The Rolling Stones'],
                    'resposta': '2'
                },
                {
                    'pergunta': '2. Que álbum do Pearl Jam é conhecido por seus hits "Even Flow", "Black" e "Jeremy?"',
                    'opcoes': ['1. Nevermind', '2. Pearl Jam', '3. Ten'],
                    'resposta': '3'
                },
                { 'pergunta': '3. Qual banda lançou o álbum "Hotel California"?',
                    'opcoes': ['1. Eagles', '2. Van Halen', '3. The Doors'],
                    'resposta': '1'
                },
                { 'pergunta': '4. Qual é o nome da banda que é considerada uma das pioneiras do punk rock, conhecida por seu álbum de estreia com o mesmo nome?',
                    'opcoes': ['1. The Clash',  '2. The Ramones', '3. Misfits'],
                    'resposta': '2'
                }]

            for p in perguntas:
                print(p['pergunta'])
                for opcao in p['opcoes']:
                    print(opcao)
                RespUser = input('Digite a resposta correta: ')
                OpcVal= [opcao.split('.')[0] for opcao in p['opcoes']]
                while RespUser not in OpcVal:
                    RespUser = input('Opção inválida, tente novamente: ')
                if RespUser == p['resposta']:
                    print()
                    print('Parabéns, você acertou!')
                else:
                    print(f'Resposta incorreta. A resposta era: {p["resposta"]}.')
                print()  # Linha em branco para separar as perguntas

        elif resp == '3':
            perguntas = [
                {
                    'pergunta': '1. Qual dessas músicas do Pink Floyd NÃO faz parte do disco "The Dark Side of the Moon"?',
                    'opcoes': ['1. Money', '2. Confortably Numb', '3. Breathe (In The Air)'],
                    'resposta': '2'
                },
                {
                    'pergunta': '2. Como é conhecida a trilogia de discos lançados por David Bowie entre 1976 e 1979, que inclui "Low", "Heroes" e "Lodger"?',
                    'opcoes': ['1. The Early Years', '2. Heroes ', '3. Trilogia de Berlim'],
                    'resposta': '3'
                },
                { 'pergunta': '3. Após a saída de Ozzy Osbourne do Black Sabbath, seu primeiro álbum solo foi o "Blizzard of Ozz", qual era o guitarrista desse álbum?',
                    'opcoes': ['1. Randy Rhoads', '2. Zakk Wylde', '3. Tommy Iommi'],
                    'resposta': '1'
                },
                { 'pergunta': '4. Qual foi a primeira música dos Beatles a ter um vidoclipe produzido para promover um single?',
                    'opcoes': ['1. Help!',  '2. Penny Lane', '3. Strawberry Fields Forever'],
                    'resposta': '2'
                }]

            for p in perguntas:
                print(p['pergunta'])
                for opcao in p['opcoes']:
                    print(opcao)
                RespUser = input('Digite a resposta correta: ')
                OpcVal = [opcao.split('.')[0] for opcao in p['opcoes']]
                while RespUser not in OpcVal:
                    RespUser = input('Opção inválida, tente novamente: ')
                if RespUser == p['resposta']:
                    print()
                    print('Parabéns, você acertou!')
                else:
                    print(f'Resposta incorreta. A resposta era: {p["resposta"]}.')
                print()  # Linha em branco para separar as perguntas

        # Perguntar se o usuário deseja jogar novamente.
        PlayAgain = input('Deseja jogar novamente? (sim/não): ')
        if PlayAgain.lower() == 'não': # O lower é utilizado para se caso o usuário digitar não com letras maísculas ou min´pusculas, ele vai identificar da mesma forma escrita no código.
            print('Obrigado por jogar! Até a próxima!')
            break # Encerra o loop.
        
# Executa o jogo ao rodar o script
if __name__ == "__main__":
    playGame()