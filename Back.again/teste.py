def custo_do_produto(valor_do_pote, peso_do_pote, peso_usado):
    retorno = (valor_do_pote*peso_usado) / peso_do_pote
    return retorno


print(custo_do_produto(100, 100, 10))



