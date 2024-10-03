'''
def expo(x, y):
    return(x ** y)

print(expo(2, 5))
print(expo(3, 2))
print(expo(4, 4))
print(expo(9, 3))
'''

'''
def voto(nome, idadex):
    if idade < 16:
        return(False)
    else:
        return(True)
    

while True:
    eleitor = input("Nome: ")
    idade = int(input("idade: "))

    if not idade:
        break

    teste = voto(eleitor, idade)
#   teste1, teste2 = voto(eleitor, idade)

#   if teste2:
    if teste [1]:
        print("Pode votar")
    else:
        print("Não pode votar")
print("FIm")

'''

'''
# Exercicio 

def maior(x):

    z = x[0]

    for i in x:
        if z < i:
            z = i

    return(z)

y = (-2, -5, -7, -9)
print(maior(y))

t = (2, 5, 7, 9)
print(maior(y))

'''

def cpf(x):
    digito1 = 0
    digito2 = 0
    pos = 11
    for i in x:
        if pos > 2:
            digito1 += int(i) * (pos - 1)
            digito2 += int(i) * pos
            pos -= 1
    digito1 = digito1 % 11
    digito1 = 11 - digito1
    if digito1 > 9:
        digito1 = 0

    digito2 += digito1 * 2
    digito2 = digito2 % 11
    digito2 = 11 - digito2
    if digito2 > 9:
        digito2 = 0

    return(digito1, digito2)