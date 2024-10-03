from time import time
import matplotlib.pyplot as plt

'''[[], [], []] --> 3 linhas e 0 colunas
   [[1,2],[3,4],[5,6]] --> 3 linhas e 2 colunas (quantidade de elementos dentro de uma linha)'''

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz
'''plt.imshow(matriz, 'BrBG_r') }
plt.colorbar()                  } --> cores 
plt.show()                      }
'''

# Ex 3 e 4
'''def diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return


def contra_diagonal_ruim(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
    return
matriz = cria_matriz(5,5)
contra_diagonal_ruim(matriz)
mostra_matriz(matriz)

def contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
    return
matriz = cria_matriz(5,5)
contra_diagonal(matriz)
mostra_matriz(matriz)'''
'''
Ex)5
def abaixo_diagonal(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return
matriz = cria_matriz(10,10)
abaixo_diagonal(matriz)
mostra_matriz(matriz)

def acima_diagonal(matriz):
    for j in range(len(matriz)):
        for i in range(j):
            matriz[i][j] = 1
    return
matriz = cria_matriz(10,10)
acima_diagonal(matriz)
mostra_matriz(matriz)
'''

'''
matriz = cria_matriz(1000,1000)
t1 = time()
contra_diagonal_ruim(matriz)
t2 = time()
print(t2-t1)    
t1 = time()
contra_diagonal(matriz)
t2 = time()
print(t2-t1)
'''
'''3blue1brown'''

'''
#Ex 6)
def transposta_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return
matriz = cria_matriz(5,5)
transposta_matriz(matriz)
mostra_matriz(matriz)'''

#Ex 7) XADREZ:
'''
# jeito MERDAA
xadrez = cria_matriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2 == 0:
            if j%2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
        else:
            if j%2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
mostra_matriz(xadrez)
plt.imshow(xadrez)
plt.show()'''

# jeito FODAA
xadrez = cria_matriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[i])):
        if (i+j)%2 == 0:
            xadrez[i][j] = 1
mostra_matriz(xadrez)
plt.imshow(xadrez)
plt.show()

#matriz de vinhos (quadriculados de vinhos na parede)
# i + j tem que ser numero primo de fibonati pra poder por um vinho naquele lugar