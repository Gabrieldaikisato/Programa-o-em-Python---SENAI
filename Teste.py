# 1 CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

# def comparar_numeros():
#   num1 = float(input('Digite um número:'))
#   num2 = float(input('Digite um número:'))
    
#   if num1 > num2:
#         print (num1, 'é maior que', num2)
#   elif num1 < num2:
#         print (num1, 'é menor que', num2)
#   else:
#         print (num1, 'é igual ao', num2)
        
# comparar_numeros()


# 2 CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.

# def soma():
#     n1 = float(input('Digite um número para multiplicar:'))
#     n2 = float(input('Digite um número para multiplicar:'))
#     n3 = float(input('Digite um número para multiplicar:'))
#     soma = n1*n2*n3
#     print (soma)
# soma()

# 3 CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.

# def n_elevado():
#     base = float(input('Digite a base:'))
#     expoente = float(input('Digite o expoente:'))
#     soma = base**expoente
#     print (soma)
# n_elevado()

# 4 CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.

# def idade(idade):
#     if idade >= 18:
#         print ('Parabéns. Você é obrigado a se alistar e a votar!')
#     else:
#         print ('Você ainda é menor de idade.')
# idade_usu = int(input('Quantos anos você tem?'))
# idade(idade_usu)

# 5 DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.

# def idade(idade):
#     print('Vamos descobrir sua idade!')
#     idade_usu = int(input('Digite sua idade:'))
#     print ('Você tem', idade_usu, 'anos')
# idade(idade)

# 6 DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1998.

# def brasil():
#     resposta = input('O Brasil ganhou a copa de 98?')
#     if resposta == 'sim' or resposta == 's':
#         print ('Brasil foi o campeão!')
#     else:
#         print ('Brasil não foi o campeão!')
# brasil()
    
# 7 DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.

def mostrar_menu():
    print('Seja bem-vindo ao restaurante!')
    print('Escolha o seu prato:')
    print('1. Salada')
    print('2. Macarronada')
    print('3. Sanduíche')
    print('4. Sorvete')
    print('5. Sair')

def pedidos():
    pedidos_list = []  
    while True:
        mostrar_menu()
        escolha = input('DIGITE O NÚMERO DO SEU PRATO (1-5): ')

        if escolha == int:
            escolha = int(escolha)
            if escolha == 1:
                pedidos_list.append('Salada')
                print('Você escolheu Salada.')
            elif escolha == 2:
                pedidos_list.append('Macarronada')
                print('Você escolheu Macarronada.')
            elif escolha == 3:
                pedidos_list.append('Sanduíche')
                print('Você escolheu Sanduíche.')
            elif escolha == 4:
                pedidos_list.append('Sorvete')
                print('Você escolheu Sorvete.')
            elif escolha == 5:
                print('Saindo...')
                break  
            else:
                print('Opção inválida. Por favor, escolha de 1-5.')
        else:
            print('Por favor, insira um número válido.')

        continuar = input("Você deseja continuar fazendo pedidos? (sim/não): ").strip().lower()
        if continuar == 'não' or continuar == 'nao':
          print("Saindo...")
          break 

    if pedidos_list:
        print("\nResumo do seu pedido:")
        for pedido in pedidos_list:
            print(f"- {pedido}")
    else:
        print("Você não fez nenhum pedido.")

pedidos()
