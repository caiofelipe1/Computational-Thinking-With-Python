#AULA PYTHON 04/11/2024
'''qtd = 0
par = 0
while qtd < 5:
    num = int(input('Diga um número:' ))
    if num % 2 == 0:
        par += 1
    qtd += 1
print(f'A quantidade de pares é {par} e impares {qtd - par}')
'''

'''
senha = '1234'
password = input('Diga sua senha: ')
tentativas = 1
while senha != password and tentativas < 3:
    print(f'Vc é hacker? Só mais {3-tentativas} tentativas')
    password = input('diga sua senha: ')
    tentativas += 1
if senha == password:
    print('Acesso liberado')
else:
    print('Sai hacker!')
'''

'''i = 0
soma = 0
while i < 100:
    i += 1
    print(i)
    #para somar ao quadrado é so colocar - soma += i*i
    soma += i
    print(f"i vale {i} e soma vale {soma}")
'''

'''# com AND 
idoso = input('Você é idoso? (sim/não): ')
while idoso != 'sim' and idoso != 'não':
    idoso = input('Você é idoso? (sim/não): ')

if idoso == 'sim':
    print('top')
else:
    print('kid')
'''


'''# com OR
idoso = input('Você é idoso? (sim/não): ')
while not (idoso == 'sim' or idoso == 'não'):
    idoso = input('Você é idoso? (sim/não): ')

if idoso == 'sim':
    print('top')
else:
    print('kid')
'''

'''# idoso com while True
while True:
    idoso = input('Você é idoso? (sim/não): ')
    if idoso == 'sim' or idoso == 'não':
        break'''


'''num = input('Diga um número: ')
while not num.isnumeric():
    num = input('Diga um número: ')
num = int(num)
print(type(num),num)
'''

# PARA LER QUANTIDADE DE CARACTERES - print(len('danilo'))
# while len(nome)<3

# LISTA EXERCÍCIOS LOOP

'''# EX 1

while True:
    nota = input('Dê uma nota de 0 a 10: ')
    if nota.isnumeric():
        if int(nota) > 0 and int(nota) < 10:
            nota = int(nota)
        break
'''

#EX 2

'''nome = input('Digite seu nome: ')
while len(nome) < 3:
    nome = input('Digite seu nome inteiro: ')

while True:
    idade = input('Diga sua idade: ')
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        else:
            print('seu numero nao esta entre 0 e 150')
    else:
        print('Não é um numero')

while True:
    salario = input('Digite seu salario: ')
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            break

sexo = input("Diga f ou m: ")
while not (sexo == 'f' or sexo == 'm'):
    sexo = input('Diga f ou m')

estadoC = input ('Diga seu estado civil (s, c, v, d')
while not (estadoC == 's' or estadoC == 'c' or estadoC == 'v' or estadoC == 'd'):
    estadoC = input('Diga seu estado civil (s, c, v, d): ')
'''

'''#EX 3
paisA = 80000
paisB = 200000
contador = 0
while paisA <= paisB:
    contador += 1
    paisA *= 1.03
    paisB *= 1.015
print(f"A cidade A passará a B em {contador} anos ")
'''

#EX 4
