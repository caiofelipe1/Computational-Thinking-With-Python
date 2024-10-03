import matplotlib.pyplot as plt
from random import choice
import pandas as pd
'''
def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

lado = 1000
linhas = lado
colunas = lado
raio = lado //2
raio_menor = 0.99*raio
circulo = cria_matriz(linhas, colunas)
for i in range(linhas):
    for j in range(colunas):
#    if (i - raio) **2 + (j - raio) **2 <= raio **2 and (i - raio) **2 + (j - raio) ** 2 >= raio_menor **2:
        if abs((i-raio) ** 2 + (j - raio) **2 - raio**2) <= 5*raio:
            circulo[i][j] = 1
plt.imshow(circulo, 'gray')
plt.colorbar()
plt.show()'''

# DICIONARIO

'''
dic = {"oi" : ['Olá','iae', 'opa','aoba'],
       'tchau' : ['xao','tmj','noiss','abç','marchaa féé!!']
}
while True:
    resp = input("Diga oi ou tchau:\n->")
    print(choice(dic[resp]))
'''

'''
dic = {
    'chave' : 'valor',
    'chave2' : None
}
print(dic['chave'])
dic['nova chave'] = ['novo valor']
print(dic)
dic['chave'] = 1
print(dic)
'''
'''
dic = {
    'chave' : 1
}
lista = dic['chave'] = dic['chave']
dic['chave'].append(3)
print(dic['chave'][1])
dic['chave'] = 4
print(dic)
'''
'''
numeros = {'pares' : []}
numeros['impar'] = []

for i in range(20):
    if i%2 == 0:
        numeros['pares'].append(i)
    else:
        numeros['impar'].append(i)
print(pd.DataFrame(numeros))

'''

'''frase = 'Arerereeeee! hahahaaha yes sir'
frase = frase.replace('hahahaaha', 'yesssss')
print(frase)
'''
#telefone sem replace
'''dic = {"um" : '1',
       "dois" : '2',
       "três" : '3',
       "quatro" : '4',
       "cinco" : '5',
       "seis" : '6',
       "sete" : '7',
       "oito" : '8',
       "nove" : '9',
       "zero" : '0'
}
tel = ''
for i in range(9):
    num = input(f'diga o {i+1}° numero\n ->')
    tel += dic[num]
print(tel)
'''


#telefone com replace
'''
numeros = {"um" : '1',
       "dois" : '2',
       "três" : '3',
       "quatro" : '4',
       "cinco" : '5',
       "seis" : '6',
       "sete" : '7',
       "oito" : '8',
       "nove" : '9',
       "zero" : '0'
}

tel = input("Diga seu numero: ")
for key in numeros.keys():
    print(f'{key} -> {numeros[key]}')
    tel = tel.replace(key,numeros[key])
    print(tel)
    tel = tel.replace(' ',' ')
'''

poligono = {
    "1" : "não é poligono",
    "2" : "não é poligono",
    "3" : "triângulo",
    "4" : "quadrado",
    "5" : "pentagono",
    "6" : "hexagono",
    "7" : "heptagono",
    "8" : "octogono",
    "9" : "eneagono"
}


escolhido = input("Digite quantos lados tem a forma:\n->")
print(poligono[escolhido])