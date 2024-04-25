print('Olá! Seja bem-vindo a Vinheria Agnello!\nInsira suas informações abaixo:\n')
while True:
    nome = input('Insira seu nome abaixo:\n')
    if len(nome) < 3:
        print("Tente novamente inserir seu nome utilizando no mínimo 3 letras!")
    else:
        break

while True:
    anoAtual = 2024
    ano_nascimento = input("Insira seu ano de nascimento:\n")
    if not ano_nascimento.isnumeric():
        print("Insira um ano de nascimento válido!")
    else:
        ano_nascimento = int(ano_nascimento)
        idade = anoAtual - ano_nascimento
        if idade < 18:
            print("Menores de idade, por lei, não podem consumir bebidas alcólicas!")
        else:
             break
        
chattelier = "1"
moonrise = "2"
cantinhodovale = "3"
mandrakesitaqua = "4"
escolhas = 0
valor = 0

endereco = input("Insira aqui o seu endereço:\n")

while True:
    print("Agora, escolha abaixo as suas opções de vinho de acordo com a numeração:\n1 - Chattelier (R$ 120,00)\n2 - Moonrise (R$ 75,00)\n3 - Cantinho do Vale (R$56,00)\n4 - Mandrakes Itaqua Wine (R$ 450,00)\nSe deseja encerrar seu pedido, pressione o dígito 5")
    opcao = input("Insira as opcoes desejadas: ")
    if opcao == "1":
        print("Voce selecionou o vinho Chattelier!")
        escolhas += 1
        valor += 120
        qtd = int(input("Insira a quantidade de garrafas desejadas: "))

    if opcao == "2":
        print("Voce selecionou o vinho Moonrise!")
        escolhas += 1
        valor += 75
        qtd = int(input("Insira a quantidade de garrafas desejadas: "))

    if opcao  == "3":
        print("Voce selecionou o Cantinho do Vale!")
        escolhas += 1
        valor += 56
        qtd = int(input("Insira a quantidade de garrafas desejadas: "))

    if opcao == "4":
        print("Voce selecionou o Mandrakes Itaqua Wine!")
        escolhas += 1
        valor += 450
        qtd = int(input("Insira a quantidade de garrafas desejadas: "))

    if opcao == "5":
        print("Tudo bem! Suas opções foram salvas e já foram enviadas para seu carrinho!")
        total = valor*qtd
        print(f"Voce escolheu o total de {escolhas} vinhos e o valor total de seu pedido foi: R${total},00 e será entregue no endereço {endereco}")
        break




