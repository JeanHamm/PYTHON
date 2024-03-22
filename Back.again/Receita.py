def custo_do_produto(valor_do_pote, peso_do_pote, peso_usado):
    retorno = (valor_do_pote*peso_usado) / peso_do_pote
    return retorno

print('-------------- Bem vindo a calculadora de preço --------------\n')

produto_n = input("Qual o nome do produto que quer calcular? ")

quantidade_ingredientes = int(input(f'\nQual a quantidade de ingredientes para fazer o {produto_n}? '))

tamanho_pote = {}
quantidade_usada = {}
valor_pote = {}
ingrediente_v = {}
ingrediente_n = {}
valor_total = 0

for i in range(quantidade_ingredientes):
    ingrediente_n[i] = input(f"\nQual o nome do {i + 1}° ingrediente? ") 
    tamanho_pote[i] = float(input(f"Qual o peso total do pote do {ingrediente_n[i]} em gramas? g"))
    valor_pote[i] = float(input(f"Qual é o peso que utiliza do {ingrediente_n[i]} em gramas? g"))
    quantidade_usada[i] = float(input(f"Qual é o valor do pote do {ingrediente_n[i]} em reais? R$"))
    ingrediente_v[i] = custo_do_produto(valor_pote[i], tamanho_pote[i], quantidade_usada[i])

quantidade_gerada = float(input("Quantas porções rende a receita: "))
print('\n-------------- CUSTO DE CADA INGREDIENTE --------------\n')
for i in range(quantidade_ingredientes):
    print(f'{ingrediente_n[i]} custa R${ingrediente_v[i]}')
    valor_total = valor_total + ingrediente_v[i]

print('\n-------------- VALOR TOTAL --------------\n')

print(f'\nO valor total do {produto_n} é de R${valor_total}\n')
print(f'\nO valor de cada porção do {produto_n} é de R${(valor_total / quantidade_gerada)}\n')



