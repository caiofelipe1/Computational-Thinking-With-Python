#PEÇA PARA O USUARIO DIGITAR UMA CHAVE DO DICIONARIOS E UM INDICE, PRINT O ELEMENTO 
#CORRESPONDENTE A ESSE INDICE NA LISTA DA CHAVE 

'''
dic = {'chave1' : [1,2,3,4],
        'chave2' : [5,6,7,8]
    }
while True:
    try:
        chave = input(f'Diga uma chave {dic.keys()}:')
        i = int(input("Diga um indice: "))
        print(dic[chave][i])

    except IndexError:
        print(f"Esse índice não existe, somente: 0-{len}(dic['chave1])-1")
    except ValueError:
        print("Deve ser um número inteiro")
    except KeyError:
        print("Somente as chaves disponíveis")
'''

while True:
    try: 
        a = int(input("Diga um número: "))
        b = float(input("Diga outro número: "))
        print(a, b)
    except ValueError:
        print("Digitou errado troxao")
