print('Olá! Seja bem-vindo a Vinheria Agnello!\n Responda algumas informações abaixo: ') 
while True:
    nome = input('Digite o seu nome: ')
    if len(nome) < 3:
        print('Tente novamente, seu nome deve ter mais de 3 caractéres: ')
    else:
        break


while True:
    anoAtual = 2024
    anoNasc = input('Digite o ano do seu nascimento: ')
    if not anoNasc.isnumeric():
        print ('Digite o ano corretamente: ')
    else:
        anoNasc = int(anoNasc)
        idade = 2024 - anoNasc
        if idade < 18:
            print('Você não pode consumir bebida alcóolica')
        else:
            break

endereco = input('Digite o seu endereço: ')

Vinho1 = 'Vinho A'
Vinho2 = 'Vinho B'
Vinho3 = 'Vinho C'
escolhas = 0
valor = 0

print(f'')

while True:
        vinho_escolhido = input('Digite o nome do vinho que deseja comprar: ')
        print('\n')

        if vinho_escolhido == Vinho1 or vinho_escolhido == Vinho2 or vinho_escolhido == Vinho3:
            break
        else:
            print('Digite uma opcao de vinho valida!!! \n')

