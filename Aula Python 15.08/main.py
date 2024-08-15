"""vinho1 = "haha1"
vinho2 = "haha2"
vinho3 = "haha3"

opcao = input('Qual a sua escolha de vinho?\n->')

while not (opcao == vinho1 and opcao == vinho2 and opcao == vinho3):
    print("Opção inválida!")
    opcao = input('Qual a sua escolha de vinho?\n->')
    

'''num = input("Diga um número: ")
while not num.isnumeric():
    print("Deve ser um número: ")
    num = input("Diga um número: ")
num = int(num)
'''
"""
'''
while True:
    num = input('diga um numero: ')
    if num.isnumeric():
        num = int(num)
        if num > 10 and num < 20:
            break
        print('Não ta entre 10 e 20')
        continue
    print('Não é um numero!')
    
'''

#Lista Loop - Exs 2,7 e 12
'''
#2)
nome = input('Diga o seu nome: ')
while not len(nome) > 3:
    print('Digite seu nome inteiro!')
    nome = input('Diga o seu nome: ')
    continue
print(nome)

while True:
    idade = input('diga sua idade: ')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        print('Diga sua idade corretamente! ')
        continue
    print('Não é um número! ')

while True:
    salario = input('diga seu salário: ')
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            break
        print('Deve ser maior que 0')
        continue
    print('Não é um numero!')

sexo = input('Diga seu sexo (f - feminino e m - masculino):\n->')
while not sexo == 'f' or sexo == 'm':
    print('Por favor digite f ou m ')
    sexo = input('Diga seu sexo (f - feminino e m - masculino):\n->')
    continue

estadoCivil = input('Diga seu estado civil "s", "c", "v" ou "d": ')
while not estadoCivil == 's' or estadoCivil == 'c' or estadoCivil == 'v' or estadoCivil == 'd':
    print('Digite corretamente: ')
    estadoCivil = input('Diga seu estado civil "s", "c", "v" ou "d": ')
    continue

print(f' Nome: {nome}')
print(f' Idade: {idade}')
print(f' Salario: {salario}')
print(f' Sexo: {sexo}')
print(f' Estado Civil: {estadoCivil}')
'''

'''
#7)
num = 1
mult = 1
while num <= 10:
    print(f'Tabuada do {num}')
    mult = 1
    while mult <= 10:
        print(f'{mult}*{num} = {num*mult}')
        mult += 1
    mult = 0
    num += 1
'''

'''
#12)
i = 0
soma = 0
while i < 7:
    nota = input(f'diga a {i+1}ª nota: ')
    while not nota.isnumeric():
        print('Não é um número!')
        nota = input(f'Diga a {i+1}ª nota: ')
    nota = int(nota)
    soma += nota
    i += 1 
media= soma/1 
print(media)
'''

'''nome = 'caio'
vogais = 0
for char in nome:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vogais += 1 
    print(char)
print(vogais)'''


'''lista = [1, True, 2.5, 'fefse',[]]
for elem in lista:
    print(elem)
for i in range(len(lista)):
    print(f'lista[{i}] = {lista[i]}')
lista = []
lista.append('danilo')
print(lista)
lista.append('andre')
print(lista)
'''

'''
media = 0
for i in range(7):
    nota = input(f'Diga a {i+1}ª nota: ')
    if not nota.isnumeric():
        print(f'{nota} não é um número! ')
        continue
    # Não ficar alterando variavel do loop!
        nota = input(f'Diga a {i+1}ª nota: ')
    media += int(nota) 
media/=7
print(media)
'''

'''
lista = [4, 3, 26, 89, 4, 2, 56, 8, 23, 3, 5]
for elem in lista:
    elem = 1 
    print(elem)
print(lista)
for i in range(len(lista)):
    lista[i] = 1
print(lista)'''

'''
lista = []
for i in range(10): 
    num = input (f'Digite o {i+1}° número: ')
    while not num.isnumeric():
        num = input (f'Digite o {i+1}° número: ')
    lista.append(int(num))
    pares = 0
    for num in lista:
        if num%2 == 0:
            pares += 1
    pares = 0
    for i in range(len(lista)):
        num = lista[i]
        if num%2 == 0:
            pares += 1
'''


def media(lista_numeros):
    soma = 0
    for num in lista:
        soma += num
    media = soma/len(lista)
    return media
lista = [32,54,6,3,4,2,423,3]
media_lista = media(lista)
print(media_lista)
media_lista = media ([3,2,54,6,5,54,6,3,5])
print(media_lista)