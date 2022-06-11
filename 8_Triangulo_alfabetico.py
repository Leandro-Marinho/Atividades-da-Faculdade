# TRIÂNGULO ALFABÉTICO

'''
O alfabeto latino é composto por letras, começando em 'A' e encerrando em 'Z'. São vinte e seis caracteres, se desconsiderarmos as
acentuações e as diferenças entre letras maiúsculas e minúsculas.
Harry, um garoto muito estudioso, percebeu que é possível inclusive desenhar usando letras. Em um dos desenhos, Harry escreve na primeira
linha e na primeira coluna de uma folha quadriculada o primeiro caractere do alfabeto. Na segunda linha escreve duas vezes, ocupando as duas
primeiras colunas. Na terceira linha escreve três vezes o terceiro caractere, ocupando as três primeiras colunas e assim por diante. Harry
percebeu que dessa forma consegue formar um triângulo alfabético, semelhante ao visto na Figura 1, onde a primeira linha contém apenas
um 'A' e a sétima contém sete 'G'.
Como Harry precisa estudar para realizar uma prova de programação, pediu para você ajudá-lo a automatizar os desenhos de "triângulo alfabético",
criando um programa que receba como entrada um número inteiro N (1 <= N <= 26) e que desenhe um triângulo com exatas N linhas, seguindo a
mesma estratégia descrita no texto. Note que o maior triângulo possível é aquele formado por vinte e seis linhas, onde na primeira linha há
apenas um caractere 'A' e na última há somente vinte e seis caracteres 'Z'.

*** Entrada ***

Um número inteiro N (1 <= N <= 26).

*** Saída ***

Um triângulo alfabético com exatas N linhas e com a mesma estratégia de construção mencionada no texto. Note que as letras são sempre maiúsculas.

'''

# RESOLUÇÃO:

lista_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N = int(input())


def exibe_letras_alfabeto(contador):
    posicao_letra = lista_alfabeto[contador - 1]

    i = 1

    while i <= contador:
      letras_alfabeto = posicao_letra * contador
      
      i += 1

    print(letras_alfabeto)


if (1 <= N <= 26):

    i = 1

    while i <= N:
      exibe_letras_alfabeto(i)
      i += 1
