def checa_numero(msg):
    num = input()
    while not num.isnumeric():
        num = input(msg)
    num = int(num)

checa_numero('Diga seu ano de nascimento: ')
checa_numero('Diga a quantidade de garrafas: ')
