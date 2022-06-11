# COMPRANDO COM DESCONTO

'''
Maria, além de comerciante, é também ema excelente negociante! Por isso, sempre consegue descontos em suas compras. Ao visitar uma loja, Maria recebe
a seguinte proposta de um vendedor: “Se comprar minha mercadoria será concedido um desconto fixo de 10% e mais 1% a cada unidade comprada”. Infelizmente,
Maria está cansada de tanto trabalhar e não quer fazer os cálculos sozinha para descobrir qual será o valor da compra antes e depois do desconto, por isso
pediu sua ajuda.
Você criará um programa que receberá como entrada um número real, indicando o preço da mercadoria comprada por Maria, e um número inteiro, indicando a
quantidade de mercadoria comprada, e exibirá o valor da compra antes do desconto e o valor final, já com o desconto aplicado.
Observação: Para todos os efeitos, assuma que essa loja nunca vende mais do que 40 unidades de uma mesma mercadoria para a mesma pessoa. Repare que não é
necessário verificar, basta assumir que isso é verdade.

*** Entrada ***

Um número real positivo na primeira linha, indicando o preço da mercadoria, e um número inteiro positivo na segunda linha, indicando a quantidade comprada
da mercadoria.

*** Saída ***

Na primeira linha deve ser impresso um valor real com duas casas decimais, indicando o preço da compra sem o desconto e, na segunda linha, o preço final
com o desconto aplicado, também com duas casas decimais.

'''

# RESOLUÇÃO:

preco_da_mercadoria = float(input()) 
quantidade_comparada_da_mercadoria = int(input()) 

preco_da_compra_sem_desconto = preco_da_mercadoria * quantidade_comparada_da_mercadoria 
desconto_de_dez_por_cento_fixo = 0.1 
desconto_de_um_por_cento_por_item = quantidade_comparada_da_mercadoria * 0.01
total_descontos = preco_da_compra_sem_desconto * (desconto_de_dez_por_cento_fixo + desconto_de_um_por_cento_por_item) 
preco_da_compra_com_desconto = preco_da_compra_sem_desconto - total_descontos

print(f'{preco_da_compra_sem_desconto:.2f}')
print(f'{preco_da_compra_com_desconto:.2f}')
