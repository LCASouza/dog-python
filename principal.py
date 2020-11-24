from dog import Dog

nome = list()

quantidade = int(input('Quantos dogs voce tem? '))

for i in range (1, quantidade+1):
    nome.append(str(input(f'Insira o nome do dog {i}: ')))

favorito = str(input('Qual o nome do dog que irá participar: ')) #Não precisa ser um dog do dono
dogao = Dog(favorito)

print('')
print(f'Que legal temos o {favorito} aqui!')
print(f'Voce podera escolher algumas acoes pro dog realizar: brincar, morder, dormir ou !brincar, !morder, !dormir.')
print(f'Para sair digite: parar')
print(f'Basta digitar a acao como descrito acima!')
print('')

while(True):

    action = input('Qual acao ele deve realizar? ')
    
    while(action != 'brincar' and action != 'morder' and action != 'dormir' and action != '!brincar' and
    action != '!morder' and action != '!dormir' and action != 'parar'):
        action = input('Esta nao e uma acao valida, por favor insira uma acao valida: ')

    if action == 'parar':
        print('Ate mais!')
        break

    if action == 'brincar':
        print('')
        dogao.verificarAcaoAtual(action)
        dogao.brincar()
        print('')

    elif action == 'morder':
        print('')
        dogao.verificarAcaoAtual(action)
        dogao.morder()
        print('')

    elif action == 'dormir':
        print('')
        dogao.verificarAcaoAtual(action)
        dogao.dormir()
        print('')

    elif action == '!brincar':
        print('')
        dogao.verificarAcaoAtual(action)
        dogao.stopBrincar()
        print('')

    elif action == '!morder':
        print('')
        dogao.verificarAcaoAtual(action)
        dogao.stopMorder()
        print('')

    elif action == '!dormir':
        print('')
        dogao.verificarAcaoAtual(action)
        dogao.stopDormir()
        print('')

print(f'Nome dos seus dogs:', end = ' ')

for i in range (0, quantidade):
    print (f'{nome[i]}', end = ' ')

print ('')