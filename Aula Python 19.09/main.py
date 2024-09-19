'''dic = {
    'chave' : 'valor'
}
print(dic['chave'])

dic['nova chave'] = 'novo valor'
print(dic)
dic['chave'] = 'outro valor'
print(dic)

saudacoes = {'oi': 'ola',
             'tchau': 'flw',
             'aoba': 'bao'}
resp = input('diga oi, tchau ou bao: \n ->')
print(saudacoes[resp])

frase = 'oi eu sou o caio, o caio é romantico'
frase = frase.replace('caio', 'Caio')
print(frase)

emojis = {
    ':)' : '😁',
    ':(' : '😔',
    ':o' : '😯',
    ':/' : '😕'
}
frase = ('Ontem eu tavo :(, hoje estoy happy :) e amanhã acho que '
         'estarei impressionadson :o, depois abaladorr :/')
for key in emojis.keys():
    frase = frase.replace(key,emojis[key])
print(frase)

'''

import pandas as pd
def forca_opcao(msg,conjunto_opcoes,msg_erro = 'Inválido!'):
    opcoes = '\n'.join(conjunto_opcoes)
    escolha = input(f'{msg}\n{opcoes}\n->')
    while not escolha in conjunto_opcoes:
        print(msg_erro)
        escolha = input(f'{msg}\n{opcoes}\n->')
    return escolha
def acha_index(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i

def forca_numero(msg,msg_erro = 'Inválido'):
    num = input(msg)
    while not num.isnumeric():
        print(msg_erro)
        num = input(msg)
    return int(num)
carros = {
    'modelo' : ['opala', 'marea', 'kombi', 'celtinha', 'uno','monza','corcel'],
    'potência(cv)' : [172,130,250,140,100,120,150],
    'consumo (km/l)' : [1,3,8,7,15,1.5,2],
    'cor' : ['laranja','verde','branca','preto','prata','preto','azul'],
    'ano' : ['1972','2004','1985','2014','2001','1980','1975'],
    'estoque' : [5,6,7,8,9,10,11],
    'preço' : [50,10,2.50,1000000,100,200,999999]
}

# print(pd.DataFrame(carros))

indices = {}
for i in range(len(carros['modelo'])):
    nome = carros['modelo'][i]
    indices[nome] = i
print(indices)
s_ou_n = ['sim', 'nao']
valor_total = 0
carrinho = {
    'Carros' : {},
    'Valor Total' : 0,
    'Endereço' : {
        'Rua' : '',
        'Cep' : '',
        'Número' : ''
    }
}
while True:
    escolha = forca_opcao('Qual carro voce quer ver?',carros['modelo'])
    index_escolha = indices[escolha]
    for key in carros.keys():
        print(key,carros[key][index_escolha])
    comprar = forca_opcao('VocÊ VAI COMPRARRR?', s_ou_n)
    if comprar == s_ou_n[0]:
        qtd = forca_numero(f'Quantos {escolha}? ')
        if carros['estoque'][index_escolha] >= qtd:
            carros['estoque'][index_escolha] -= qtd
            carrinho['Valor Total'] += qtd*carros['preço'][index_escolha]
            if escolha not in carrinho['Carros'].keys():
                carrinho['Carros']['escolha'] = qtd
            else:
                carrinho['Carros']['escolha'] += qtd
        else:
            print(f'Não há {qtd} de {escolha} no estoque. Voltaremos ao inicio.')
            continue

        encerrar = forca_opcao('Quer encerrar a compra?',s_ou_n)
        if encerrar == s_ou_n[0]:
            print('Tenho que montar o carrinho do usuario, calma.')
            break

    else:
        ver_mais = forca_opcao('quer ver outras opções?', s_ou_n)
        if ver_mais == [1]:
            break

