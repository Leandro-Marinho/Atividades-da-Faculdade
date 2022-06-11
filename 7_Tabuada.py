# TABUADA

'''
Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada de N de 1 até 10.

*** Entrada ***

Um número natural N (0 <= N <= 10).

*** Saída ***

Exibir a tabuada do valor dado na entrada.

'''

# RESOLUÇÃO:

N = int(input())

if (0 <= N <= 10):
  contador = 1

  while (contador <= 10):
    print(f'{N} x {contador} = {N * contador}')  
    contador += 1
