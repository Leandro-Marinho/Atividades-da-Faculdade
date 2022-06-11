# DOAÇÃO

'''
Ao perceber que um de seus amigos estava com dificuldades financeiras, Victória, uma garota muito inteligente, decidiu ajuda-lo com uma "vaquinha digital",
em que todos poderiam doar quanto pudesse para ajudar seu amigo.
Para isso, Victória criou uma criptomoeda, a Vic Coin, em que cada unidade equivale a R$ 2,50. Assim, as pessoas que doarão primeiro compram a criptomoeda e,
em seguida, depositam uma parte delas para doação. A parte que não foi doada fica guardada em uma carteira digital e poderá ser usada no futuro para
outras doações.
Victória está ocupada implementando o que é necessário para o funcionamento do ambiente de doação, por isso pediu para que você a ajudasse com uma das
partes essenciais: a contabilização de doações e a conversão para reais.
Seu papel é criar um programa que receba como entrada diversas doações feitas em Vic Coin e, ao final, exiba o total em Vic Coin (VC$) e o total
convertido para reais (R$).

*** Entrada ***

Diversos números reais, um por linha, que representam os valores das doações feitas em Vic Coin. A entrada será finalizada com o valor
de doação -1.0 que não deverá ser contabilizado na soma das doações.

*** Saída ***

Duas linhas. A primeira linha será um valor real com duas casas decimais indicando o total doado em Vic Coin (VC$); a segunda linha será
um valor real com duas casas decimais que indica o total doado em reais (R$).

'''

# RESOLUÇÃO:

vic_coin = 2.5
doacao = 0
soma_doacoes = 0
soma_vic_coin = 0

while doacao != -1:
    doacao = float(input())

    if doacao != -1:
        soma_doacoes += doacao
        soma_vic_coin = soma_doacoes * vic_coin

print(f'VC$ {soma_doacoes:.2f}')
print(f'R$ {soma_vic_coin:.2f}')
