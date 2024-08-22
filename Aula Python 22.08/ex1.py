numeros = [4,3,2,5,1,6,9,8,7,10]
def soma_elementos(numeros):
    soma = 0
    for num in numeros:
        soma += num
    return soma

def soma_elementos_indice(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma

vinhos = ['Sangue de Boi', 'Pérgola', 'Chapinha', 'Cantinho do Vale']

def forca_opcao(msg,lista_opcoes):
    opcao = input(msg)
    possibilidades = '\n'.join(lista_opcoes)
    possibilidades = '\n' +possibilidades+'\n->'
    msg += possibilidades
    opcao = input(f"{msg}")
    while opcao not in lista_opcoes:
        print(f'Opção Inválida! Somente essas: {possibilidades}')
        opcao = input(msg)
    return opcao

vinhos = ['Sangue de Bói', 'Pérgola','Chapinha', 'Cantinho do Vale']
escolha_vinho = forca_opcao(vinhos, "Qual vinho vc escolhe?\n->")
print(f'vocÊ escolheu o {escolha_vinho}')