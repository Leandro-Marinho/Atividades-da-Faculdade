# PAGUE O ALUGUEL

'''
Ramón está com problemas para pagar o aluguel de sua casa, o pior é que o total da dívida é enorme, pois ele tem muitos pagamentos em atraso, atualmente
são mais de 14 meses atrasados!
A casa de Ramón está em uma vila em que todas as casas pertencem a uma única pessoa, o Senhor Édgar. Para quitar a dívida, Ramón fez um acordo com
Senhor Édgar, prometendo pagar mensalmente um valor que será descontado da dívida total. Ele se comprometeu a sempre pagar o mesmo valor até que a
dívida seja encerrada. Porém, se o valor que ele puder pagar superar o valor da dívida, ele pagará exatamente o que deve e não mais, evidentemente.
Como Ramón não tem um controle adequado para atualizar o valor da dívida de acordo com os valores pagos, pediu sua ajuda para construir
um programa que receba como entrada o valor da dívida e o valor que se comprometeu a pagar mensalmente, o programa deve exibir, mês a mês,
o valor da dívida antes e depois do pagamento.

*** Entrada ***

Dois números inteiros positivos, o primeiro representa o valor da dívida e o segundo o valor que Ramón poderá pagar mensalmente.

*** Saída ***

O número do pagamento, o valor restante da dívida antes do pagamento mensal e o valor restante da dívida após o pagamento mensal, conforme
o padrão exibido nos exemplos. A exibição deve continuar até que a dívida seja quitada.

'''

# RESOLUÇÃO:

divida = int(input())
pagamento_mensal = int(input())
contador = 0

while divida != 0:
    contador += 1

    if divida >= pagamento_mensal:
        antes = divida
        divida = divida - pagamento_mensal
        depois = divida
    else:
        antes = divida
        divida = divida - divida
        depois = divida

    print(f'pagamento: {contador}')
    print(f'antes = {antes}')
    print(f'depois = {depois}')
    print('-----')
