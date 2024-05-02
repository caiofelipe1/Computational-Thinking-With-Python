'''
# for (loops em strings)
# for var in 'string'
 
for char in 'rafael':
    print(char)
'''
 
'''
# for (range do loop)
# range(10) -> range (0, 10, 1)
 
for i in range(10):
    print(i)
'''
 
'''
# for (range do loop)
# for var in range(inicio, final, passo)
 
for i in range(1, 10, 2):
    print(i)
'''
 
'''
# for (range 'vazio')
# range(10, 1, 2) -> conjunto vazio
 
for i in range(10, 1, -2):
    print(i)
'''
 
'''
# senha (3 tentativas)
 
senha_cadastrada = '1234'
 
for i in range(3):
    senha = input('Senha: ')
 
    if senha == senha_cadastrada:
        print('Acesso Liberado!!! \n')
        break
    print(f'Senha incorreta, voce tem {2-i} tentativas restantes!!! \n')
 
if senha != senha_cadastrada:
    print('Acesso negado!!! \n')
'''
 
'''
# Exercicio 01: Some todos os numeros de 1 a 100 (for).
 
soma = 0
 
for i in range(1, 101):
    soma += i
 
print(f'Soma = {soma}')
'''
 
'''
# Exercicio 02: Peça 10 numeros e conte a quantidade de pares e impare (for).
 
pares = 0
 
for i in range(1, 11):
    while True:
        num = input(f'Digite o {i}º numero: ')
 
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Voce deve digitar um valor numerico!!! \n')
 
    if num % 2 == 0:
        pares += 1
 
impares = i - pares
   
print(f'\n > Voce digitou {pares} numero(s) par(es), e {impares} numero(s) impar(es). \n')
'''
 
'''
# Exercicio 03: Peça 10 numeros e faça a soma e a media (for).
 
soma = 0
media = 0
 
for i in range(1, 11):
    while True:
        num = input(f'Digite o {i}º numero: ')
 
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Voce deve digitar um valor numerico!!! \n')
 
    soma += num
 
media = soma / i
 
print(f'\n > Soma = {soma} \n'
      f' > Media = {media} \n')
'''
 
'''
# Exercicio 04: Faça a tabuada de todos os numeros de 1 a 10 (for).
 
for num in range(1, 11):
    print(f'\n\n > Tabuada do {num} \n')
 
    for fator in range(1, 11):
        tabuada = num * fator
 
        print(f'{num} x {fator} = {tabuada}')
'''
 

'''
# Exercicio 05: Encontre a quantidade de vogais numa string que o usuario digitou (for).
 
vogais = 0
palavra = input('Diga uma palavra: ')
for char in palavra:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or \
        char == 'u':
        vogais += 1
print(f'Há {vogais} vogais e {len(palavra) - vogais} consoantes'
      f' na sua palavra')
'''

'''
# APRENDENDO LISTAS 
lista = [1,True,3.2,'caio',['dwdw',False]]

print(type(lista))
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
lista[4] = True
print(lista)

for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")


for elem in lista:
    print(elem,end = ' ')
    elem = 1
    print(elem)
print(lista)

for i in range(len(lista)):
    lista[i] = 1
print(lista)
'''

'''
# Lista professores testando se Danilo está na lista e onde esta
profs = ['Andre', 'Lucas Silva', 'Yan', 'Danilo', 'Allen', 'Celso']

for i in range(len(profs)):
    if profs[i] == 'Danilo':
        achou = True
        print(f'Indice: {i}\n'
              f'Posição: {i + 1}\n'
              f'Danilao arroz e feijao')
        break
if not achou:
    print('Nao ta na lista')
'''

'''
# Lista professores e materias 
profs = ['Andre', 'Lucas Silva', 'Yan', 'Danilo', 'Allen', 'Celso']
materias = ['Storytelling', 'Front-End', 'Edge', 'Python', 'Software Design', 'Soluving problems']
for i in range(len(profs)):
    print(f'O prof {profs[i]} dá {materias[i]}')
achou = False
if not achou:
    print('Nao ta na lista')
'''

profs1 = ['Patricia', 'Ana', 'Danilo', 'Thiago', 'Jones', 'Yan']
profs2 = ['Andre', 'Lucas Silva', 'Yan', 'Danilo', 'Allen', 'Celso']

for prof1 in profs1:
    for profs in profs:
        if profs == profs:
            print(f'O {profs1} dá aula nas duas turmas')
