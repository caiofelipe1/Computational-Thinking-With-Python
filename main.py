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

# EX 1 --------------------------------------------------------------------------------

'''while True:
    num = input('Dê uma nota de 0 a 10: ')
    if nota.isnumeric():
        print(type(num), num)
        num = int(num)
        print(type(num), num)
        if num > 0 and num < 10:
            break
        else:
            print("Você não digitou algo entre 0 e 10")
    else:
        print("Você não digitou um número")
'''

'''# EX 2 --------------------------------------------------------------------------------

nome = input('Digite seu nome: ')
while len(nome) < 3:
    nome = input('Nome deve ter no mínimo 3 caractéres: ')

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

sx = input("Diga f ou m: ")
while sx != 'f' and sx != 'm':
    sx = input("Diga f ou m: ")

sexo = input("Diga f ou m: ")
while not (sexo == 'f' or sexo == 'm'):
    sexo = input('Diga f ou m')

estadoC = input('Diga seu estado civil (s, c, v, d')
while not (estadoC == 's' or estadoC == 'c' or estadoC == 'v' or estadoC == 'd'):
    estadoC = input('Diga seu estado civil (s, c, v, d): ')
print(f"Seu nome é {nome}, sua idade é {idade}, seu salário é {salario}"
      f"você é {sexo} e seu estado civil é {estadoC}")
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

#a = 80
#b = 200
#anos = 0
#while a < b:
#    a = a + 0.03*a
#    a*= 1.03
#    b*= 1.015
#    print(anos)

'''

'''
#EX 4

soma = 0
qtd = 0
while qtd < 5:
    num = input(f'Diga o {qtd+1}° número: ')
    while not num.isnumeric():
        num = input(f'Diga o {qtd+1}° número: ')
    num = int(num)
    qtd += 1
    soma += num
media = soma/qtd
print(f"a soma é {soma} e a media é {media}")
'''

'''
#EX 5

a = input("Diga um numero: ")
while not a.isnumeric():
    a = input("Diga um numero: ")
a = int(a)


b = input("Diga outro numero: ")
while not b.isnumeric():
    b = input("Diga outro numero: ")
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a)
    a += 1
'''

'''
# EX 6

usuario = input('Diga seu usuário: ')
senha = input('Diga sua senha: ')
while usuario == senha:
    print('Não pode ser igual')
    usuario = input('Diga seu usuário: ')
    senha = input('Diga sua senha: ')
'''

'''
# EX 7

num = 1
while num <= 10:
    print(f'Tabuada do {num}')
    i = 1
    while i <= 10:
        print(f'{num}*{i} = {num+i}')
        i += 1
    num += 1
    print('--------')'''
'''
# EX 8 

a = 1
b = 1
print(a, end=' ')
print(b, end=' ')

qtd = 10
i = 0
while i < qtd:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    i += 1 
'''

# EX 9
'''
qtd = 0
pares = 0
impares = 0
while qtd < 10:
    num = input(f'Diga o {qtd+1}° número: ')
    if not num.isnumeric():
        num = input(f'Diga o {qtd+1}° número: ')
        continue
    num = int(num)
    if num % 2 == 0:
        pares += 1
    qtd += 1
impares = qtd - pares
print(impares)
'''

# EX 10
'''
num = input('Digite o número que deseja fatoriar: ')
while not num.isnumeric():
    num = input('Digite o número que deseja fatoriar: ')
num = int(num)
fatorial = num
fatorial_string = f"{num}! = {num}"
while num > 1:
    num -= 1
    fatorial *= num
    fatorial_string += f"*{num}"
fatorial_string += f" = {fatorial}"
print(fatorial_string)
'''

'''
# EX 11

# Verificando TODOS os números
i = 2
num = 97
while i < num:
    print(f"{num}%{i} = {num%i}")
    if num%i == 0:
        print(f"{num} não é primo")
        break
    elif i == num-1:
        print("é primo")
    i += 1

# Verificando apenas até a METADE dos números
i = 2
num = 97
while i < num/2:
    print(f"{num}%{i} = {num%i}")
    if num%i == 0:
        print(f"{num} não é primo")
    i += 1
if 1 >= num/2:
    print('É primo')

# Verificando apenas as RAÍZES dos números
i = 2
num = 97
while i < num**0.5
    print(f"{num}%{i} = {num%i}")
    if num%i == 0:
        print(f"{num} não é primo")
    i += 1
if 1 >= num**0.5:
    print('É primo')
'''
