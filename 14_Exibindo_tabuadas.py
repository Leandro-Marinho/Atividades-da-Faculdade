# EXIBINDO TABUADAS

'''
Escreva um programa que receba como entrada dois números inteiros quaisquer A e B e exiba todas as tabuadas existentes
no intervalo fechado crescente [A...B].

*** Entrada ***

Dois números inteiros, um em cada linha.

*** Saída ***

As tabuadas de todos os valores inteiros no intervalo fechado crescente [A...B]. Ao fim de cada tabuada, exibir uma linha com dez hifens ('-').
Caso A seja maior do que B, o intervalo será vazio e, neste caso, deve ser exibida somente a frase 'Nenhuma tabuada no intervalo',
sem apóstrofos. Obs.: Lembre-se de não exibir texto no input.

'''

# RESOLUÇÃO:

A = int(input())
B = int(input())

if (A > B):
  print('Nenhuma tabuada no intervalo!')
else:
  for intervalo in range(A, B + 1):
    for i in range(1, 11):
      print(f'{intervalo} x {i} = {intervalo * i}')
    print('----------') 
